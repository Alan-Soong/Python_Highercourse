import numpy as np
from numpy import random


def given_value(p):
    Fs = random.random(
        size=(p, p)
    )
    return Fs


channel_num = int(input("请输入通道数："))
numbers = int(input("请输入 feature map 的个数："))
fm_size = int(input("请输入 feature map 每个的大小："))
kernel_size = int(input("请输入 kernel 每个的大小："))

tmp = fm_size - kernel_size + 1

feature_maps = []
for index in range(numbers):
    feature_maps.append(given_value(fm_size))

kernels = []
for index in range(channel_num):
    kernels.append([])
    for index0 in range(numbers):
        kernels[index].append(given_value(kernel_size))

results = []
for index in range(channel_num):
    results.append([])
    for index0 in range(numbers):
        results[index].append(np.zeros((tmp, tmp)))

for i in range(channel_num):
    for j in range(numbers):
        F = feature_maps[j]
        G = kernels[i][j]
        R = results[i][j]
        for row in range(tmp):
            for col in range(tmp):
                R[row, col] = np.sum(F[row:row + kernel_size, col:col + kernel_size] * G)

for i in range(numbers):
    print('原矩阵', i + 1, '：\n', feature_maps[i])

for i in range(channel_num):
    R = sum(results[i])
    print('卷积', i + 1, '：\n', R)
