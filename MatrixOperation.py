# Matrix Operation Code

class MatrixAll:
    def __init__(self):
        try:
            matrix1 = []
            self.row = int(input('Enter the Row Order Of Matrix:'))
            self.col = int(input('Enter the Column Order Of Matrix:'))
            print("\nEnter elements of matrix 1:")
            for i in range(self.row):
                v = []
                for j in range(self.col):
                    print(f"Element {i}, {j}", end=" ")
                    v.append(int(input()))
                matrix1.append(v)

            matrix2 = []
            self.row = int(input('Enter the Row Order Of Matrix:'))
            self.col = int(input('Enter the Column Order Of Matrix:'))
            print("\nEnter elements of matrix 1:")
            for i in range(self.row):
                v = []
                for j in range(self.col):
                    print(f"Element {i}, {j}", end=" ")
                    v.append(int(input()))
                matrix2.append(v)

            res = []
            for i1 in range(self.row):
                res1 = []
                for j in range(self.col):
                    res1.append(0)
                res.append(res1)

            while True:
                x = int(input("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Reset\n5.Exit\nEnter Your Choice? "))
                if x == 1:
                    Addition(matrix1, matrix2, res)
                elif x == 2:
                    Subtraction(matrix1, matrix2, res)
                elif x == 3:
                    Multiplication(matrix1, matrix2, res)
                elif x == 4:
                    print()
                    MatrixAll()
                elif x == 5:
                    break
                else:
                    print("Invalid Input")
        except Exception as er:
            print(er)
 

def Addition(mat1, mat2, res):
    for i in range(len(mat1)):
        for j in range(len(mat2)):
            res[i][j] = mat1[i][j] + mat2[i][j]
    print("\nResult!")
    for i in mat1:
        print(i)
    print()
    for i in mat2:
        print(i)
    print()
    for i in res:
        print(i)


def Subtraction(mat1, mat2, res):
    for i in range(len(mat1)):
        for j in range(len(mat2)):
            res[i][j] = mat1[i][j] - mat2[i][j]
    print("\nResult!")
    for i in mat1:
        print(i)
    print()
    for i in mat2:
        print(i)
    print()
    for i in res:
        print(i)


def Multiplication(mat1, mat2, res):
    for i in range(len(mat1)):
        for j in range(len(mat2)):
            for k in range(len(mat2)):
                res[i][j] += mat1[i][k] * mat2[k][j]
    print("\nResult!")
    for i in mat1:
        print(i)
    print()
    for i in mat2:
        print(i)
    print()
    for i in res:
        print(i)


obj = MatrixAll()
