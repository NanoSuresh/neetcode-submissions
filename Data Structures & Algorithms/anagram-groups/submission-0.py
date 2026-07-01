from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in strs:
            keys = ''.join(sorted(i))
            groups[keys].append(i)
        return list(groups.values())