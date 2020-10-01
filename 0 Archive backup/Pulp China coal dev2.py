"""
Minimal example script for coal transport model China

Has:
    - import input data from xlsx
    - Multiple bins from different regions, but not with limits on transport
Todo:
    - Create separate weight and GJ flows
    - Add production costs for each bin on the first line that exits a coal mine. This will mean summing truck and 
    - Create duplicate routes
    - Create two-way routes
    - Use a mass multiplier for different CV bins
    - Expand dataset to full rail network with data from KAPSARC
    - Try multi-index instead of tuple index
    - 
"""    
# Packages
import pandas as pd
import numpy as np
import xlrd # Required dependency for pd.read_excel
import re # for some string manipulation with regex
# Import PuLP modeller functions
from pulp import *

# Read in basic node and edge data
df_nodes = pd.read_excel('./data/chinacoaldb TEST.xlsx', sheet_name='node data')
df_edges = pd.read_excel('./data/chinacoaldb TEST.xlsx', sheet_name='edge data')


########   Convoluted way to read in data and get in the needed shape
# List of all the nodes
Nodes = df_nodes['nodename'].to_list()
# nodeData 
nodeData = df_nodes.set_index('nodename')
nodeData  = nodeData.T.to_dict('list')
# List of all the edges
edgelist = df_edges[['from', 'to']]
Arcs = list(edgelist.itertuples(index=False, name=None))
# Edge data  
arcData = df_edges
arcData['fromto'] = list(zip(arcData['from'], arcData['to']))
arcData = arcData.drop(['from', 'to'], axis = 1) 
arcData = arcData.set_index(['fromto'])
arcData  = arcData.T.to_dict('list')




# Splits the dictionaries to be more understandable
(supply, prodcost, demand) = splitDict(nodeData)
(costs, mins, maxs) = splitDict(arcData)

# Creates the boundless Variables as Integers
# This uses list comprehension on 'edgelist'
vars = LpVariable.dicts("Route",Arcs,None,None,cat='Integer')



# Set upper and lower bounds on the flow in each edge
# Not too sure you could have negative values represent flow the other dircetion here. Probably bets to keep all as positive flows
for a in Arcs:
    vars[a].bounds(mins[a], maxs[a])

# Creates the 'prob' variable to contain the problem data    
cn_coal_problem = LpProblem("China coal cost problem",LpMinimize)

# Objective function
# @@ Needs to add prod costs
cn_coal_problem += lpSum([vars[a]*costs[a] for a in Arcs]) 

# Transport constraints
#prob += maxs[('Australia', 'Caofeidian')] + maxs[('Australia', 'Guangdong')] <= 5000

# Constraints section
# Constraint: amount going into each node is at least equal to the amount leaving (i.e., no storage)
# @@ This might need fixin when we allow import/export supply nodes to take in much coal
for n in Nodes:
    cn_coal_problem += (supply[n]+ lpSum([vars[(i,j)] for (i,j) in Arcs if j == n]) >=
                     demand[n]+ lpSum([vars[(i,j)] for (i,j) in Arcs if i == n]))
    




# Add constraint for different CV bins
# Or how do we do this?


# Write problem data to file
cn_coal_problem.writeLP("ChinaCoalProblem.lp")
# Solve with default solver
cn_coal_problem.solve()
# Print solver status 
print("Status:", LpStatus[cn_coal_problem.status])
# Print all flows 
for v in cn_coal_problem.variables():
    print(v.name, "=", v.varValue)
# Print total costs 
print("Total Costs are = ", value(cn_coal_problem.objective))