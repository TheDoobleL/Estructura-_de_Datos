def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Iteración {i+1}: {arr}")
    print(f"Lista ordenada: {arr}")
    return arr

example_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(example_list.copy())
