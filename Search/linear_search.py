#we will see the linear search
#https://en.wikipedia.org/wiki/Linear_search

def linearSearch(mylist, target):
    if not mylist or not target:
        raise ValueError("list and target should not be empty")
    
    for idx, ele in enumerate(mylist):
        if ele == target:
            return True, idx
    return False, ""

if __name__ == "__main__":
    target = 5
    found, idx = linearSearch([1,2,3,4,5], target)
    if found:
        print('{} found at {} position'.format(target, idx))
    else:
        print('{} not found'.format(target))
