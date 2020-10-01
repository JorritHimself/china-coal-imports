from pulp import *

prob = LpProblem('glass', LpMaximize)

# Declare variables.
x1 = LpVariable('x1_var', lowBound=0, upBound=None, cat=LpContinuous)
x2 = LpVariable('x2_var', lowBound=0, upBound=None, cat=LpContinuous)

# Build objective function.
prob += 3 * x1 + 5 * x2

# Add constraints.    
prob += x1 <= 4
prob += 2 * x2 <= 12
prob += 3 * x1 + 2 * x2 <= 18

# Solve problem.
prob.solve()

# Print status.
print("Status:", LpStatus[prob.status], "\n")

print("The value of x1 = {}. (Not what we want.)".format(x1))
print("The values of x1.value() and x1.varValue = {} and {}. (That's what we want.)\n".format(x1.value(), x1.varValue))

# Print optimal values of decision variables.
print("All variables:")
for v in prob.variables():
    print(v.name, "=", v.varValue)