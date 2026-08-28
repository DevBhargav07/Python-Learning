import time
# moving zeroes to end
def moveZeros(arr: list) -> list:
    # cnt_zero = 0
    # length = len(arr)
    # for i in arr:
    #     if i == 0:
    #         cnt_zero += 1
    
    # return [1] * (length - cnt_zero) + [0] * cnt_zero # O(n) - O(n)

    # or list comprehension
    # non_zeros = [x for x in arr if x != 0]
    # zero_count = arr.count(0)
    # return non_zeros + [0] * zero_count # O(n) - O(n)

    # using the two pointer appraoch
    left = 0
    for right in range(len(arr)):
        if arr[right] != 0:
            arr[left], arr[right] = arr[right],arr[left]
            left += 1
    return arr # O(n) - O(1)

start = time.perf_counter()
print(moveZeros([1,0,1,0,0,0,0,1,1,1,0]))
print(f'{time.perf_counter() - start}:.6f seconds')

"""
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
2.7701258659362793e-05:.6f seconds


** Process exited - Return Code: 0 **

[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
4.1163526475429535e-05:.6f seconds


** Process exited - Return Code: 0 **
"""
