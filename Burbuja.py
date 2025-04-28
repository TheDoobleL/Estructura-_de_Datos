def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print(f"Iteración {i+1}: {arr}")
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(f"Lista ordenada: {arr}")
    return arr

example_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(example_list.copy())
 
