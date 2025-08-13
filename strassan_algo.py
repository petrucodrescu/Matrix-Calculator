from matrix_class import Matrix

def split(m: Matrix) -> tuple[Matrix, Matrix, Matrix, Matrix]:
    """
    NOTE: Same conditions as the function algo.
    """
    dim = m.n//2
    m1 = Matrix(dim) #top left
    for i in range(dim):
        m1.add_column(m.matrix[i][:dim])

    m2 = Matrix(dim) #bottom left
    for i in range(dim):
        m2.add_column(m.matrix[i][dim:])

    m3 = Matrix(dim) #top right
    for i in range(dim, m.n):
        m3.add_column(m.matrix[i][:dim])

    m4 = Matrix(dim) #bottom right
    for i in range(dim, m.n):
        m4.add_column(m.matrix[i][dim:])

    return m1, m2, m3, m4 #edit here

def join(top_left: Matrix, top_right: Matrix, bottom_left: Matrix, bottom_right: Matrix) -> Matrix:
    final_matrix = Matrix(top_left.n + top_right.n)
    for i in range(top_left.n):
        temp = top_left.matrix[i] + bottom_left.matrix[i]
        final_matrix.add_column(temp)
    for i in range(top_right.n):
        temp = top_right.matrix[i] + bottom_right.matrix[i]
        final_matrix.add_column(temp)
    return final_matrix

def algo(m1: Matrix, m2: Matrix) -> Matrix:
    """
    Precondition: Both m1 and m2 are of equal size (and square).
    NOTE: the dimension of m1 and m2 are always even.
    """
    if m1.n == 1:
        return m1*m2
    else:
        top_left1, bottom_left1, top_right1, bottom_right1 = split(m1)
        top_left2, bottom_left2, top_right2, bottom_right2 = split(m2)

        M1 = algo(top_left1 + bottom_right1, top_left2 + bottom_right2)
        M2 = algo(bottom_left1 + bottom_right1, top_left2)
        M3 = algo(top_left1, top_right2 - bottom_right2)
        M4 = algo(bottom_right1, bottom_left2 - top_left2)
        M5 = algo(top_left1 + top_right1, bottom_right2)
        M6 = algo(bottom_left1 - top_left1, top_left2 + top_right2)
        M7 = algo(top_right1 - bottom_right1, bottom_left2 + bottom_right2)

        top_left = M1 + M4 - M5 + M7
        top_right = M3 + M5
        bottom_left = M2 + M4
        bottom_right = M1 - M2 + M3 + M6

        final_matrix = join(top_left, top_right, bottom_left, bottom_right)
        return final_matrix