# 1-е ДЗ
# monday = int(input('Введите ваш расход на Понедельник: '))
# tuesday = int(input('Введите ваш расход на Вторник: '))
# wednesday = int(input('Введите ваш расход на Среда: '))
# thursday = int(input('Введите ваш расход на Четверг: '))
# friday = int(input('Введите ваш расход на Пятница: '))
# saturday = int(input('Введите ваш расход на Суббота: '))
# (sunday) = int(input('Введите ваш расход на Воскресенье: '))
# totalconsumption = monday + tuesday + wednesday + thursday + friday + saturday + sunday
# print(f'Ваш общий расход за эту неделю составляет: {totalconsumption}')
# average_consumption_per_day = totalconsumption / 7
# print(average_consumption_per_day)


# 2-е ДЗ


# 3-е ДЗ
# vowel = ['а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е', 'a', 'e', 'i', 'o', 'u', 'y']
# consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', "р",
#               'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
#               'r', 's', 't', 'v', 'w', 'x', 'z']
# while True:
#     vovels = 0
#     consonantss = 0
#     print('Введите слово, для выхода пропишите exit')
#     user_input = input('')
#     if user_input.lower() == 'exit'.lower():
#         print('Программа завершина')
#         break
#     else:
#         num1 = len(user_input)
#         for i in user_input.lower():
#             if i in consonants:
#                 consonantss += 1
#             elif i in vowel:
#                 vovels += 1
#         procenscont = consonantss / num1 * 100
#         procentvowels = vovels / num1 * 100
#         print(f'Количество согласых: {consonantss}\n'
#               f'Количество гласных: {vovels}\n'
#               f'Количество букв: {num1}\n'
#               f'согласные: {float(procenscont)}%\n'
#               f'гласные: {float(procentvowels)}%')


# 4-е ДЗ
# letters = []
# numbers = []
# data_turple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
# for i in data_turple:
#     if type(i) == str:
#         letters += i
#     else:
#         numbers.append(i)
# del numbers[0]
# letters.append(numbers.pop(0))
# numbers.insert(1, 2)
# numbers.sort()
# letters.reverse()
# letters[1] = letters[1].upper()
# letters[7] = letters[7].lower()
# numbers = [i * i for i in numbers]
# numbers = tuple(numbers)
# letters = tuple(letters)
#
# print(letters)
# print(numbers)

# 5-е ДЗ
# data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
# designations = []
# codes = []
# for i in data:
#     if i.isnumeric():
#         codes.append(i)
#     else:
#         designations.append(i)
# operators = {}
# i = 0
# while i < len(codes):
#     operators[designations[i]] = {codes[i]}
#     i += 1
# del operators['Katel']
# del operators['Fonex']
# operators['O!'].add('0700')
# operators["O!"].update({'0500'})
# operators.get('Megacom').add('0555')
# operators['Megacom'].update({'0555'})
# operators.get('Beeline').add('0222')
# operators['Beeline'].update({'0777'})
# for i, x in operators.items():
#     print(f'{i} - {x}')


# 6-е
# def multiply_numbers(*args):
#     result = 1
#     for num in args:
#         result *= num
#     return result
#
#
# result = multiply_numbers(2, 3, 4, 5)
# print(result)
#
#
# def is_palindrome(input_string):
#     input_string = input_string.replace(" ", "").lower()
#     return input_string == input_string[::-1]
#
#
# string = "racecar"
# result = is_palindrome(string)
# print(result)
#
#
# def calculator(num1, operator, num2):
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/':
#         if num2 == 0:
#             return "Деление на ноль недопустимо"
#         return num1 / num2
#     elif operator == '**':
#         return num1 ** num2
#     elif operator == '%':
#         return num1 % num2
#     else:
#         return "Неподдерживаемый оператор"
#
#
# result1 = calculator(2, '**', 3)
# result2 = calculator(5, '+', 9.6)
# result3 = calculator(20, '%', 3)
#
# print(result1)
# print(result2)
# print(result3)

# 7-е ДЗ
# 8-е ДЗ
