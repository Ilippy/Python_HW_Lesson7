# Задача 36: На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N

# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран получившийся кортеж.

# Sample Input:
# house=дом car=машина men=человек tree=дерево
# Sample Output:
# ((house, дом), (car, машина), (men, человек), (tree, дерево))


def change_to_tuple(words: str):
    # return tuple(tuple(i.split("=")) for i in words.split())    # Это решение кажется даже проще
    return tuple(map(lambda x: tuple(x.split("=")), words.split()))

input_string = "house=дом car=машина men=человек tree=дерево"
print(change_to_tuple(input_string))