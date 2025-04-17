def insertion_sort_trace(arr):
    n = len(arr)
    already_sorted = True
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            already_sorted = False
        
        arr[j + 1] = key
        
        if not already_sorted:
            print(" ".join(map(str, arr)))
    
    if already_sorted:
        print("The array is already sorted")

# Зчитування вводу
n = int(input())
arr = list(map(int, input().split()))
insertion_sort_trace(arr)