# Зчитуємо вхідні дані
digits = list(map(int, input().split()))

# Масив для зберігання цифр до першого нуля
before_zero = []

# Збираємо всі цифри до появи нуля
for digit in digits:
    if digit == 0:
        break
    before_zero.append(digit)

# Підрахунок кількості кожної цифри від 1 до 9
counts = [0] * 9
for d in before_zero:
    if 1 <= d <= 9:
        counts[d - 1] += 1

# Виводимо результати
print(*counts)
print(len(before_zero))
print(*sorted(before_zero))