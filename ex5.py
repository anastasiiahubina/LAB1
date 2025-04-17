n = int(input())
a = list(map(int, input().split()))
k = int(input())
positive = [x for x in a if x > 0]
positive.sort(reverse=True)
print(sum(positive[:k]))