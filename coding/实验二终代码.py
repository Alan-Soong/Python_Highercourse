def mini(a, b, list0):
    m = a
    for i in range(a + 1, b + 1):
        if list0[m] > list0[i]:
            m = i
    return m


n = int(input("Please enter the size of list: "))
list1 = [h]

for j in range(0, n):
    c = int(input())
    list1.append(c)

print(list1)

for i in range(0, n - 1):
    k = mini(i + 1, n - 1, list1)
    if list1[i] > list1[k]:
        list1[i], list1[k] = list1[k], list1[i]

print(list1, end="\r")
