class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        spidey = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in spidey:
                return[spidey[diff],i]
            spidey[n] = i