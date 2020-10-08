"""
Minimal example script for coal transport model China

Has:
    - import input data from xlsx
    - Multiple bins from different regions, but not with limits on transport
Todo:
    - Different cost/supply bins: for each mine, have each supply bin be one flow/edge into a generic mine-outflow-node.
        Then transport constraints after that are shared. Production costs can then be assigned to each of the edges from the mine into the mine-outflow-node
    - Create separate weight and GJ flows: use a mass multiplier for different CV bins somehow
    - Create duplicate routes for trucks and rails
    - Create two-way routes    
    - Create trans-shipping hubs: connect 
    - Expand dataset to full rail network with data from KAPSARC
    - Try multi-index instead of tuple index. Current system is just stupid.
    - 
"""    
# Packages
import pandas as pd
import numpy as np
import xlrd # Required dependency for pd.read_excel
import re # for some string manipulation with regex
# Import PuLP modeller functions
from pulp import *

# Read in node and edge data from file
df_nodelist = pd.read_excel('./data/chinacoaldb TEST with diff coal types.xlsx', sheet_name='node data')
df_edges = pd.read_excel('./data/chinacoaldb TEST with diff coal types.xlsx', sheet_name='edge data')

########   Convoluted way to get xlsx into panda df into required shape
# List of all the nodes
nodelist = df_nodelist['nodename'].drop_duplicates(keep='first').to_list()

# nodedata: only pure node level data, supply of each coal type is separate 
nodedata = df_nodelist.set_index('nodename')
nodedata = nodedata.drop(['nodetype'], axis = 1)


nodedata  = nodedata.T.to_dict('list')
# Split data dictionary so we can use variable names more easily in below problem definition
(coaltype, supply, prodcost, demand, energycontent, sulfurcontent, sulfurmax) = splitDict(nodedata)


# List of all the edges
edgelist = df_edges[['from', 'to']]
edgelist = list(edgelist.itertuples(index=False, name=None))
# Edge data  
edgedata = df_edges
edgedata['fromto'] = list(zip(edgedata['from'], edgedata['to']))
edgedata = edgedata.drop(['from', 'to', 'transshipment cost', 'distance', 'cost pkm'], axis = 1) 
edgedata = edgedata.set_index(['fromto'])
edgedata  = edgedata.T.to_dict('list')
# Split data dictionary so we can use variable names more easily in below problem definition
(transportcosts, mins, maxs) = splitDict(edgedata)

# List of all coal types
coaltypelist = df_nodelist['coaltype'].dropna().to_list()
# Coal type data
coaltypedata = df_nodelist[['coaltype', 'energy content', 'sulfur content']].dropna()
coaltypedata = coaltypedata.set_index(['coaltype'])

##### Supply list
# Full list of nodes and coal types
# List with unique and non-missing values
df_nodes_temp = df_nodelist[['nodename']].drop_duplicates('nodename').dropna()
df_coaltypes_temp = df_nodelist[['coaltype']].drop_duplicates().dropna()
# df with all combinations

aatest = list(itertools.product(nodelist, coaltypelist))



supplylist = pd.merge(df_nodes_temp, df_coaltypes_temp, left_on=None, right_on=None, how='outer')


df_nodes_temp

supplylisttemp = df_nodelist
supplylisttemp = supplylisttemp.drop(['demand', 'energy content', 'sulfur content', 'sulfmax', 'nodetype'], axis = 1) 








##### Define the problem variable and optimizaton type    
cn_coal_problem = LpProblem("China coal cost problem",LpMinimize)

# Create problem variables, either as integers or continuous. 
# This uses list comprehension on 'edgelist'. Options: cat=LpInteger or cat=LpContinuous
massflow = LpVariable.dicts("flow_total",edgelist,None,None,cat=LpInteger)


##### Constraints section
# Transport network limits: set upper and lower bounds on the flow in each edge
# Not too sure you could have negative values represent flow the other dircetion here. Probably bets to keep all as positive flows
for edge in edgelist:
    massflow[edge].bounds(mins[edge], maxs[edge])
    
    


# Constraint: amount of each coal type going into each node is at least equal to the amount leaving or demanded 
# @@ This might need fixin when we allow import/export supply nodelist to take in unrestricted amounts of coal
#Mass Balance:
for ct in coaltypelist:
    for node in nodelist:
        cn_coal_problem += (supply[node]+ lpSum([massflow[(i,j)] for (i,j) in edgelist if j == node]) >=
                            demand[node]+ lpSum([massflow[(i,j)] for (i,j) in edgelist if i == node]))
# Energy balance


# Maxflow limits, sum stuffs 


# Min GJ and max sulfur consumption



    
##### Objective function
cn_coal_problem += (lpSum([massflow[edge]*transportcosts[edge] for edge in edgelist]) + # all transport costs
                    lpSum([massflow[(i,j)]*prodcost[i] for (i,j) in edgelist]) # all production costs, and remember all non-producing nodes are included in this sum but have 0 supply and 0 prod costs
                    )



    

# Write problem data to file
cn_coal_problem.writeLP("ChinaCoalProblem.lp")
# Solve with default solver
cn_coal_problem.solve()
# Print solver status 
print("Status:", LpStatus[cn_coal_problem.status])
# Print optimal flows along each of the edges
for v in cn_coal_problem.variables():
    print(v.name, "=", v.varValue)
# Print total costs 
print("Total prod and transport costs are = ", value(cn_coal_problem.objective))