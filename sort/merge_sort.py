# Merge sort
# it uses the divide and conquer method that divides the array into smaller sub-arrays
# and then merges them in a sorting order.
# O(n log n)
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # sorting the left & right sides
        mergeSort(left_half)
        mergeSort(right_half)

        # taking three pointers 1 for left, 1 for right, 1 for main arr pos
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        
        return arr


if __name__ == "__main__":
    print(mergeSort([11,2,5,72,9,11,88,99,121,70,66,44,0,-12,32]))