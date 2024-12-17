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

# специальности
specialty1 = 4  # для первой специальности 4 женщины
specialty2 = 6  # для второй специальности 6 мужчин
specialty3 = 3  # для третьей специальности 3 работника (независимо от пола)

def algorithm():
    result = []
    for women_group in itertools.combinations(range(women), specialty1):
        for men_group in itertools.combinations(range(women, total), specialty2):
            remaining = set(range(total)) - set(women_group) - set(men_group)
            for third_group in itertools.combinations(remaining, specialty3):
                result.append((women_group, men_group, third_group))
    return result

def pythonFunc():
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


# Вывод первых 10 вариантов для наглядности:
print("\nПервые 10 вариантов заполнения (алгоритмический способ):")
for i, variant in enumerate(algorithm_result[:10], 1):
    print(f"{i}. Спец1: {variant[0]}, Спец2: {variant[1]}, Спец3: {variant[2]}")

print("\nПервые 10 вариантов заполнения (функции Python):")
for i, variant in enumerate(python_result[:10], 1):
    print(f"{i}. Спец1: {variant[0]}, Спец2: {variant[1]}, Спец3: {variant[2]}")
