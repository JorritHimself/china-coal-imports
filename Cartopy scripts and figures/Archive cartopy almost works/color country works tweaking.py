import matplotlib.pyplot as plt
import matplotlib
import cartopy
from cartopy.io import shapereader
import cartopy.crs as ccrs
import geopandas
import numpy as np
import pandas as pd

# get natural earth data (http://www.naturalearthdata.com/)

# get country borders
resolution = '10m'
category = 'cultural'
name = 'admin_0_countries'
shpfilename = shapereader.natural_earth(resolution, category, name)

# read the shapefile using geopandas
df = geopandas.read_file(shpfilename)


# Set up the map canvas
fig = plt.figure(figsize=(12, 8))
central_lon, central_lat = 100, 30
extent = [73, 135, 18, 50]
ax = plt.axes(projection=cartopy.crs.PlateCarree(central_longitude=central_lon, globe=None))
ax.set_extent(extent)
#ax.gridlines()

# Add natural earth features and borders
ax.add_feature(cartopy.feature.BORDERS, linestyle=':', alpha=1)
ax.add_feature(cartopy.feature.OCEAN, facecolor=("lightblue"))
ax.add_feature(cartopy.feature.LAND)
ax.coastlines(resolution='10m')

# # Add provincial production data
df = geopandas.read_file('./db/CHN_adm1.shp')
prov_prod_df = pd.read_excel('./db/coal_test_data.xlsx', sheet_name='Sheet1')
df = pd.merge(df, prov_prod_df, how='left', on=['ID_1'])





# Insert your lists of countries and lag times here
countries = df['NAME_1_x'].tolist()
lags = df['coal_prod'].tolist()

# Normalise the lag times to between 0 and 1 to extract the colour
lags_norm = (lags-np.nanmin(lags))/(np.nanmax(lags) - np.nanmin(lags))

# Choose your colourmap here
cmap = matplotlib.cm.get_cmap('viridis')


for country, lag_norm in zip(countries, lags_norm):
    # read the borders of the country in this loop
    poly = df.loc[df['NAME_1_x'] == country]['geometry']
    # get the color for this country
    rgba = cmap(lag_norm)
    # plot the country on a map
    ax.add_geometries(poly, crs=ccrs.PlateCarree(), facecolor=rgba, edgecolor='none', zorder=1)

#Add a scatter plot of the original data so the colorbar has the correct numbers. Hacky but it works
dummy_scat = ax.scatter(lags, lags, c=lags, cmap=cmap, zorder=0)
fig.colorbar(mappable=dummy_scat, label='Time lag of phenomenon', orientation='horizontal', shrink=0.8)





# # Insert your lists of countries and lag times here
# # Add provincial production data
# provs_gdf = geopandas.read_file('./db/CHN_adm1.shp')
# prov_prod_df = pd.read_excel('./db/coal_test_data.xlsx', sheet_name='Sheet1')
# provs_gdf = pd.merge(provs_gdf, prov_prod_df, how='left', on=['ID_1'])

# # This from https://stackoverflow.com/questions/61460814/color-cartopy-map-countries-according-to-given-values
# # Insert your lists of countries and lag times here
# prov_list = provs_gdf['NAME_1_x'].tolist()
# prov_prod_list = provs_gdf['coal_prod'].tolist()

# # Normalise the lag times to between 0 and 1 to extract the colour
# prod_normalized = (prov_prod_list-np.nanmin(prov_prod_list))/(np.nanmax(prov_prod_list) - np.nanmin(prov_prod_list))

# # Choose your colourmap here
# cmap = matplotlib.cm.get_cmap('viridis')

# for prov, prov_prod in zip(prov_list, prod_normalized):
#     # read the borders of the country in this loop
#     poly = provs_gdf.loc[provs_gdf['NAME_1_x'] == prov]['geometry'].values[0]
#     # get the color for this country
#     rgba = cmap(prov_prod)
#     # plot the country on a map
#     ax.add_geometries(poly, crs=ccrs.PlateCarree(), facecolor=rgba, edgecolor='none', zorder=1)



# # Add a scatter plot of the original data so the colorbar has the correct numbers. Hacky but it works
# dummy_scat = ax.scatter(prov_prod_list, prov_prod_list, c=prov_prod_list, cmap=cmap, zorder=0)
# fig.colorbar(mappable=dummy_scat, label='Time lag of phenomenon', orientation='horizontal', shrink=0.8)