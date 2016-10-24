# -*- coding: utf-8 -*-


def create_matrix():
    rows = int(input("input number of rows: "))
    columns = input("input number of columns: ")
    print "input number to fill matrix"
    matrix = [[0] * columns for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = input()
    return matrix


def create_fake_matrix():
    return [[14, -3, 194], [-3, -4, 15], [24, -3, 4]]


def create_magic_matrix():
    return [[2, 7, 6], [9, 5, 1], [4, 3, 8]]


def create_complex_matrix():
    # return [[14, -3, [1, 2, [4, 6, 5]]], [-3, [-4, -9, [0, 9, 8, 3, 5, 33, 3], 3], 15], [24, -3, 4]] # not unique
    return [[14, -31, [1, 2, [4, 6, 509]]], [-332, [-4, -9, [0, 9, 8, 32, 5, 33, 36], 3], 15], [24, -3, 453]] # unique


def get_mean(matrix):
    sum_ = 0.00
    count = 0.00
    #why int/int ==int
    #why 0.00/0.00 == 0.00 not 0.0000

    for i in matrix:
        for j in i:
            if j < 0:
                sum_ += j
                count += 1
    return round(sum_/count, 2) if count > 0 else 0


def is_unique(matrix):

    new_matrix = []
    for i in matrix:
        new_matrix += i

    while new_matrix:
        el = new_matrix.pop()
        if el in new_matrix:
            return "elements are not unique"
    return "elements are unique"


def sum_of_row(matrix):
    for row in matrix:
        sum_ = 0
        for i in range(len(row)):
            if i == len(row) - 1:
                row[i] = sum_
            else:
                sum_ += row[i]
    return matrix


def is_magic(matrix):

    len_matrix = len(matrix)
    if len_matrix != len(matrix[0]):
        return "matrix is not magic (is not square)"

    magic_sum = sum(matrix[0])

    sum_d1 = 0
    sum_d2 = 0
    for i in range(len(matrix)):
        sum_row = 0
        sum_col = 0
        for j in range(len(matrix)):
            sum_col += matrix[j][i]
            sum_row += matrix[i][j]
        if sum_row != magic_sum or sum_col != magic_sum:
            return "matrix is not magic"
        sum_d1 += matrix[i][i]
        sum_d2 += matrix[len_matrix - i - 1][j]
    if sum_d1 != magic_sum or sum_d2 != magic_sum:
        return "matrix is not magix"
    return "matrix is magic"


def make_simple(matrix, simple_matrix):
    for i in matrix:
        if isinstance(i, list):
            make_simple(i, simple_matrix)
        else:
            simple_matrix.append(i)# += i
    return simple_matrix


def is_unique_general(matrix):

    simple_matrix = []
    make_simple(matrix, simple_matrix)

    while simple_matrix:
        el = simple_matrix.pop()
        if el in simple_matrix:
            return "elements are not unique"
    return "elements are unique"


if __name__ == '__main__':
    my_matrix = create_fake_matrix()
    # matrix = create_matrix()
    print "matrix:", my_matrix, "\n"

    # task1
    print "#1 mean of negatives:", get_mean(my_matrix)

    # task2
    print "#2", is_unique(my_matrix)

    # task3
    print "#3 last is sum:", sum_of_row(my_matrix)

    # task 4
    #my_matrix = create_magic_matrix()
    print "#4", is_magic(my_matrix)

    # task 5
    #my_matrix = create_complex_matrix()
    print "#5", is_unique_general(my_matrix)

