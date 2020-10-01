import matplotlib.pyplot as plt
import matplotlib
import cartopy
from cartopy.io import shapereader
import cartopy.crs as ccrs
import geopandas
import numpy as np

# get natural earth data (http://www.naturalearthdata.com/)

# get country borders
resolution = '10m'
category = 'cultural'
name = 'admin_0_countries'
shpfilename = shapereader.natural_earth(resolution, category, name)

# read the shapefile using geopandas
df = geopandas.read_file(shpfilename)


# Set up the canvas
fig = plt.figure(figsize=(8, 8))
central_lon, central_lat = 0, 45
extent = [-10, 45, 35, 70]
ax = plt.axes(projection=cartopy.crs.Orthographic(central_lon, central_lat))
ax.set_extent(extent)
ax.gridlines()

# Add natural earth features and borders
ax.add_feature(cartopy.feature.BORDERS, linestyle=':', alpha=1)
ax.add_feature(cartopy.feature.OCEAN, facecolor=("lightblue"))
ax.add_feature(cartopy.feature.LAND)
ax.coastlines(resolution='10m')

# Insert your lists of countries and lag times here
countries = ['Germany', 'France', 'Italy', 'Spain', 'Belgium', 'Netherlands', 'Portugal', 'Poland', 'United Kingdom', 'Switzerland', 'Ireland']
lags = [-20,-5, 15, 0, 2, 10, 12, 8, -15, 3, -8, 10]

# Normalise the lag times to between 0 and 1 to extract the colour
lags_norm = (lags-np.nanmin(lags))/(np.nanmax(lags) - np.nanmin(lags))

# Choose your colourmap here
cmap = matplotlib.cm.get_cmap('tab10')


for country, lag_norm in zip(countries, lags_norm):
    # read the borders of the country in this loop
    poly = df.loc[df['ADMIN'] == country]['geometry']
    # get the color for this country
    rgba = cmap(lag_norm)
    # plot the country on a map
    ax.add_geometries(poly, crs=ccrs.PlateCarree(), facecolor=rgba, edgecolor='none', zorder=1)

#Add a scatter plot of the original data so the colorbar has the correct numbers. Hacky but it works
dummy_scat = ax.scatter(lags, lags, c=lags, cmap=cmap, zorder=0)
fig.colorbar(mappable=dummy_scat, label='Ugliness', orientation='horizontal', shrink=0.8)
