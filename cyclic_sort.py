# Cyclic sort
# time complexity of O(n)
# and this is only works for the definite range numbers see the input we are giving and
# output we are getting for the below two\

def cyclicSort(arr):
    i = 0
    while i < len(arr):
        j = arr[i] -1
        if 0 <= j < len(arr) and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    return arr

if __name__ == "__main__":
    print(cyclicSort([11,2,5,72,9,11,88,99,121,70,66,44,0,-12,32])) # we cant use this algorithm for random numbers sorting
    print(cyclicSort([3,5,4,2,1])) # this will work based on the number their index it is setting
    # print(min([1,2,3,4]))