# insertion sort will try to sort everything one at a time
# O(n2) - worst time complexity can't use for larger arrays

def insertion_sort(arr):
    for i in range(len(arr)-1):
        j = i + 1

        while (j > 0):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
            else:
                break
    return arr

if __name__ == "__main__":
    print(insertion_sort([11,2,5,72,9,11,88,99,121,70,66,44,0,-12,32]))
    # print(min([1,2,3,4]))