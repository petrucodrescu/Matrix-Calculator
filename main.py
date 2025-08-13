from matrix_class import Matrix
from menu import menu
from matrix_creator import create
from addition import addition
from multiplication import multiplication
from strassan_algo import algo

choice = menu()

if choice == 1:
    print('Welcome to Addition')
    print('-------------------')
    dim = int(input('Please input your nxn matrix dimension: '))

    print("Input for matrix 1:")
    matrix1 = create(dim)
    print("Input for matrix 2:")
    matrix2 = create(dim)

    matrix3 = addition(matrix1, matrix2)
    print('Here is your added matrix: ')
    print(matrix3)
    print('-' * dim)

    print('Thank you for using the Matrix Calculator V1!')

elif choice == 2:
    print('Welcome to Multiplication')
    print('-------------------')
    dim = int(input('Please input your nxn matrix dimension: '))

    print("Input for matrix 1:")
    matrix1 = create(dim)
    print("Input for matrix 2:")
    matrix2 = create(dim)

    matrix3 = multiplication(matrix1, matrix2)
    print('Here is your multiplication matrix: ')
    print(matrix3)
    print('-' * dim)
    print('Thank you for using the Matrix Calculator V1!')

elif choice == 3:
    print('Welcome to Strassen Algorithm')
    print('-----------------------------')
    dim = int(input('Please input your nxn matrix dimension: '))
    print("Input for matrix 1:")
    matrix1 = create(dim)
    print("Input for matrix 2:")
    matrix2 = create(dim)

    matrix3 = algo(matrix1, matrix2)
    print('Here is the matrix calculated using the Strassen Algorithm: ')
    print(matrix3)
    print('-' * dim)
    print('Thank you for using the Matrix Calculator V1!')