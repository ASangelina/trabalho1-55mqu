from pyomo.environ import *
graph = [
    [0, 3, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 2, 0],
    [0, 0, 0, 4, 5, 0, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 12],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0]
]
s = 0
t = 6
n = len(graph)

model = ConcreteModel()
model.flow = Var([i for i in range(n)], [j for j in range(n)], domain = Binary)

model.obj = Objective(expr = sum(model.flow[i, j] * graph[i][j] for i in range(n) for j in range(n)), sense = minimize)

model.cons = ConstraintList()

for i in range(n):
    b = 1 if i == s else -1 if i == t else 0
    model.cons.add(expr = ((sum(model.flow[i, j] for j in range(n))) - sum(model.flow[j, i] for j in range(n)) == b))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            model.cons.add(expr = model.flow[i, j] == 0)

opt = SolverFactory('glpk', executable='C:/glpk-4.65/w64/glpsol')
results = opt.solve(model)
#results.write()

for i in range(n):
    for j in range(n):
        if model.flow[i, j]() == 1: print(f'{i} -> {j}')
print(f'Cost: {model.obj()}')
