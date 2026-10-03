class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for n in nums:
            hset.add(n)
        return len(nums) != len(hset)