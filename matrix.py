def matrix_multiplication(a, b):
    columns1 = len(a[0])
    rows1 = len(a)
    columns2 = len(b[0])
    rows2 = len(b)

    result_matrix = [[j for j in range(columns2)] for i in range(rows1)]
    if columns1 == rows2:
        for x in range(rows1):
            for y in range(columns2):
                sum = 0
                for k in range(columns1):
                    sum += a[x][k] * b[k][y]
                result_matrix[x][y] = sum
        return result_matrix
    else:
        print("Error (rows of matrix = columns of matrix)")
        return None
