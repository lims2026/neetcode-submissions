class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 2:
            return [0,1]
        
        

        res = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in res:
                return [res[diff], i]
            res[n] = i
            

        
        
        

        

    











        