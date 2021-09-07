test_arr = [1000, 1000000, 1, -15 , 33]

def mergeSort(arr):
    if len(arr) > 1:
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
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
