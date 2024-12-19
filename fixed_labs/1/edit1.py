# С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N) заполняется случайным образом целыми числами в интервале [-10,10].
# Для тестирования использовать не случайное заполнение, а целенаправленное, введенное из файла. Условно матрица имеет вид:

# 5. Формируется матрица F следующим образом: Скопировать в нее матрицу А и если область 1 симметрична относительно медианы, то поменять области 2 и 4 местами, 1 и 2 поменять местами несимметрично.
# При этом матрица А не меняется. После чего вычисляется выражение: A*A^T–К*(AT+F). Выводятся по мере формирования А, F и все матричные операции последовательно.
import random

def print_mat(matrix, mat_name):
    print("Матрица " + mat_name)
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

k = int(input(("Введите K:")))
n = int(input(("Введите N:")))

a = [[0] * n for _ in range(n)]
f = [[0] * n for _ in range(n)]

print("Выбор ввода матрицы:\n1. рандом\n2. из файла\n3. генератором")
choice = int(input())
if choice == 1:
    for i in range(n):
        for j in range(n):
            a[i][j] = random.randint(-10, 10)
elif choice == 2:
    with open("11.txt", "r") as file:
        for i in range(n):
            row = list(map(int, file.readline().split()))
            a[i] = row
elif choice == 3:
    for i in range(n):
        for j in range(n):
            if i < j and j < n-1-i:
                a[i][j] = 1
            elif i < j and j > n-1-i:
                a[i][j] = 2
            elif i > j and j > n-1-i:
                a[i][j] = 3
            elif i > j and j < n-1-i:
                a[i][j] = 4
else:
    print("Неверный выбор!")
    exit()
    
print_mat(a, "A")



for i in range(n):
    for j in range(n):
        f[i][j] = a[i][j] # copy a in f


# проверка симметрии области 1
symmetrical = True
for i in range(n // 2):
    for j in range(i - 1):
        if a[i][j] != a[n - 1 - i][j]:
            symmetrical = False
            break

if symmetrical:
    for i in range(n // 2):
        for j in range(n // 2, n):
            f[i][j], f[n - 1 - i][j] = f[n - 1 - i][j], f[i][j] # область 2 - область 4

    for i in range(n // 2):
        for j in range(n // 2):
            f[i][j], f[i + n // 2][j] = f[i + n // 2][j], f[i][j] # область 1 - область 3
            
print_mat(f, "F")



#A * A^T - K * (A + F)
a_t = [[0] * n for _ in range(n)]
af_sum = [[0] * n for _ in range(n)]
result = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        a_t[i][j] = a[j][i] # transpon

a_at = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        a_at[i][j] = sum(a[i][t] * a_t[t][j] for t in range(n)) # a*a^t

for i in range(n):
    for j in range(n):
        af_sum[i][j] = a[i][j] + f[i][j] # a+f

k_af = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        k_af[i][j] = k * af_sum[i][j] # k*(a+F)

for i in range(n):
    for j in range(n):
        result[i][j] = a_at[i][j] - k_af[i][j]

print_mat(a_at, "A * A^T")
print_mat(af_sum, "A + F")
print_mat(k_af, "K * (A + F)")
print_mat(result, "результат")
