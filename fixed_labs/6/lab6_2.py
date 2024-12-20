
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

s1 = 4
s2 = 6  # для второй специальности 6 мужчин
s3 = 3  # для третьей специальности 3 работника (хотя бы 1 мужчина и 1 женщина)


def algorithm():
    result = []
    #перебор 4 женщин для специальности1
    for i in range(women):
        for j in range(i + 1, women):
            for k in range(j + 1, women):
                for l in range(k + 1, women):
                    women_group = [i, j, k, l]
                    
                    #перебираем 6 мужчин для второй специальности2
                    for a in range(women, total):
                        for b in range(a + 1, total):
                            for c in range(b + 1, total):
                                for d in range(c + 1, total):
                                    for e in range(d + 1, total):
                                        for f in range(e + 1, total):
                                            men_group = [a, b, c, d, e, f]

                                            #остальные люди для специальности3
                                            remaining = [x for x in range(total) if x not in women_group and x not in men_group]
                                            
                                            #перебор 3 человек для специальности 3
                                            for x in range(len(remaining)):
                                                for y in range(x + 1, len(remaining)):
                                                    for z in range(y + 1, len(remaining)):
                                                        third_group = [remaining[x], remaining[y], remaining[z]]
                                                        
                                                        #ограничение: хотя бы 1 мужчина и 1 женщина в третьей группе
                                                        third_women = len([p for p in third_group if p < women])
                                                        third_men = len(third_group) - third_women
                                                        if third_women >= 1 and third_men >= 1:
                                                            result.append((women_group, men_group, third_group))
    return result

def pythonFunc():
    all_people = range(total)
    result = []
    for women_group in itertools.combinations(range(women), s1):
        for men_group in itertools.combinations(range(women, total), s2):
            remaining = set(all_people) - set(women_group) - set(men_group)
            for third_group in itertools.combinations(remaining, s3):
                third_women = len([x for x in third_group if x < women])
                third_men = len(third_group) - third_women
                if third_women >= 1 and third_men >= 1:
                    result.append((women_group, men_group, third_group))
    return result

def find_optimal(results):
    max_workers = 0
    optimal_solution = None

    for solution in results:
        total_workers = len(solution[0]) + len(solution[1]) + len(solution[2])  # всего занятых людей
        if total_workers > max_workers:
            max_workers = total_workers
            optimal_solution = solution

    return optimal_solution, max_workers


start_time_algo_opt = timeit.default_timer()
algo_result = algorithm() 
end_time_algo_opt = timeit.default_timer()

start_time_func_opt = timeit.default_timer()
python_result = pythonFunc()
end_time_func_opt = timeit.default_timer()

optimal_algo_solution, optimal_algo_workers = find_optimal(algo_result)
optimal_python_solution, optimal_python_workers = find_optimal(python_result)

print(f"всего вариантов (алгоритмический способ): {len(algo_result)}")
print(f"время (алгоритмический способ): {end_time_algo_opt - start_time_algo_opt:.6f} секунд")
print(f"Оптимальное решение (алгоритмический способ): {optimal_algo_solution}")
print(f"общее количество работников в оптимальном решении: {optimal_algo_workers}")

print(f"\nОвсего вариантов (функции Python): {len(python_result)}")
print(f"время (функции Python): {end_time_func_opt - start_time_func_opt:.6f} секунд")
print(f"оптимальное решение (функции Python): {optimal_python_solution}")
print(f"Общее количество работников в оптимальном решении: {optimal_python_workers}")

print("\nпервые 50 возможных вариантов (алгоритмический способ):")
for i, variant in enumerate(algo_result[:50], 1):
    print(f"{i}. Спец1: {variant[0]}, Спец2: {variant[1]}, Спец3: {variant[2]}")

print("\nпервые 50 возможных вариантов (функции Python):")
for i, variant in enumerate(python_result[:50], 1):
    print(f"{i}. Спец1: {variant[0]}, Спец2: {variant[1]}, Спец3: {variant[2]}")
