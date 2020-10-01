import matplotlib.pyplot as plt
import matplotlib
import cartopy
from cartopy.io import shapereader
import cartopy.io.shapereader as shpreader
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import geopandas
import numpy as np

# get natural earth data (http://www.naturalearthdata.com/)

# get country borders
resolution = '10m'
category = 'cultural'
name = 'admin_1_states_provinces'
shpfilename = shapereader.natural_earth(resolution, category, name)

# read the shapefile using geopandas
df = geopandas.read_file(shpfilename)


# Set up the map canvas
fig = plt.figure(figsize=(12, 8))
central_lon, central_lat = 100, 30
extent = [73, 135, 18, 50]
ax = plt.axes(projection=cartopy.crs.PlateCarree(central_longitude=central_lon, globe=None))
ax.set_extent(extent)
ax.gridlines()

provs_gdf = geopandas.read_file('./db/CHN_adm1.shp')
adm1_shapes = list(shpreader.Reader(provs_gdf).geometries())





# Add natural earth features and borders
ax.add_feature(cartopy.feature.BORDERS, linestyle=':', alpha=1)
ax.add_feature(cartopy.feature.OCEAN, facecolor=("lightblue"))
ax.add_feature(cartopy.feature.LAND)
ax.coastlines(resolution='10m')
ax.add_feature(provs_gdf, edgecolor='gray')


# for country in shpreader.Reader(countries_shp).records():
#     name = country.attributes['name_long']
#     num_users = countries[name]
#     ax.add_geometries(country.geometry, ccrs.PlateCarree(),
#                 facecolor=cmap(num_users/max_users, 1))

# for country, lag_norm in zip(countries, lags_norm):
#     # read the borders of the country in this loop
#     poly = df.loc[df['ADMIN'] == country]['geometry'].values[0]
#     # get the color for this country
#     rgba = cmap(lag_norm)
#     # plot the country on a map
#     ax.add_geometries(poly, crs=ccrs.PlateCarree(), facecolor=rgba, edgecolor='none', zorder=1)

# Add a scatter plot of the original data so the colorbar has the correct numbers. Hacky but it works
# dummy_scat = ax.scatter(lags, lags, c=lags, cmap=cmap, zorder=0)
# fig.colorbar(mappable=dummy_scat, label='Time lag of phenomenon', orientation='horizontal', shrink=0.8)
