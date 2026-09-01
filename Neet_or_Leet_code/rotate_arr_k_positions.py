def rotate(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
k = 3
arr = [2,3,4,1,32,9,10]
k %= len(arr)
rotate(arr, 0, len(arr)-1)
rotate(arr, 0, k-1)
rotate(arr, k, len(arr)-1)
print(arr)
