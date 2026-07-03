class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}

        for n,c in enumerate(numbers):
            if target-c in d:
                return [d[target-c] +1, n+1]
            d[c] = n