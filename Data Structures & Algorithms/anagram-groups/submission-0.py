class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = []

        size = len(strs)
        while (size > 0):
            found = [strs[0]]
            for j in range (1, size):
                if (self.isAnagram(strs[0],strs[j])):
                    found.append(strs[j])
            for x in found:
                print(x)
                strs.remove(x)
            
            size = len(strs)
            arr.append(found)

        return arr
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        for c in s:
            if c in d1:
                d1[c] += 1
            else:
                d1[c] = 1

        for c in t:
            if c in d2:
                d2[c] += 1
            else:
                d2[c] = 1

        if len(d1.keys()) != len(d2.keys()):
            return False

        return d1 == d2