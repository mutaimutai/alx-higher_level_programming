#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    for row in matrix:
        for i in range(len(0,row)):
            if i < len(row) - 1:
                print("{:d} ".format(row[i]), end="")
            else:
                print("{}".format(row[i]))
