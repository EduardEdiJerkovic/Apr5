from matrix import Matrix

if __name__ == '__main__':
    a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    x = Matrix.inverse(a)
    print(x)
