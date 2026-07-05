class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        n = len(heights)
        step = 0

        for i in range(n):
            for j in range(i+1,n):
                a = (j-i) * min(heights[i],heights[j])
                area = max(area, a)

        return area

        