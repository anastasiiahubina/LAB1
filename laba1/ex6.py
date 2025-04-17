 from functools import cmp_to_key

# Функція порівняння
def custom_cmp(a, b):
    # Якщо a — парне, а b — непарне => a > b
    if a % 2 == 0 and b % 2 != 0:
        return 1
    # Якщо a — непарне, а b — парне => a < b
    elif a % 2 != 0 and b % 2 == 0:
        return -1
    # Обидва парні => зростання
    elif a % 2 == 0 and b % 2 == 0:
        return a - b
    # Обидва непарні => спадання
    else:
        return b - a

# Вхідні дані
n = int(input())
a = list(map(int, input().split()))

# Сортування за кастомним компаратором
a.sort(key=cmp_to_key(custom_cmp))

# Виведення результату
print(*a)