class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 2:
            return [0,1]
        
        

        res = {}

        for i, n in enumerate(nums):
            res[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in res and res[diff] != i:
                return [i, res[diff]]
        
        return []
            

        
        
        

        

    











        