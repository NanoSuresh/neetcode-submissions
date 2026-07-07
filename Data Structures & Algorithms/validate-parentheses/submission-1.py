class Solution:
    def isValid(self, s: str) -> bool:
        br_map = {'(':')', '[':']', '{':'}'}
        seen = []

        for i in s:
            if i in br_map:
                seen.append(br_map[i])
            else:
                if not seen or i != seen[-1]:
                    return False
                seen.pop()

        return len(seen) == 0