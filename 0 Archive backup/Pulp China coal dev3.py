"""
Minimal example script for coal transport model China

Has:
    - import input data from xlsx
    - Multiple bins from different regions, but not with limits on transport
Todo:
    - Differetn cost/supply bins: for each mine, have each supply bin be one flow/edge into a generic mine-outflow-node.
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
df_nodelist = pd.read_excel('./data/chinacoaldb TEST.xlsx', sheet_name='node data')
df_edges = pd.read_excel('./data/chinacoaldb TEST.xlsx', sheet_name='edge data')

########   Convoluted way to get panda df into the required shape
# List of all the nodelist
nodelist = df_nodelist['nodename'].to_list()
# nodedata 
nodedata = df_nodelist.set_index('nodename')
nodedata  = nodedata.T.to_dict('list')
# List of all the edges
edgelist = df_edges[['from', 'to']]
edgelist = list(edgelist.itertuples(index=False, name=None))
# Edge data  
edgedata = df_edges
edgedata['fromto'] = list(zip(edgedata['from'], edgedata['to']))
edgedata = edgedata.drop(['from', 'to'], axis = 1) 
edgedata = edgedata.set_index(['fromto'])
edgedata  = edgedata.T.to_dict('list')


# Splits data dictionaries so we can use varibale names in below probelme defintion more easily
(supply, prodcost, demand) = splitDict(nodedata)
(costs, mins, maxs) = splitDict(edgedata)

# Creates problem variables, either as integers or continuous. 
# This uses list comprehension on 'edgelist'
#vars = LpVariable.dicts("Route",edgelist,None,None,cat=LpContinuous)
vars = LpVariable.dicts("directional edge",edgelist,None,None,cat=LpInteger)

# Set upper and lower bounds on the flow in each edge
# Not too sure you could have negative values represent flow the other dircetion here. Probably bets to keep all as positive flows
for a in edgelist:
    vars[a].bounds(mins[a], maxs[a])

# Creates the 'prob' variable to contain the problem data    
cn_coal_problem = LpProblem("China coal cost problem",LpMinimize)

# Objective function
cn_coal_problem += lpSum([vars[a]*costs[a] for a in edgelist]) 

# Constraints section
# Constraint: amount going into each node is at least equal to the amount leaving or demanded 
# @@ This might need fixin when we allow import/export supply nodelist to take in unrestricted amounts of coal
for n in nodelist:
    cn_coal_problem += (supply[n]+ lpSum([vars[(i,j)] for (i,j) in edgelist if j == n]) >=
                        demand[n]+ lpSum([vars[(i,j)] for (i,j) in edgelist if i == n]))
    

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