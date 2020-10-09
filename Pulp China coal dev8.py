"""
Minimal example script for coal transport model China

Has:
    - import input data from xlsx
    - Multiple supply bins/steps from different regions
    - Different suplhur and enegry content per supply step
    - Transport capacity limited by Mt
    - Demand requirment in GJ
    - Consumption limit of total sulphur
Todo:
    - Create duplicate routes for trucks and rails
    - Create two-way routes    
    - Create trans-shipping hubs: connect 
    - Expand dataset to full rail network with data from KAPSARC
    - Export problem solution to csv or xlsx maybe
    Met vs Thermal coal:
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
df_nodes = pd.read_excel('./data/chinacoaldb TEST v8.xlsx', sheet_name='node data')
df_edges = pd.read_excel('./data/chinacoaldb TEST v8.xlsx', sheet_name='edge data')
df_supply = pd.read_excel('./data/chinacoaldb TEST v8.xlsx', sheet_name='supply data')
df_coaltypes = pd.read_excel('./data/chinacoaldb TEST v8.xlsx', sheet_name='coal type data')

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
nodelist_temp_df.insert(2, 'mergevar', 1, allow_duplicates= True)
coaltypelist_temp_df.insert(2, 'mergevar', 1, allow_duplicates= True)
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
flowslist.insert(2, 'mergevar', 1, allow_duplicates= True)
flowslist = pd.merge(flowslist, coaltypelist_temp_df, how='outer', on='mergevar')
flowslist = flowslist[['from', 'to', 'coaltype']]
flowslist = list(flowslist.itertuples(index=False, name=None))

##################   MODEL SECTION ###########################################
##### Define the problem variable and optimizaton type    
cn_coal_problem = LpProblem("China coal cost problem",LpMinimize)

# Create problem variables, either as integers or continuous. 
# This uses list comprehension on 'edgelist'. Options: cat=LpInteger or cat=LpContinuous
massflowtot = LpVariable.dicts("flow_total",edgelist,lowBound = 0,upBound=None,cat=LpContinuous)
massflowtype = LpVariable.dicts("flow_by_coaltype",flowslist,lowBound = 0,upBound=None,cat=LpContinuous)
supplyitembynode = LpVariable.dicts("supply_coaltype_by_node",supplylist,lowBound = 0,upBound=None,cat=LpContinuous)



# Constraint: Mass Balance pt1: nodes cannot supply coal types they do not have to other nodes or to fulfill own demand
for item in supplylist:
    supplyitembynode[item].bounds(0, supply[item])

# Constraint: Mass Balance pt2: amount of each coal type flowing out of each node cannot exceed supply plus amount flowing into of each node
# Note: demand in each node here is irrelevant, as nodes demand GJ not tons of some type of coal
for item in supplylist:
    cn_coal_problem += (supplyitembynode[item]+ 
                        lpSum([massflowtype[(i,j,ct)] for (i,j,ct) in flowslist if (j,ct) == item]) >=
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

# Constraint: total sulfur influx cannot exceed sulfur consumption limits
# supply of each coal type in each node multiplied with sulfur content of that coaltype +
# flows of each coal type into that node multiplied with sulfur content of that coaltype -
# flows of each coal type out of that node multiplied with sulfur content of that coaltype <=
# max sulfur consumption within that node
for node in nodelist:
    cn_coal_problem += (lpSum([supplyitembynode[(i,ct)]*sulfurcontent[ct] for (i,ct) in supplylist if i == node]) + 
                        lpSum([massflowtype[(i,j,ct)]*sulfurcontent[ct] for (i,j,ct) in flowslist if j == node]) - 
                        lpSum([massflowtype[(i,j,ct)]*energycontent[ct] for (i,j,ct) in flowslist if i == node]) <=
                        sulfurmax[node]
                        )
    
# Constraint: Flows of each type of coal over each edge cannot be negative
# This is dealt with in the variable definition

# Constraint: transport capacity of each edge cannot be exceeded
# Total flows of all types of coal over each edge cannot exceed the edges' transport capacity
for edge in edgelist:
    cn_coal_problem += (lpSum([massflowtype[(i,j,ct)] for (i,j,ct) in flowslist if (i, j) == edge]) <= maxflowMt[edge])
# For reporting, not a cosnstraint: massflowtotal over each edge is the sum of all flows by coaltype
for edge in edgelist:
    cn_coal_problem += (massflowtot[edge] == lpSum([massflowtype[(i,j,ct)] for (i,j,ct) in flowslist if (i, j) == edge]))
                                       
    
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
print("")
# Print optimal flows along each of the edges
for v in cn_coal_problem.variables():
        print(v.name, "=", v.varValue) 
print("")
print("Summary:")
# Print optimal flows along each of the edges sumary: output limited to lines that are non-zero
for v in cn_coal_problem.variables():
    if v.varValue!=0:
        print(v.name, "=", v.varValue) 
# Print total costs 
#print("Total prod costs are = ", lpSum([massflowtot[edge]*transportcosts[edge] for edge in edgelist]))
print("")
print("Total prod and transport costs are = ", value(cn_coal_problem.objective))
print("")

### Export solution to some csv or xlsx file
# To do





