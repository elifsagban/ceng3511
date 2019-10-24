from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from ortools.sat.python import cp_model
import re


def futoshiki_solver(file):


    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.
    num_vals = 5
    elements = []

    row_one = []
    row_two = []
    filehandle = open(file, 'r')
    while True:
        line = filehandle.readline()
        if not line:
            break
        row_one.append(re.sub(r"\s+", "", line.split(',')[0]))
        row_two.append(re.sub(r"\s+", "", line.split(',')[1]))
    filehandle.close()




    #a = model.NewIntVar(int(txt_others[0]), int(txt_others[0]), row_one[0])
    #b = model.NewIntVar(int(txt_others[0]), int(txt_others[0]), row_one[0])
    #print(model.Add(a > b))

    A1 = model.NewIntVar(1, num_vals - 1, "A1")
    A2 = model.NewIntVar(1, num_vals - 1, "A2")
    A3 = model.NewIntVar(1, num_vals - 1, "A3")
    A4 = model.NewIntVar(1, num_vals - 1, "A4")
    B1 = model.NewIntVar(1, num_vals - 1, "B1")
    B2 = model.NewIntVar(1, num_vals - 1, "B2")
    B3 = model.NewIntVar(1, num_vals - 1, "B3")
    B4 = model.NewIntVar(1, num_vals - 1, "B4")
    C1 = model.NewIntVar(1, num_vals - 1, "C1")
    C2 = model.NewIntVar(1, num_vals - 1, "C2")
    C3 = model.NewIntVar(1, num_vals - 1, "C3")
    C4 = model.NewIntVar(1, num_vals - 1, "C4")
    D1 = model.NewIntVar(1, num_vals - 1, "D1")
    D2 = model.NewIntVar(1, num_vals - 1, "D2")
    D3 = model.NewIntVar(1, num_vals - 1, "D3")
    D4 = model.NewIntVar(1, num_vals - 1, "D4")

    elements.append(A1)
    elements.append(A2)
    elements.append(A3)
    elements.append(A4)
    elements.append(B1)
    elements.append(B2)
    elements.append(B3)
    elements.append(B4)
    elements.append(C1)
    elements.append(C2)
    elements.append(C3)
    elements.append(C4)
    elements.append(D1)
    elements.append(D2)
    elements.append(D3)
    elements.append(D4)


    text_row_one = []
    text_row_two = []
    for e in range(len(elements)):
        for i in range(len(row_one)):
            if row_one[i] == elements[e].Name():
                if row_two[i].isdigit():
                    model.Add(elements[e] == int(row_two[i]))
                else:
                    text_row_one.append(elements[e])
            if row_two[i] == elements[e].Name():
                text_row_two.append(elements[e])

    for i in range(len(text_row_one)):
        model.Add(text_row_one[i] > text_row_two[i])


    # for i in range(len(txt_others)):
    #     if txt_others[i].isdigit():
    #
    #         row_one[i] = model.NewIntVar(int(txt_others[i]), int(txt_others[i]), row_one[i])
    #         elements.append(row_one[i])
    #




# converts each array values to a variable


    # before = []
    # after = []
    # filehandle = open(file, 'r')
    # while True:
    #     line = filehandle.readline()
    #     if not line:
    #         break
    #     before.append(re.sub(r"\s+", "", line.split(',')[0]))
    #     after.append(re.sub(r"\s+", "", line.split(',')[1]))
    #     if (re.sub(r"\s+", "", line.split(',')[1])).isdigit():
    #
    #         line.split(',')[0] = model.Add(re.sub(r"\s+", "", line.split(',')[0]) == int(re.sub(r"\s+", "", line.split(',')[1])))
    #         print("I am digit")
    #     else:
    #        model.Add(model.NewIntVar(1, num_vals - 1, re.sub(r"\s+", "", line.split(',')[0])) > model.NewIntVar(1, num_vals - 1, re.sub(r"\s+", "", line.split(',')[1])))
    model.AddAllDifferent([A1, A2, A3, A4])
    model.AddAllDifferent([B1, B2, B3, B4])
    model.AddAllDifferent([C1, C2, C3, C4])
    model.AddAllDifferent([D1, D2, D3, D4])
    model.AddAllDifferent([A1, B1, C1, D1])
    model.AddAllDifferent([A2, B2, C2, D2])
    model.AddAllDifferent([A3, B3, C3, D3])
    model.AddAllDifferent([A4, B4, C4, D4])
    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()


    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:
        print("A1 ", solver.Value(elements[0]), "A2 ", solver.Value(elements[1]), "A3 ",  solver.Value(elements[2]), "A4 ",  solver.Value(elements[3]))
        print("B1 ", solver.Value(elements[4]), "B2 ", solver.Value(elements[5]), "B3 ",  solver.Value(elements[6]), "B4 ",  solver.Value(elements[7]))
        print("C1 ", solver.Value(elements[8]), "C2 ", solver.Value(elements[9]), "C3 ",  solver.Value(elements[10]), "C4 ",  solver.Value(elements[11]))
        print("D1 ", solver.Value(elements[12]), "D2 ", solver.Value(elements[13]), "D3 ",  solver.Value(elements[14]), "D4 ",  solver.Value(elements[15]))


file = "C:\\Users\\bk\\Desktop\\ceng3511-1\\p2\\futoshiki_input.txt"

futoshiki_solver(file)

