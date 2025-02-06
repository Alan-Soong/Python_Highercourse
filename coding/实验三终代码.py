#修正的martrix.py文件，可以执行判断，错误则返回Error

def multiply(A, B):
    
    #判断是否符合计算条件
    if (A is None) | (B is None): return None
    if len(A[0]) != len(B): return None
    C = [[0 for j in range(len(B[0]))] for i in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    return C


def Hadamard(A, B):
    
    #判断是否符合计算条件
    if (A is None) | (B is None): return None
    if len(A) == len(B) & len(A[0]) == len(B[0]):
        C = [[0 for j in range(len(B[0]))] for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                C[i][j] = A[i][j] * B[i][j]
        return C
    else:
        return None


def switch(A):
    
    #判断是否符合计算条件
    if A is None: return None
    C = [[0 for j in range(len(A))] for i in range(len(A[0]))]
    for i in range(len(A[0])):
        for j in range(len(A)):
            C[i][j] = A[j][i]

    return C


def add(A, B):
    
    #判断是否符合计算条件
    if (A is None) | (B is None): return None
    if len(A) != len(B) | len(A[0]) != len(B[0]): return None
    C = [[0 for j in range(len(A))] for i in range(len(A[0]))]
    for i in range(len(A[0])):
        for j in range(len(A)):
            C[i][j] = A[i][j] + B[i][j]

    return C


def minus(A, B):
    
    #判断是否符合计算条件
    if (A is None) | (B is None): return None
    if len(A) != len(B) | len(A[0]) != len(B[0]): return None
    C = [[0 for j in range(len(A))] for i in range(len(A[0]))]
    for i in range(len(A[0])):
        for j in range(len(A)):
            C[i][j] = A[i][j] - B[i][j]

    return C


def print_matrix(C):
    
    #判断是否符合计算条件
    if C is not None:
        for i in range(len(C)):
            for j in range(len(C[0])):
                print('%.1f' % C[i][j], end=' ')
            print()
    else:
        print('Error!')
    print()


import numpy as np
import martrix as mt
import random

#生成随机矩阵，随机大小，随机内容
nrA = random.randint(1, 5)
ncA = random.randint(1, 5)
A = np.random.rand(nrA,ncA)
nrB = random.randint(1, 5)
ncB = random.randint(1, 5)
B = np.random.rand(nrB,ncB)

#打印矩阵
mt.print_matrix(A)
mt.print_matrix(B)

C = mt.multiply(A, B)
mt.print_matrix(C)
D = mt.switch(C)
mt.print_matrix(D)

E = mt.Hadamard(A, mt.switch(B))
mt.print_matrix(E)

X = mt.add(C,D)
mt.print_matrix(X)

Y = mt.minus(C,D)
mt.print_matrix(Y)
