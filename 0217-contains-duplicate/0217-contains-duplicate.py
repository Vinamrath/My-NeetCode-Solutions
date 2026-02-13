class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        venom = set()
        for num in nums:
            if num in venom:
                return True
            else:
                venom.add(num)
        return False