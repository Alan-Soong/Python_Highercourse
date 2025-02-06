import numpy as np
import random as rd
#两个库，实现生成二维数组和随机数的作用

class Matrix:

    #构造函数初始化
    def __init__(self, A):
        self.A = A

    #矩阵的加法
    def add(self, other):
        if len(self.A) != len(other.A) & len(other.A[0]) != len(self.A[0]):
            return None
        rA = [[0 for j in range(len(self.A[0]))] for i in range(len(self.A))]
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                rA[i][j] = self.A[i][j] + other.A[i][j]
        result = Matrix(rA)
        return result

    #矩阵的减法
    def sub(self, other):
        if len(self.A) != len(other.A) & len(other.A[0]) != len(self.A[0]):
            return None
        rA = [[0 for j in range(len(self.A[0]))] for i in range(len(self.A))]
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                rA[i][j] = self.A[i][j] - other.A[i][j]
        result = Matrix(rA)
        return result

    #矩阵的数乘
    def num_mul(self, p):
	    rA = [[0 for j in range(len(self.A[0]))] for i in range(len(self.A))]
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                rA[i][j] = self.A[i][j] * p
        result = Matrix(rA)
        return result
    
    #矩阵的乘法
    def mul(self, other3):
        if len(self.A[0]) != len(other3.A):
            return None
        rA = [[0 for j in range(len(other3.A[0]))] for i in range(len(self.A))]
        for i in range(len(self.A)):
            for j in range(len(other3.A[0])):
                for k in range(len(other3.A)):
                    rA[i][j] += self.A[i][k] * other3.A[k][j]
        result = Matrix(rA)
        return result

    #矩阵的哈德马乘法
    def hadamard(self, other):
        if len(self.A) != len(other.A) & len(other.A[0]) != len(self.A[0]):
            return None
        rA = [[0 for j in range(len(self.A[0]))] for i in range(len(self.A))]
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                rA[i][j] = self.A[i][j] * other.A[i][j]
        result = Matrix(rA)
        return result

    #矩阵转置
    def switch(self):
        rA = [[0 for j in range(len(self.A))] for i in range(len(self.A[0]))]
        for i in range(len(self.A[0])):
            for j in range(len(self.A)):
                rA[i][j] = self.A[j][i]
        result = Matrix(rA)
        return result

    #封装的矩阵打印函数
    def print_matrix(self):
        if self is None:
            print("Error!")
        else:
            for i in range(len(self.A)):
                for j in range(len(self.A[0])):
                    print('%.1f' % self.A[i][j], end="")
                    if j != len(self.A[0]) - 1:
                        print(end=" ")
                print(end="\n")
        print()

	#析构函数
    def __del__(self):
        print("Matrix is deleted!")

#主程序
if __name__ == '__main__':
    
    #定义两个矩阵
    A = Matrix(np.random.rand(4, 6))
    B = Matrix(np.random.rand(6, 4))
    Matrix.print_matrix(A)
    Matrix.print_matrix(B)

    #计算加法（减法同理）
    C = Matrix(np.random.rand(4, 6))
    add_re = A.add(C)
    Matrix.print_matrix(add_re)

    #计算乘法
    D = A.mul(B)
    Matrix.print_matrix(D)

    #计算哈德马乘法
    E = A.hadamard(C)
    Matrix.print_matrix(E)

    #计算矩阵转置
    F = A.switch()
    Matrix.print_matrix(F)
