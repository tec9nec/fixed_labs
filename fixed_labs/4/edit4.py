# Написать программу, которая читая символы из файла, распознает, преобразует и выводит на экран объекты по определенному правилу. 
# Объекты разделены пробелами. Распознавание и преобразование делать по возможности через регулярные выражения. Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.

# Вариант 5.
# Четные целые числа, не превышающие 5 цифр. Каждое число на нечетном месте выводить словами.

import re

file = '4.txt'

def words(number):
    """Функция для преобразования числа в слова"""
    words = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять',
        '-': 'минус'  
    }
    return ' '.join(words[digit] for digit in str(number))

def process_file(open_file):
    with open(open_file, 'r', encoding='utf-8') as file:
        content = file.read()
        matches = re.findall(r'(?<!\S)-?\d+(?!\S)', content)
        
        even_numbers = [] 
        for num in matches:
            num_int = int(num)
            if num_int % 2 == 0: 
                even_numbers.append(num_int)
        
        result = []
        for index, number in enumerate(even_numbers, start=1):
            if index % 2 != 0:  #нечетное
                result.append(words(number))
            else:  #четное
                result.append(str(number))
        
        print(' '.join(result))

process_file(file)
