n = int(input())
arr = list(map(int, input().split()))
even_sorted = sorted([x for x in arr if x % 2 == 0])
even_index = 0
result = []
for num in arr:
    if num % 2 == 0:
        result.append(even_sorted[even_index])
        even_index += 1
    else:
        result.append(num)
print(*result)