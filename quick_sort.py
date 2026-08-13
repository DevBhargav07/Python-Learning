"""
    Quick Sort:
        Uses the Divide and Conqueror Rule.

        BEST: O(log n)
        AVERAGE: O(n log n) # random pivot
        WORST: O(n ** 2) # when the pivot itself is the maxi

        Space: O(n log n)

"""
# changing the same array and using swapping method
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)
    



# retunning a new array and using recursion method
def quickSort(list1):
    if len(list1) <= 1:
        return list1

    pivot = list1[len(list1) // 2]
    left = [x for x in list1 if x < pivot]
    middle = [x for x in list1 if x == pivot]
    right = [x for x in list1 if x > pivot]

    return quickSort(left)+ middle + quickSort(right)

arr = [1,3,523,9,64,5,23,1,25,2,351,24,131,2]
print(quickSort(arr))
print(arr)
quick_sort(arr, 0, len(arr)-1)
print(arr)