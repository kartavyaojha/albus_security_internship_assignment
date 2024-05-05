def mult(a, b):
    res = [[0 for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                res[i][j] += a[i][k] * b[k][j]
    return res

A = [[5, 2, 3], [2, 5, 1], [6, 8, 9]]
B = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

product = mult(A, B)
for row in product:
    print(row)