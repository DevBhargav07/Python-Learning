#finding all the subsequence for a list of series 
'''
    [3, 2, 1]
    [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]
'''

def do_subsequence(seqlist, crnt_seqlist, index, rlist):

    if index == len(seqlist):
        # print(crnt_seqlist)
        rlist.append(crnt_seqlist.copy())
        return 
    do_subsequence(seqlist, crnt_seqlist, index+1, rlist)
    crnt_seqlist.append(seqlist[index])
    do_subsequence(seqlist, crnt_seqlist, index+1, rlist)
    crnt_seqlist.pop()
    # print(crnt_seqlist)
rlist = []
do_subsequence([3,2,1], [], 0, rlist)
print(rlist)




def do_subsequences(pos, mylist, crnt_list, rlist):
    if not mylist:
        return [mylist]
    if pos == len(mylist):
        rlist.append(crnt_list.copy())
        return
    
    do_subsequences(pos+1, mylist, crnt_list, rlist)
    crnt_list.append(mylist[pos])
    do_subsequences(pos+1, mylist, crnt_list, rlist)
    crnt_list.pop()
    


rlist = []

do_subsequences(0, [3,2,1], [], rlist)

print(rlist)





