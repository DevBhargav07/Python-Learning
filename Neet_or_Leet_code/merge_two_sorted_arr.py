# sorting two lists when two lists are already sorted without using any sorting algo

def sort_lists(a, b):
    res, i , j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]: 
            res.append(a[i])
            i+=1
        else: 
            res.append(b[j])
            j+=1
    return res+a[i:]+b[j:]

print(sort_lists([1,3,6],[2,4,5,7]))
