# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 14:42:26 2023

@author: 86319
"""
# 计算矩阵的转置
def transpose(A):
    rows, cols = len(A), len(A[0])
    return [[A[i][j] for i in range(rows)] for j in range(cols)]

# 计算矩阵的乘法
def matrix_multiply(A, B):
    A_rows, A_cols = len(A), len(A[0])
    B_rows, B_cols = len(B), len(B[0])
    assert A_cols == B_rows, "矩阵维度不匹配"
    
    C = [[0] * B_cols for i in range(A_rows)]
    for i in range(A_rows):
        for j in range(B_cols):
            for k in range(A_cols):
                C[i][j] += A[i][k] * B[k][j]
    return C

# 计算矩阵的逆
def matrix_inverse(A):
    assert len(A) == len(A[0]), "矩阵必须是方阵"
    n = len(A)
    
    # 构造增广矩阵
    augmented = [row + [int(i == j) for j in range(n)] for i, row in enumerate(A)]
    
    # 高斯-约旦消元法
    for i in range(n):
        # 将主元素归一
        pivot = augmented[i][i]
        assert pivot != 0, "矩阵不可逆"
        augmented[i] = [x / pivot for x in augmented[i]]
        
        # 将列进行消元
        for j in range(n):
            if j != i:
                factor = augmented[j][i]
                augmented[j] = [augmented[j][k] - factor * augmented[i][k] for k in range(2 * n)]
    
    # 返回逆矩阵部分
    inverse = [row[n:] for row in augmented]
    return inverse

# 主程序
A = [[2, 3], [3, -5], [1, 2], [4, 2]]
b = [11, 3, 6, 14]

A_transpose = transpose(A)
A_transpose_A = matrix_multiply(A_transpose, A)
A_transpose_b = matrix_multiply(A_transpose, [[x] for x in b])

A_transpose_A_inverse = matrix_inverse(A_transpose_A)
x = matrix_multiply(A_transpose_A_inverse, A_transpose_b)

print("近似解为:", [x[0][0], x[1][0]])


