def jigsaw_sort(arr):
    for i in range(1, len(arr)):
        element_to_insert = arr[i]
        j = i - 1
        while j >= 0 and element_to_insert < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = element_to_insert

if __name__ == "__main__":
    # Example usage:
    unsorted_array = [12, 11, 13, 5, 6]
    print("Unsorted array:", unsorted_array)
    
    jigsaw_sort(unsorted_array)
    
    print("Sorted array:", unsorted_array)
