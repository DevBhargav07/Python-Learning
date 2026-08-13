#we use this sorting method to sort the list of integers
# worst time complexity - O(n2)


def BubbleSort(mylist):
    n = len(mylist)

    for i in range(n):
        isSorted=True
        for j in range(n - i - 1):
            if mylist[j] >= mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
                isSorted = False
        if isSorted:
            break
    return mylist

if __name__ == "__main__":
    print(BubbleSort([11,2,5,72,9,11,88,99,121,70,66,44,0,-12,32]))
    print(min([1,2,3,4]))