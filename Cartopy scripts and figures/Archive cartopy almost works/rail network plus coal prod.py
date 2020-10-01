# Packages 
# import os
import pandas as pd
import numpy as np
import xlrd # Required dependency for pd.read_excel
import re # for some string manipulation with regex
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import cartopy.feature as cfeature
from IPython.display import Image
import geopandas



# read in all the edges
df_edges = pd.read_excel('./db/Rail network data.xlsx', sheet_name='rail lines')
df_edges = df_edges[['orig_city', 'dest_city', 'capacity_exist_Mty']]
df_edges = df_edges[df_edges['capacity_exist_Mty']!=0]
# Get summed wieght of reapted edges
df_edges= df_edges.groupby(['orig_city','dest_city']).sum()
# And get rid of the  bloody index
df_edges= df_edges.reset_index()
df_edges['weight'] = df_edges['capacity_exist_Mty']/100

# Define map/graph
chinarailmap = nx.Graph()
chinarailmap = nx.from_pandas_edgelist(df_edges, source='orig_city', target='dest_city', edge_attr='weight', create_using=nx.Graph)
#nx.draw(chinarailmap)
edges = chinarailmap.edges()
weights = [chinarailmap[u][v]['weight'] for u,v in edges]

# read in all the nodes
df_nodes = pd.read_excel('./db/Rail network data.xlsx', sheet_name='Station locations')
df_nodes['pos'] = list(zip(df_nodes['long'],df_nodes['lat']))
df_nodes = df_nodes[['city', 'pos']]
dict_pos = dict(zip(df_nodes['city'],df_nodes['pos']))

# Map projection
crs = ccrs.PlateCarree()
fig, ax = plt.subplots(
    1, 1, figsize=(12, 8),
    subplot_kw=dict(projection=crs))
ax.coastlines()

# Get prov shapes
fname = './db/CHN_adm1.shp'
adm1_shapes = list(shpreader.Reader(fname).geometries())
# Add maps stuffs
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.COASTLINE)
#ax.add_feature(states_provinces, edgecolor='gray')
ax.add_geometries(adm1_shapes, ccrs.PlateCarree(),
                  edgecolor='black', facecolor='gray', alpha=0.3)
# Set extent of he plotted map
ax.set_extent([73, 135, 18, 50])

# Add provincial production data
provs_gdf = geopandas.read_file('./db/CHN_adm1.shp')
prov_prod_df = pd.read_excel('./db/coal_test_data.xlsx', sheet_name='Sheet1')
provs_gdf = pd.merge(provs_gdf, prov_prod_df, how='left', on=['ID_1'])


# This from https://stackoverflow.com/questions/61460814/color-cartopy-map-countries-according-to-given-values
# Insert your lists of countries and lag times here
prov_list = provs_gdf['NAME_1_x'].tolist()
prov_prod_list = provs_gdf['coal_prod'].tolist()


# Normalise the lag times to between 0 and 1 to extract the colour
prod_normalized = (prov_prod_list-np.nanmin(prov_prod_list))/(np.nanmax(prov_prod_list) - np.nanmin(prov_prod_list))

# Choose your colourmap here
cmap = matplotlib.cm.get_cmap('viridis')


for prov, prov_prod in zip(prov_list, prov_prod_list):
    # read the borders of the country in this loop
    poly = provs_gdf.loc[provs_gdf['NAME_1_x'] == prov]['geometry'].values[0]
    # get the color for this country
    rgba = cmap(prod_normalized)
    # plot the country on a map
    ax.add_geometries(poly, crs=ccrs.PlateCarree(), facecolor=rgba, edgecolor='none', zorder=1)

# # Add a scatter plot of the original data so the colorbar has the correct numbers. Hacky but it works
# dummy_scat = ax.scatter(lags, lags, c=lags, cmap=cmap, zorder=0)
# fig.colorbar(mappable=dummy_scat, label='Time lag of phenomenon', orientation='horizontal', shrink=0.8)



# for col in provs_gdf.columns: 
#     print(col) 



# # Add the network
# nx.draw_networkx(chinarailmap, ax=ax,
#                  font_size=0,
#                  node_size=10,
#                  labels=None,
#                  pos=dict_pos,
#                  node_color='blue', 
#                  width=weights,
#                  cmap=plt.cm.autumn)

# plt.savefig('./fig/maprailchinacurrent.png')
# plt.savefig('./fig/maprailchinacurrent.pdf',dpi=300)