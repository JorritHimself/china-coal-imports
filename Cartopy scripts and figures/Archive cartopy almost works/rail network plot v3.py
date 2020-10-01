# Packages 
# import os
import pandas as pd
import numpy as np
import xlrd # Required dependency for pd.read_excel
import re # for some string manipulation with regex
import networkx as nx
import matplotlib.pyplot
# from mpl_toolkits.basemap import Basemap
# m = Basemap(
#         projection='merc',
#         llcrnrlon=-130,
#         llcrnrlat=25,
#         urcrnrlon=-60,
#         urcrnrlat=50,
#         lat_ts=0,
#         resolution='i',
#         suppress_ticks=True)

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

#nx.draw_networkx(chinarailmap, node_size=10,node_color='blue', width=weights) # works
nx.draw_networkx(chinarailmap, pos=dict_pos, node_size=10, labels=None, font_size=8, node_color='blue', width=weights)
#nx.draw_networkx_nodes(chinarailmap,pos=dict_pos,node_size=10)

# m.drawcountries()




matplotlib.pyplot.show() 