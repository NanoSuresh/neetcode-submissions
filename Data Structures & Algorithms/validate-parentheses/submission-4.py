class Solution:
    def isValid(self, s: str) -> bool:
        br = {'{':'}', '(':')', '[':']'}
        seen = []

        for i in s:
            if i in br:
                seen.append(br[i])
            else:
                if not seen or i != seen[-1]:
                    return False
                seen.pop()

        return len(seen) == 0