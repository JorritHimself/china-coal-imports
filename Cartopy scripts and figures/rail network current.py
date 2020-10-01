# Packages 
# import os
import pandas as pd
import numpy as np
import xlrd # Required dependency for pd.read_excel
import re # for some string manipulation with regex
import networkx as nx
import matplotlib.pyplot as plt

# import math
# import json
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import cartopy.feature as cfeature
from IPython.display import Image
# %matplotlib inline

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

# Draw network
#nx.draw_networkx(chinarailmap, pos=dict_pos, node_size=10, labels=None, font_size=8, node_color='blue', width=weights)
#plt.show() 

# Map projection
crs = ccrs.PlateCarree()
fig, ax = plt.subplots(
    1, 1, figsize=(12, 8),
    subplot_kw=dict(projection=crs))
ax.coastlines()



# Create a feature for States/Admin 1 regions at 1:50m from Natural Earth
states_provinces = cfeature.NaturalEarthFeature(
    category='cultural',
    name='admin_1_states_provinces_lines',
    scale='50m',
    facecolor='none')

SOURCE = 'Natural Earth'
LICENSE = 'public domain'


fname = './db/CHN_adm1.shp'
adm1_shapes = list(shpreader.Reader(fname).geometries())

ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.COASTLINE)
#ax.add_feature(states_provinces, edgecolor='gray')
ax.add_geometries(adm1_shapes, ccrs.PlateCarree(),
                  edgecolor='black', facecolor='gray', alpha=0.3)
# Set extent of he plotted map
ax.set_extent([73, 135, 18, 50])
nx.draw_networkx(chinarailmap, ax=ax,
                 font_size=0,
                 node_size=10,
                 labels=None,
                 pos=dict_pos,
                 node_color='blue', 
                 width=weights,
                 cmap=plt.cm.autumn)

plt.savefig('./fig/maprailchinacurrent.png', bbox_inches = 'tight',pad_inches = 0)
plt.savefig('./fig/maprailchinacurrent.pdf',dpi=300, bbox_inches = 'tight',pad_inches = 0)