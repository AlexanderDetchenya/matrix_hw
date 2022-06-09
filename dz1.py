m = 5
n = 5
A =[[5]*m for i in range(n)]
print(A)
import random
for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] = random.randint(1, 10)
print(A)

a = []
for i in range(len(A)):
    sum = 0
    for j in range(len(A[i])):
        sum += A[i][j]
    a.append(sum)
print(a)
print('Номер строки матрицы с максимальной суммой элементов: ', a.index(max(a))+1, 'Сумма равна: ', max(a))



