class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            word = ''.join(sorted(s))

            if word in d:
                d[word].append(s)
            else:
                d[word] = [s]

        arr = []

        for key in d:
            arr.append(d[key])

        return arr
    
