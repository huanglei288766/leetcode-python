import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = collections.defaultdict(list)
        for cur in strs:
            group = ''.join(sorted(cur))
            if group in groups:
                groups[group].append(cur)
            else:
                groups[group] = [cur]
        return list(groups.values())
