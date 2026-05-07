class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = []

        while (len(strs) > 0):
            found = [strs[0]]
            d1 = {}

            for c in strs[0]:
                if c in d1:
                    d1[c] += 1
                else:
                    d1[c] = 1

            for j in range (1, len(strs)):
                d2 = {}
                for c in strs[j]:
                    if c in d2:
                        d2[c] += 1
                    else:
                        d2[c] = 1
                if (d1 == d2):
                    found.append(strs[j])
            for x in found:
                strs.remove(x)
            
            arr.append(found)

        return arr
