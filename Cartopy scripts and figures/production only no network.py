# Packages 
# import os
import pandas as pd
import numpy as np
import xlrd # Required dependency for pd.read_excel
import re # for some string manipulation with regex
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import cartopy
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
from cartopy.io import shapereader
import cartopy.feature as cfeature
from IPython.display import Image
import geopandas

# Edges
df_edges = pd.read_excel('./db/Rail network data.xlsx', sheet_name='rail lines')
df_edges = df_edges[['orig_city', 'dest_city', 'capacity_exist_Mty']]
df_edges = df_edges[df_edges['capacity_exist_Mty']!=0]
# Get summed wieght of repeated edges
df_edges= df_edges.groupby(['orig_city','dest_city']).sum()
# And get rid of the  bloody index
df_edges= df_edges.reset_index()
df_edges['weight'] = df_edges['capacity_exist_Mty']/100
# Define map/graph
chinarailmap = nx.Graph()
chinarailmap = nx.from_pandas_edgelist(df_edges, source='orig_city', target='dest_city', edge_attr='weight', create_using=nx.Graph)
edges = chinarailmap.edges()
weights = [chinarailmap[u][v]['weight'] for u,v in edges]

# read in all the nodes
df_nodes = pd.read_excel('./db/Rail network data.xlsx', sheet_name='Station locations')
df_nodes['pos'] = list(zip(df_nodes['long'],df_nodes['lat']))
df_nodes = df_nodes[['city', 'pos']]
dict_pos = dict(zip(df_nodes['city'],df_nodes['pos']))



# Set up the map canvas
fig = plt.figure(figsize=(12, 8))
extent = [73, 135, 18, 50]
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent(extent)
ax.add_feature(cfeature.LAND, facecolor='black', alpha=0.3)
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.OCEAN)
#ax.gridlines()


# # Get province shapefiles
chn_prov_shapes_df = geopandas.read_file('./db/CHN_adm1.shp')
prov_prod_df = pd.read_excel('./db/coal_data_quick.xlsx', sheet_name='Net')
prov_names = pd.read_excel('./db/Chinese prov list.xlsx', sheet_name='Sheet1')
prov_prod_df  = pd.merge(prov_prod_df , prov_names, how='left', left_on='Province', right_on='prov_name')
chn_prov_shapes_df  = pd.merge(chn_prov_shapes_df , prov_names, how='left', left_on='NAME_1', right_on='prov_name')
chn_prov_shapes_df = pd.merge(chn_prov_shapes_df, prov_prod_df, how='left', on=['prov_name_std'])
# Get rid of na's

#test = chn_prov_shapes_df[['NAME_1', 'prov_name', 'Net']]


# Lists of geometries and values to plot
provincelist = chn_prov_shapes_df['prov_name_std'].tolist()
provprodlist = chn_prov_shapes_df['Net'].tolist()

# Colourmap 
# cmap = matplotlib.cm.get_cmap('PiYG')

# This dictionary defines the colormap NOTE this has red and green switched
cdict = {'green':  ((0.0, 0.0, 0.0),   # no red at 0
                  (0.5, 1.0, 1.0),   # all channels set to 1.0 at 0.5 to create white
                  (1.0, 0.8, 0.8)),  # set to 0.8 so its not too bright at 1

        'red': ((0.0, 0.8, 0.8),   # set to 0.8 so its not too bright at 0
                  (0.5, 1.0, 1.0),   # all channels set to 1.0 at 0.5 to create white
                  (1.0, 0.0, 0.0)),  # no green at 1

        'blue':  ((0.0, 0.0, 0.0),   # no blue at 0
                  (0.5, 1.0, 1.0),   # all channels set to 1.0 at 0.5 to create white
                  (1.0, 0.0, 0.0))   # no blue at 1
       }

# Create the colormap using the dictionary
RedGreen = mcolors.LinearSegmentedColormap('RdGn', cdict)
cmap = RedGreen

# Normalise values to between 0 and 1 to extract the colour, with zero on center
# prov_prod_norm = (provprodlist-np.nanmin(provprodlist))/(np.nanmax(provprodlist) - np.nanmin(provprodlist))
offset = mcolors.TwoSlopeNorm(vmin=np.nanmin(provprodlist), vcenter=0., vmax=np.nanmax(provprodlist))
prov_prod_norm = offset(provprodlist)


for prov, prod_norm in zip(provincelist, prov_prod_norm):
    # read the borders of the country in this loop
    poly = chn_prov_shapes_df.loc[chn_prov_shapes_df['prov_name_std'] == prov]['geometry']
    # get the color for this country
    rgba = cmap(prod_norm)
    # plot the country on a map
    ax.add_geometries(poly, crs=ccrs.PlateCarree(), facecolor=rgba, edgecolor='black', zorder=0, alpha=0.8)

# #More simple prov shape plotting, no colour:
# #ax.add_feature(states_provinces, edgecolor='gray')
# ax.add_geometries(adm1_shapes, ccrs.PlateCarree(),
#                   edgecolor='black', facecolor='gray', alpha=0.3)

# # Draw the network
# nx.draw_networkx(chinarailmap, 
#                   ax=ax,
#                   font_size=0,
#                   node_size=10,
#                   labels=None,
#                   pos=dict_pos,
#                   node_color='blue',
#                   edge_color='black',
#                   width=weights)





# set the colormap and centre the colorbar
class MidpointNormalize(mcolors.Normalize):
	"""
	Normalise the colorbar so that diverging bars work there way either side from a prescribed midpoint value)

	e.g. im=ax1.imshow(array, norm=MidpointNormalize(midpoint=0.,vmin=-100, vmax=100))
	"""
	def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
		self.midpoint = midpoint
		mcolors.Normalize.__init__(self, vmin, vmax, clip)

	def __call__(self, value, clip=None):
		# I'm ignoring masked values and all kinds of edge cases to make a
		# simple example...
		x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
		return np.ma.masked_array(np.interp(value, x, y), np.isnan(value))
   
prod_min= np.nanmin(provprodlist)
midpoint_val=0
prod_max=np.nanmax(provprodlist)

### Add a scatter plot of the original data so the colorbar has the correct numbers
dummy_scat = ax.scatter(provprodlist, provprodlist, c=provprodlist, cmap=cmap, zorder=0, norm=MidpointNormalize(vmin=prod_min, midpoint=midpoint_val, vmax=prod_max))
#fig.colorbar(mappable=dummy_scat, label='Net exports', orientation='horizontal', shrink=0.5)
fig.colorbar(mappable=dummy_scat, shrink=0.5)


### Save
plt.savefig('./fig/prod ex rail.png', bbox_inches = 'tight',pad_inches = 0)
plt.savefig('./fig/prod ex rail.pdf',dpi=300, bbox_inches = 'tight',pad_inches = 0)