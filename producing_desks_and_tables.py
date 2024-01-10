from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("GLOP")
infinity = solver.infinity()
x1 = solver.IntVar(0.0, infinity, "x1")
x2 = solver.IntVar(0.0, infinity, "x2")

solver.Add(3*x1 + 5*x2 <= 3600)
solver.Add(x1 + 2*x2 <= 1600)
solver.Add(50*x1 + 20*x2 <= 48000)
solver.Add(x1 >= 0)
solver.Add(x2 >= 0)

solver.Maximize(700*x1+900*x2)
status = solver.Solve()

print(f"Solving with {solver.SolverVersion()}")
if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print("Objective value =", solver.Objective().Value())
        print("x1 =", x1.solution_value())
        print("x2 =", x2.solution_value())
else:
    print("The problem does not have an optimal solution.")
