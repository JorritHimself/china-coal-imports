import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

cmap = mpl.cm.Blues
# Countries is a dictionary of {"country_name": number of users}, for example
countries = {"United States": 100, "Canada": 50, "China": 10}

max_users = float(max(countries.values()))
shapename = 'admin_0_countries'
countries_shp = shpreader.natural_earth(resolution='110m', category='cultural', name=shapename)
ax = plt.axes(projection=ccrs.Robinson())
for country in shpreader.Reader(countries_shp).records():
    name = country.attributes['name_long']
    num_users = countries[name]
    ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(num_users/max_users, 1))

sm = plt.cm.ScalarMappable(cmap=cmap,norm=plt.Normalize(0,1))
sm._A = []
plt.colorbar(sm,ax=ax)

plt.savefig('iOS_heatmap.png', transparent=True, dpi=900)