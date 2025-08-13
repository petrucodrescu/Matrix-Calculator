from matrix_class import Matrix

def create(dim: int) -> Matrix:
    matrix1 = Matrix(dim)
    for i in range(dim):
        col = []
        for j in range(dim):
            col.append(int(input('Please input your values for the column: ')))
        matrix1.add_column(col)
    return matrix1