# we will receivee a list and we are going to find whether
# there will be a unique value

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # collection = {}
        # for i in nums:
        #     collection[i] = collection.get(i, 0) + 1
        # single = [n for n,i in collection.items() if i == 1]
        # return single
        # but this approach will give you O(n) & O(n)

        res = 0
        for n in nums:
            res ^= n
        return res
        # if there is a single unique value then it is going to be that value
        # more than one don't use this. O(n) & O(1)
        # and every duplicate should be have a pair if no.of 2's are 3 then this will 
        # not work.
    
if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([4,1,2,1,2]))
