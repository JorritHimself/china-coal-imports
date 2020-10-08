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
    - Use met/thermal difference as different columns in both supply and demand in xlsx
    - Met coal coversnion can be done at demand node: is enegy content*0.x
"""    
# Packages
import pandas as pd
import numpy as np
import xlrd # Required dependency for pd.read_excel
import re # for some string manipulation with regex
# Import PuLP modeller functions
from pulp import *

# Read in node and edge data from file
df_nodes = pd.read_excel('./data/chinacoaldb TEST with diff coal types.xlsx', sheet_name='node data')
df_edges = pd.read_excel('./data/chinacoaldb TEST with diff coal types.xlsx', sheet_name='edge data')
df_supply = pd.read_excel('./data/chinacoaldb TEST with diff coal types.xlsx', sheet_name='supply data')
df_coaltypes = pd.read_excel('./data/chinacoaldb TEST with diff coal types.xlsx', sheet_name='coal type data')

########   Import all data from xlsx 
### List of all the nodes
nodelist = df_nodes['nodename'].drop_duplicates(keep='first').to_list()
### nodedata: only data specific to node, supply of each coal type is separate 
nodedata = df_nodes.set_index('nodename')
nodedata = nodedata.drop(['nodetype'], axis = 1)
nodedata  = nodedata.T.to_dict('list')
(demand, sulfurmax) = splitDict(nodedata) # Splits data dictionary so we can use variable names more easily in below problem definition
### List of all the edges
edgelist = df_edges[['from', 'to']]
edgelist = list(edgelist.itertuples(index=False, name=None))
### Edge data  
edgedata = df_edges
edgedata['fromto'] = list(zip(edgedata['from'], edgedata['to']))
edgedata = edgedata.drop(['from', 'to', 'transshipment cost', 'distance', 'cost pkm'], axis = 1) 
edgedata = edgedata.set_index(['fromto'])
edgedata  = edgedata.T.to_dict('list')
(transportcosts, minflowMt, maxflowMt) = splitDict(edgedata) # Splits data dictionary so we can use variable names more easily in below problem definition

### List of all coal types
coaltypelist = df_coaltypes['coaltype'].dropna().to_list()
### Coal type data
coaltypedata = df_coaltypes
coaltypedata = coaltypedata.set_index(['coaltype'])
coaltypedata  = coaltypedata.T.to_dict('list')
(energycontent, sulfurcontent) = splitDict(coaltypedata)

### Supply list: combinations of all nodes and coaltypes
## Create full list of nodes and coal types, with unique and non-missing values
nodelist_temp_df = df_nodes[['nodename', 'demand']] # Need to keep 2 vars for maintaining df structure
coaltypelist_temp_df = df_coaltypes[['coaltype', 'energy content']] # Need to keep 2 vars for maintaining df structure
nodelist_temp_df['mergevar'] = 1
coaltypelist_temp_df['mergevar'] = 1
supplylist = pd.merge(nodelist_temp_df, coaltypelist_temp_df, how='outer', on='mergevar')
supplylist_temp = supplylist.drop(['demand', 'energy content', 'mergevar'], axis = 1) 
# Expand supply limits to all combinations of nodes and coal types
supplydata = df_supply
supplydata = pd.merge(supplylist_temp, supplydata, how='left', on=['nodename', 'coaltype']).fillna(value=0)
supplydata['indextemp'] = list(zip(supplydata['nodename'], supplydata['coaltype']))
supplydata = supplydata.set_index(['indextemp'])
supplydata = supplydata.drop(['nodename', 'coaltype'], axis = 1) 
supplydata  = supplydata.T.to_dict('list')
(supply, prodcosts) = splitDict(supplydata) # Splits data dictionary so we can use variable names more easily in below problem definition
# And only now make list out of the supplylist
supplylist = list(supplylist_temp.itertuples(index=False, name=None)) 

### Flows list: combinations of all edges and coaltypes
flowslist = df_edges[['from', 'to']]
flowslist['mergevar'] = 1
flowslist = pd.merge(flowslist, coaltypelist_temp_df, how='outer', on='mergevar')
flowslist = flowslist[['from', 'to', 'coaltype']]
flowslist = list(flowslist.itertuples(index=False, name=None))



# Does it limit supply of each item?
# Does it limit flows per section in total MT?
# Does it limit flows per demadn in GJ?
# Does it limit flows per demadn in consumption limit sulfur?




##### Define the problem variable and optimizaton type    
cn_coal_problem = LpProblem("China coal cost problem",LpMinimize)

# Create problem variables, either as integers or continuous. 
# This uses list comprehension on 'edgelist'. Options: cat=LpInteger or cat=LpContinuous
massflowtot = LpVariable.dicts("flow_total",edgelist,None,None,cat=LpInteger)
massflowtype = LpVariable.dicts("flow_by_coaltype",flowslist,None,None,cat=LpInteger)
supplyitembynode = LpVariable.dicts("supply_coaltype_by_node",supply,None,None,cat=LpInteger)



# Constraint: Mass Balance: amount of each coal type going into each node is at least equal to the amount leaving
# Note: demand in each node here is irrelevant, as nodes demand GJ not tons of some type of coal
for item in supplylist:
    cn_coal_problem += (supply[item]+ lpSum([massflowtype[(i,j,ct)] for (i,j,ct) in flowslist if (j,ct) == item]) >=
                        lpSum([massflowtype[(i,j,ct)] for (i,j,ct) in flowslist if (i,ct) == item]))

# Constraint: Energy demand must be satisfied, whilst supply nodes may have energy left over
# supply of each coal type in each node multiplied with energy content of that coaltype +
# flows of each coal type into that node multiplied with energy content of that coaltype >=
# total energy demand within that node +
# flows of each coal type out of that node multiplied with energy content of that coaltype
for node in nodelist:
    cn_coal_problem += (lpSum([supplyitembynode[(i,ct)]*energycontent[ct] for (i,ct) in supplylist if i == node]) + 
                        lpSum([massflowtype[(i,j,ct)]*energycontent[ct] for (i,j,ct) in flowslist if j == node]) >= 
                        demand[node] + 
                        lpSum([massflowtype[(i,j,ct)]*energycontent[ct] for (i,j,ct) in flowslist if i == node]))
  
# Constraint: transport capacity of each edge cannot be exceeded
# Flows of each type fo coal over each edge cannot be negative
# Total flows of all types of coal over each edge cannot exceed the edges' capacity
for flow in flowslist:
    massflowtype[flow].bounds(0, None)
for edge in edgelist:
    cn_coal_problem += (lpSum([massflowtype[(i,j,ct)] for (i,j,ct) in flowslist if (i, j) == edge]) <= maxflowMt[edge])




# Max sulfur consumption
# For now: sulf in minus sulf out <= sulfmax


    
##### Objective function
cn_coal_problem += (lpSum([massflowtot[edge]*transportcosts[edge] for edge in edgelist]) + # all transport costs
                    lpSum([massflowtype[(i,j,ct)]*prodcosts[i,ct] for (i,j,ct) in flowslist]) # all production costs, and remember all non-producing nodes are included in this sum but have 0 supply and 0 prod costs
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