def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        print(f"Iteración {i}: {arr}")
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print(f"Lista ordenada: {arr}")
    return arr

example_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(example_list.copy())
