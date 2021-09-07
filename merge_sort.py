test_arr = [1000, 1000000, 1, -15 , 33]

def merge_sort(arr):
    if len(arr) > 1:
         # Finding the mid of the array
        mid = len(arr)//2
        # Dividing the array elements
        left = arr[:mid]
        # into 2 halves
        right = arr[mid:]
        # Sorting the first half
        merge_sort(left)
        # Sorting the second half
        merge_sort(right)
 
        i = j = k = 0
        # Copy data to temp arrays left[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

def printList(arr):
    for i in range(len(arr)):
        if i == len(arr)-1:
             print(abs(arr[i]), end="")
        else:
            print(abs(arr[i]), end="---")
    print()

sorted_list = mergeSort(test_arr)

printList(sorted_list)
