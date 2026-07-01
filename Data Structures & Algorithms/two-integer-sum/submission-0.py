class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for n,c in enumerate(nums):
            if target - c in d:
                return [d[target-c], n]
            d[c] = n