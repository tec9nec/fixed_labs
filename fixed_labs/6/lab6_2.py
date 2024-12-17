# Задание состоит из двух частей. 
# 1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
# 2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального  решения.

# Вариант 5. Предприятие может предоставить работу по одной специальности 4 женщинам, по другой - 6 мужчинам, по третьей - 3 работникам независимо от пола. 
# Сформировать все возможные варианты заполнения вакантных мест, если имеются 14 претендентов: 6 женщин и 8 мужчин.

import itertools
import timeit

women = 6
men = 8 
total = women + men

s1 = 4  # для первой специальности 4 женщины
s2 = 6  # для второй специальности 6 мужчин
s3 = 3  # для третьей специальности 3 работника (хотя бы 1 мужчина и 1 женщина)


def algorithm():
    result = []
    for women_group in itertools.combinations(range(women), s1):  # Выбираем 4 женщины
        for men_group in itertools.combinations(range(women, total), s2):  # Выбираем 6 мужчин
            remaining = set(range(total)) - set(women_group) - set(men_group)
            for third_group in itertools.combinations(remaining, s3):  # 3 человека на третью специальность
                # Ограничение: хотя бы 1 мужчина и 1 женщина в третьей группе
                third_women = len([x for x in third_group if x < women])
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

# Определим оптимальные решения
optimal_algo_solution, optimal_algo_workers = find_optimal(algo_result)
optimal_python_solution, optimal_python_workers = find_optimal(python_result)

# Вывод результатов:
print(f"Оптимизированных вариантов (алгоритмический способ): {len(algo_result)}")
print(f"Время (алгоритмический способ): {end_time_algo_opt - start_time_algo_opt:.6f} секунд")
print(f"Оптимальное решение (алгоритмический способ): {optimal_algo_solution}")
print(f"Общее количество работников в оптимальном решении: {optimal_algo_workers}")

print(f"\nОптимизированных вариантов (функции Python): {len(python_result)}")
print(f"Время (функции Python): {end_time_func_opt - start_time_func_opt:.6f} секунд")
print(f"Оптимальное решение (функции Python): {optimal_python_solution}")
print(f"Общее количество работников в оптимальном решении: {optimal_python_workers}")

# Вывод всех возможных вариантов
print("\nВсе возможные варианты (алгоритмический способ):")
for i, variant in enumerate(algo_result[:50], 1):
    print(f"{i}. Спец1: {variant[0]}, Спец2: {variant[1]}, Спец3: {variant[2]}")

print("\nВсе возможные варианты (функции Python):")
for i, variant in enumerate(python_result[:50], 1):
    print(f"{i}. Спец1: {variant[0]}, Спец2: {variant[1]}, Спец3: {variant[2]}")


