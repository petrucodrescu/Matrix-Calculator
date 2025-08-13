class Matrix:
    """Attributes"""
    """
    n: the dimension of the matrix (nxn)
    matrix: the multi-dimensional list that will form the matrix
    
    Example: The list [[1,2], [2,3]] would be the nxn matrix where
    pos 0,0 = 1, pos 0,1 = 2, pos 1,0 = 2, pos 1,1 = 3
    
    Preconditions:
    -len(matrix) == n
    
    Representation Invariants:
    -len(column) == n
    
    """
    n: int
    matrix: list[list]
    def __init__(self, dimension: int) -> None:
        """
        Initialize the matrix with dimension size and list.
        """
        self.matrix = []
        self.n = dimension

    def add_column(self, column: list[int]) -> None:
        """
        Add a column to the matrix.
        """
        self.matrix.append(column)

    def __add__(self, other: "Matrix") -> "Matrix":
        """
        Adds two matrices.
        """
        new = Matrix(self.n)
        for i in range(len(self.matrix)):
            temp = []
            for j in range(len(self.matrix[i])):
                temp.append(self.matrix[i][j] + other.matrix[i][j])
            new.add_column(temp)
        return new

    def __sub__(self, other: "Matrix") -> "Matrix":
        """
        Subtracts two matrices.
        """
        new = Matrix(self.n)
        for i in range(len(self.matrix)):
            temp = []
            for j in range(len(self.matrix[i])):
                temp.append(self.matrix[i][j] - other.matrix[i][j])
            new.add_column(temp)
        return new

    def __mul__(self, other: "Matrix") -> "Matrix":
        """
        Multiply two matrices.
        """
        new = Matrix(self.n)
        for j in range(self.n):
            temp = []
            for i in range(self.n):
                multi = 0
                for k in range(self.n):
                    multi += self.matrix[k][i] * other.matrix[j][k]
                temp.append(multi)
            new.add_column(temp)
        return new

    def __str__(self) -> str:
        """
        Prints the matrix as a string.
        """
        s = ''
        for row in range(self.n):
            row_str = ''
            for col in range(self.n):
                row_str += str(self.matrix[col][row]) + '\t'
            s += row_str.strip() + '\n'
        return s.strip()