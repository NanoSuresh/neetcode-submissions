import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = re.sub(r'[^A-Za-z0-9]','',s)
        return strs.lower() == strs[::-1].lower()