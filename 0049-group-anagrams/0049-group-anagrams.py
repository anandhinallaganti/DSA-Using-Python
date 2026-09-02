class Solution(object):
    def groupAnagrams(self, strs):
        a = {}

        for i in strs:
            s = "".join(sorted(i))
            if s in a:
                a[s].append(i)
            else:
                a[s] = [i]

        return list(a.values())