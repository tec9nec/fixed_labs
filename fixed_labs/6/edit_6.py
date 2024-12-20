#1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона),
# сравнив по времени их выполнение.

#2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов...
#...(которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального  решения.

#Вариант 5. Предприятие может предоставить работу по одной специальности 4 женщинам, по другой - 6 мужчинам, по третьей - 3 работникам независимо от пола. 
#Сформировать все возможные варианты заполнения вакантных мест, если имеются 14 претендентов: 6 женщин и 8 мужчин.

import itertools
import timeit

women = 6
men = 8
total = women + men
#спец
specialty1 = 4  # для первой специальности 4 женщины
specialty2 = 6  # для второй специальности 6 мужчин
specialty3 = 3  # для третьей специальности 3 работников (независимо от пола)

def algorithm():
    comb = []
    # Перебираем 4 женщины для специальности 1
    for i in range(women):
        for j in range(i + 1, women):
            for k in range(j + 1, women):
                for l in range(k + 1, women):
                    spec1 = [i, j, k, l]  # спец1 = 4 женщины
                    remaining_women = [w for w in range(women) if w not in spec1]
                    # Перебираем 6 мужчин для специальности 2
                    for m in range(women, total):
                        for n in range(m + 1, total):
                            for o in range(n + 1, total):
                                for p in range(o + 1, total):
                                    for q in range(p + 1, total):
                                        for r in range(q + 1, total):
                                            spec2 = [m, n, o, p, q, r]  #спец2 = 6 мужчин
                                            remaining_men = [man for man in range(women, total) if man not in spec2]
                                            # оставшиеся сотрудники для спец3
                                            remaining_people = remaining_women + remaining_men
                                            for x in range(len(remaining_people)):
                                                for y in range(x + 1, len(remaining_people)):
                                                    for z in range(y + 1, len(remaining_people)):
                                                        spec3 = [remaining_people[x], remaining_people[y], remaining_people[z]]  #спец3 = 3 работника
                                                        comb.append((spec1, spec2, spec3))

    return comb


#test
#result = algorithmic_approach()
#print(f"Всего комбинаций: {len(result)}")
#for idx, combo in enumerate(result[:10], 1):
#    print(f"{idx}. spec1: {combo[0]}, spec2: {combo[1]}, spec3: {combo[2]}")



# Способ с использованием встроенных функций Python
def pythonFunc():
    import itertools
    all_people = range(total)
    result = []
    # подбор 4 женщин
    for women_group in itertools.combinations(range(women), specialty1):
        # подбор 6 мужчин
        for men_group in itertools.combinations(range(women, total), specialty2):
            # подбор 3 любых из оставшихся
            remaining = set(all_people) - set(women_group) - set(men_group)
            for third_group in itertools.combinations(remaining, specialty3):
                result.append((women_group, men_group, third_group))
    return result


#time
start_time_algo = timeit.default_timer()
algorithm_result = algorithm()
end_time_algo = timeit.default_timer()

start_time_func = timeit.default_timer()
python_result = pythonFunc()
end_time_func = timeit.default_timer()

print(f"Всего вариантов (algorithm_manual): {len(algorithm_result)}")
print(f"time (algorithm_manual): {end_time_algo - start_time_algo:.6f} секунд")
print(f"\nВсего вариантов (PythonFunc): {len(python_result)}")
print(f"time (PythonFunc): {end_time_func - start_time_func:.6f} секунд")

print("\варианты заполнения (алгоритмический):")
for i, variant in enumerate(algorithm_result, 1):
    print(f"{i}. Спец1: {variant[0]}, Спец2: {variant[1]}, Спец3: {variant[2]}")

print("\nварианты заполнения (функции питон):")
for i, variant in enumerate(python_result, 1):
    print(f"{i}. Спец1: {variant[0]}, Спец2: {variant[1]}, Спец3: {variant[2]}")
