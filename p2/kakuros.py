from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re
import sys

from ortools.sat.python import cp_model
txt_values = []

# reading txt file

filehandle = open(sys.argv[1], 'r')
while True:
    line = filehandle.readline()
    if not line:
        break
    txt_values.append(re.findall(r'\d+', line))
filehandle.close()



#print(txt_values[0])
#print(txt_values[1])

# converts each array values to a variable

r1 = txt_values[1][0]
r2 = txt_values[1][1]
r3 = txt_values[1][2]

c1 = txt_values[0][0]
c2 = txt_values[0][1]
c3 = txt_values[0][2]

#print(r1, r2, r3)
#print(c1, c2, c3)




def kakuro_solver():
    """Minimal CP-SAT example to showcase calling the solver."""
    # Creates the model.
    model = cp_model.CpModel()
    # Creates the variables.
    num_vals = 10
    x1 = model.NewIntVar(1, num_vals - 1, "x1")
    x2 = model.NewIntVar(1, num_vals - 1, "x2")
    x3 = model.NewIntVar(1, num_vals - 1, "x3")
    y1 = model.NewIntVar(1, num_vals - 1, "y1")
    y2 = model.NewIntVar(1, num_vals - 1, "y2")
    y3 = model.NewIntVar(1, num_vals - 1, "y3")
    z1 = model.NewIntVar(1, num_vals - 1, "z1")
    z2 = model.NewIntVar(1, num_vals - 1, "z2")
    z3 = model.NewIntVar(1, num_vals - 1, "z3")
    # Adds an all-different constraint.
    model.Add(x1 != x2)
    model.Add(x1 != x3)
    model.Add(y1 != y2 != y3)
    model.Add(z1 != z2 != z3)
    model.Add(x1 != y1 != z1)
    model.Add(x2 != y2 != z2)
    model.Add(x3 != y3 != z3)
    model.Add(x1 + x2 + x3 == int(r1))
    model.Add(y1 + y2 + y3 == int(r2))
    model.Add(z1 + z2 + z3 == int(r3))
    model.Add(x1 + y1 + z1 == int(c1))
    model.Add(x2 + y2 + z2 == int(c2))
    model.Add(x3 + y3 + z3 == int(c3))

    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

#writes outputs to the txt file
    orig_stdout = sys.stdout
    f = open('kakuro_output.txt', 'w')
    sys.stdout = f
    if status == cp_model.FEASIBLE:
        print("x", ",", c1, ",", c2, ",", c3)
        print(r1, ",", solver.Value(x1), ",", solver.Value(x2), ",", solver.Value(x3))
        print(r2, ",",  solver.Value(y1), ",", solver.Value(y2), ",", solver.Value(y3))
        print(r3, ",", solver.Value(z1), ",", solver.Value(z2), ",", solver.Value(z3))
    sys.stdout = orig_stdout
    f.close()
kakuro_solver()