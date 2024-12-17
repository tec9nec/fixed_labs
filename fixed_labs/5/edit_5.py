#F(x<2) = 100; F(n) = (-1)n*(F(n-1)/n! + F(n//5) /(2n)!)

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

    F0 = 1
    F1 = 1
    Fn = 1
    minus = -1
    fact_n = 1
    fact_2n = 1 

    for i in range(2, n + 1):
        fact_n *= i
        fact_2n *= (2 * i - 1) * (2 * i)
        Fn = minus * (F1 / fact_n - F0 / fact_2n)

        F0, F1 = F1, Fn
        minus *= -1

    return Fn


print(f"{'n':<5} {'recursive time (s)':<20} {'iterative time (s)':<20} {'recursive result':<20} {'iterative result':<20}")

for n in range(2, 21):
    recursive_time = timeit.timeit(lambda: Fr(n), number=1)
    recursive_result = Fr(n)
    iterative_time = timeit.timeit(lambda: Fi(n), number=1)
    iterative_result = Fi(n)
    
    print(f"{n:<5} {recursive_time:<20.6f} {iterative_time:<20.6f} {recursive_result:<20} {iterative_result:<20}")
