#using brute-force we ll try to do
#first we will check any of the list number are divisible the target if yes we will add them in that many times in a list and append it to the returning list
from time import time
class Combination:
    def combination_sum(self, candidates, target):
        result = []
        if not candidates or not target:
            # print("Need a record")
            raise ValueError("Need a record")
        if any(v for v in candidates if v <= 0):
            # return False
            raise ValueError("Got a negative number")

        def backtracking(start, remaining, current):
            if remaining == 0:
                result.append(current.copy())
                return 
            
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                if remaining >= candidates[i] and candidates[i] not in current: #this is helping for the sum_of_subsets_solution where only unique values taking eventually there are the maxiumu ones or not we have to test
                    current.append(candidates[i])
                    backtracking(i, remaining - candidates[i], current)
                    current.pop()
        backtracking(0, target, [])
        return result
    

c = Combination()
start = time()
print(c.combination_sum([3, 34, 4, 12, 5, 2], 3))
print(f'completing time {time() - start}')


'''
if remaining < 0: return
[[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 3], [1, 1, 1, 5], [1, 1, 3, 3], [3, 5]]
completing time 3.719329833984375e-05


** Process exited - Return Code: 0 **
if remaining >= candidates[i]
[[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 3], [1, 1, 1, 5], [1, 1, 3, 3], [3, 5]]
completing time 5.125999450683594e-05


** Process exited - Return Code: 0 **

both-----
[[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 3], [1, 1, 1, 5], [1, 1, 3, 3], [3, 5]]
completing time 3.695487976074219e-05


** Process exited - Return Code: 0 **
'''
