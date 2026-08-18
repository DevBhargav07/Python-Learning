#we will see the binary search 
#https://en.wikipedia.org/wiki/Binary_search
#we have to perform this on a sorted array/list
#if not sorted sort this
# import bisect
def sortList(mylist):
    return sorted(mylist)

# def BinarySearch(mylist, target,low, high, mid):
#     #we will try to use the recursive of the program here
#     if mid > len(mylist) -1:
#         return False, mid
#     if mylist[mid] == target:
#         return True, mid
#     elif mylist[mid] > target:
#         # mylist=mylist[:mid]
#         return BinarySearch(mylist, target, len(mylist) // 2 - 1) 
#     else:
#         # mylist=mylist[mid:]
#         return BinarySearch(mylist, target, len(mylist) // 2 + 1)
#     return False, ""

def BinarySearch(mylist, target, low, high):
    #slow one using recursion (4)
    if low > high:
        return -1
    # mid = (high + low) // 2
    # print(f'1: {mid}')

    mid = low + (high - low) //2
    # print(f'2: {mid2}')


    if mylist[mid] ==  target:
        return mid
    elif mylist[mid] > target:
        return BinarySearch(mylist, target, low, mid-1)
    else:
        return BinarySearch(mylist, target, mid+1, high)

def bisect_left(mylist, target, low=0, high=-1):
    if high < 0:
        high = len(mylist)
    while low < high:
        mid = low + (high - low) // 2
        if mylist[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

    

def Binary_search(mylist, target):
    #fastest one in binary search (1)
    if list(mylist) != sorted(mylist):
        raise ValueError("sorted_collection must be sorted in ascending order")
    index = bisect_left(mylist, target)
    if index != len(mylist) and mylist[index] == target:
        return index
    return -1

def binarysearch(mylist, target):
    if mylist != sorted(mylist):
        raise ValueError("List is not in sorted order")
    low,high = 0, len(mylist)
    while low < high:
        mid = low + (high - low) // 2
        if mylist[mid] == target:
            return mid
        elif mylist[mid] < target:
            low = mid + 1
        else:
            high = mid  # making mid - 1 applies that we will miss one last value
    return -1

if __name__ == "__main__":
    mylist = sortList([10, 2 ,1 ,3, 4, 6, 89, 11, 17])
    target = 19
    # print(mylist[len(mylist)//2])
    pos = BinarySearch(mylist, target, 0, len(mylist)-1)
    if pos != -1:
        print('{} found at {} position'.format(target, pos))
    else:
        print('{} not found'.format(target))
    print(Binary_search(mylist, target))
    print(binarysearch(mylist, target))
