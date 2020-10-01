"""
Minimal example script for coal transport model China

Has:
    - Multiple bins from different regions, but not with limits on transport
Todo:
    - import input data from xlsx
    - Create duplicate routes
    - Create two-way routes
    - Use a mass multiplier for different CV bins
    - Expand dataset to full rail network with data from KAPSARC
"""     



# Import PuLP modeller functions
from pulp import *

# List of all the nodes
Nodes = ["Shaanxi bin1",
         "Shaanxi bin2",
         "Inner Mongolia",
         "Caofeidian",
         "Hebei",
         "Guangdong",
         "Jiangsu",
         "Australia bin1",
         "Australia bin2"]

nodeData = {# NODE        Supply Demand
         "Shaanxi bin1":    [10000,0],
         "Shaanxi bin2":    [15000,0],
         "Inner Mongolia":  [20000,0],
         "Caofeidian":   [0,0],
         "Hebei":        [0,3000],
         "Guangdong":         [0,4000],
         "Jiangsu":          [0,6000],
         "Australia bin1":    [6000,0],
         "Australia bin2":    [30000,0]
         }

# List of all the arcs
Arcs = [("Shaanxi bin1","Hebei"),
        ("Shaanxi bin2","Hebei"),
        ("Shaanxi bin1","Caofeidian"),
        ("Shaanxi bin2","Caofeidian"),
        ("Inner Mongolia","Hebei"),
        ("Inner Mongolia","Caofeidian"),
        ("Caofeidian","Jiangsu"),
        ("Caofeidian","Guangdong"),
        ("Australia bin1","Jiangsu"),
        ("Australia bin2","Jiangsu"),
        ("Australia bin1","Guangdong"),
        ("Australia bin2","Guangdong"),
        ("Australia bin1","Caofeidian"),
        ("Australia bin2","Caofeidian"),
        ("Caofeidian","Hebei")]

arcData = { #      ARC                Transport cost; Min flow; Max flow
        ("Shaanxi bin1","Hebei"):        [0.5,0,1000],
        ("Shaanxi bin2","Hebei"):        [0.35,0,3000],
        ("Shaanxi bin1","Caofeidian"):        [0.45,0,5000],
        ("Shaanxi bin2","Caofeidian"):        [0.375,0,5000],
        ("Inner Mongolia","Hebei"):        [0.35,0,2000],
        ("Inner Mongolia","Caofeidian"):        [0.45,0,3000],
        ("Caofeidian","Jiangsu"):        [0.4,0,4000],
        ("Caofeidian","Guangdong"):        [0.45,0,2000],
        ("Australia bin1","Jiangsu"):        [0.2,0,5000],
        ("Australia bin2","Jiangsu"):        [0.55,0,6000],
        ("Australia bin1","Guangdong"):        [0.375,0,4000],
        ("Australia bin2","Guangdong"):        [0.65,0,4000],
        ("Australia bin1","Caofeidian"):        [0.6,0,2000],
        ("Australia bin2","Caofeidian"):        [0.12,0,4000],
        ("Caofeidian","Hebei"):        [0.5,0,1000]}


# Splits the dictionaries to be more understandable
(supply, demand) = splitDict(nodeData)
(costs, mins, maxs) = splitDict(arcData)

# Creates the boundless Variables as Integers
vars = LpVariable.dicts("Route",Arcs,None,None,LpInteger)

# Creates the upper and lower bounds on the variables
for a in Arcs:
    vars[a].bounds(mins[a], maxs[a])

# Creates the 'prob' variable to contain the problem data    
prob = LpProblem("China coal problem",LpMinimize)

# Creates the objective function
# @@ Needs to add prod costs
prob += lpSum([vars[a]* costs[a] for a in Arcs]), "Total Cost of Transport"

# Constraints section
# Constraint: amount going into each node is at least equal to the amount leaving (i.e., no storage)
# @@ This might need fixin when we allow import/export supply nodes to take in much coal
for n in Nodes:
    prob += (supply[n]+ lpSum([vars[(i,j)] for (i,j) in Arcs if j == n]) >=
             demand[n]+ lpSum([vars[(i,j)] for (i,j) in Arcs if i == n])), "Steel Flow Conservation in Node %s"%n



# The problem data is written to an .lp file
prob.writeLP("ChinaCoalProblem.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen    
print("Total Cost of Transportation = ", value(prob.objective))