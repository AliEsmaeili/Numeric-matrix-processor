import math

menu = """1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit"
"""

transpose_menu = """1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line"""

error = "The operation cannot be performed."


def vector_scalar(scalar, vector):
    return [scalar * number for number in vector]


def vector_sum(*vectors):
    # return [sum(vector[i] for vector in vectors) for i in range(len(vectors[0]))]
    return [math.fsum(col) for col in zip(*vectors)]


def matrix_multiply(a, b):
    # return [vector_sum(*(vector_scalar(a[i][j], b[j]) for j in range(len(b)))) for i in range(len(a))]
    return [vector_sum(*(vector_scalar(col, row) for col, row in zip(a[i], b))) for i in range(len(a))]


def determinant(a):
    return a[0][0] if len(a) == 1 else sum(pow(-1, j) * a[0][j] * determinant([row[:j] + row[j + 1:] for row in a[1:]]) for j in range(len(a[0])))


def transpose(a):
    return [col for col in zip(*a)]


def cofactor(a):
    return [[pow(-1, i + j) * determinant([row[:j] + row[j+1:] for row in a[:i] + a[i+1:]]) for j in range(len(a))] for i in range(len(a))]


def inverse(a):
    det = determinant(a)
    if det:
        return [vector_scalar(1 / det, row) for row in transpose(cofactor(a))]


def vertical_transpose(a):
    return [row[::-1] for row in a[::]]


def horizontal_transpose(a):
    return a[::-1]


def side_transpose(a):
    # Alternatively a combination of transpose, horizontal, vertical where transpose is not in between
    return horizontal_transpose(transpose(horizontal_transpose(a)))


def output_matrix(a):
    print("The result is:")
    for row in a:
        print(*(format(value, "^ 23") for value in row))


def input_matrix(name=""):
    n = int(input(f"Enter the number of rows of {name}matrix:").split()[0])
    print("Enter matrix:")
    return [[float(number) for number in input().split()] for _ in range(n)]


def input_square_matrix():
    n = int(input("Enter matrix size:").split()[0])
    print("Enter matrix:")
    a = list(range(n))
    for i in range(n):
        row = [float(number) for number in input().split()]
        if len(row) != n:
            return 0
        a[i] = row
    return a


def scalar_multiplication():
    a = input_matrix()
    print("Enter constant:")
    c = float(input())
    output_matrix([vector_scalar(c, row) for row in a])


def matrix_addition():
    a = input_matrix("first ")
    if int(input("Enter the number of rows of second matrix:").split()[0]) != len(a):
        return 0
    print("Enter second matrix:")
    b = list(range(len(a)))
    for i in range(len(a)):
        b_row = input().split()
        if len(b_row) != len(a[i]):
            return 0
        b[i] = [float(number) for number in b_row]
    output_matrix([vector_sum(a[i], b[i]) for i in range(len(a))])


def matrix_multiplication():
    c = ["first", "second"]
    n = [0, 0]
    for j in range(2):
        n[j] = int(input(f"Enter the number of rows of {c[j]} matrix:").split()[0])
        if j > 0 and n[j] != len(c[0][0]):
            return 0
        print(f"Enter {c[j]} matrix:")
        c[j] = list(range(n[j]))
        c[j][0] = [float(number) for number in input().split()]
        for i in range(1, n[j]):
            c[j][i] = [float(number) for number in input().split()]
            if len(c[j][i]) != len(c[j][0]):
                return 0
    output_matrix([row for row in matrix_multiply(c[0], c[1])])


def matrix_transpose():
    print(transpose_menu)
    option = input()
    a = input_matrix()
    if option == "1":
        output_matrix(transpose(a))
    elif option == "2":
        output_matrix(side_transpose(a))
    elif option == "3":
        output_matrix(vertical_transpose(a))
    elif option == "4":
        output_matrix(horizontal_transpose(a))


def matrix_determinant():
    a = input_square_matrix()
    print("The result is:", determinant(a), sep="\n")


def matrix_inverse():
    a = input_square_matrix()
    a_inverse = inverse(a)
    if a_inverse:
        output_matrix(a_inverse)
    else:
        print("This matrix doesn't have an inverse.")


while True:
    print(menu)
    choice = input("Your choice:")
    if choice == "0":
        break
    if choice == "1":
        if matrix_addition() == 0:
            print(error)
    elif choice == "2":
        scalar_multiplication()
    elif choice == "3":
        if matrix_multiplication() == 0:
            print(error)
    elif choice == "4":
        matrix_transpose()
    elif choice == "5":
        if matrix_determinant() == 0:
            print(error)
    elif choice == "6":
        if matrix_inverse() == 0:
            print(error)
