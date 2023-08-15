#  1. Дано предложение. Удалить все повторяющиеся слова.
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# someString = input('Введите предложение: ').strip()
# for i in someString:
#     if i.isspace():
#         continue
#     elif not i.isalpha():
#         someString = someString.replace(i, '')
# someString = someString.split()
# removingString = []
# for i in someString:
#     if someString.count(i) > 1:
#         removingString.append(i)
#         someString.remove(i)
# print(' '.join(someString))
# print(" ".join(removingString))
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  2. Написать программу с двумя действиями записи в файл и чтения из файла.
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import os
#
# while True:
#     print('1. Добавить запись в файл')
#     print('2. Вывести содержимое файла')
#     print('0. Выход')
#
#     choice = input('Выберите действие: ')
#     if choice == '1':
#         with open('file.txt', 'a') as file:
#             file.writelines(input('Введите строку: ') + '\n')
#     elif choice == '2':
#         with open('file.txt', 'r') as file:
#             someText = file.readlines()
#             someText = [text.rstrip("\n") for text in someText]
#             for text in someText:
#                 print(text)
#     elif choice == '0':
#         break
#     else:
#         print('Неверный ввод')
#
#     os.system('pause')
#     os.system('cls')
# print('Программа завершена')
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
