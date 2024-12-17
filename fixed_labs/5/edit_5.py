# 5.	F(x<2) = 100; F(n) = (-1)^n*(F(n-1)/n! + F(n//5) /(2n)!)
import timeit
import math

def Fr(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (-1)**n * (Fr(n - 1) / math.factorial(n) - Fr(n - 2) / math.factorial(2 * n))

def Fi(n):
    if n == 0 or n == 1:
        return 1
    F_0 = 1        # F(0)
    F_1 = 1        # F(1)
    factorial_n = 1       # n!
    factorial_2n = 1      # (2n)!
    minus = -1

    i = 2  # начало с n=2
    while i <= n:
        factorial_n *= i
        factorial_2n *= (2 * i - 1) * (2 * i)
        F_n = minus * (F_1 / factorial_n - F_0 / factorial_2n)

        F_0, F_1 = F_1, F_n
        minus *= -1
        i += 1  

    return F_n

print(f"{'n':<5} {'recursive time (s)':<20} {'iterative time (s)':<20} {'recursive result':<20} {'iterative result':<20}")

for n in range(2, 21):
    recursive_time = timeit.timeit(lambda: Fr(n), number=1)
    recursive_result = Fr(n)
    iterative_time = timeit.timeit(lambda: Fi(n), number=1)
    iterative_result = Fi(n)
    
    print(f"{n:<5} {recursive_time:<20.6f} {iterative_time:<20.6f} {recursive_result:<20} {iterative_result:<20}")
