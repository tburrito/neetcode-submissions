class Solution:

    def encode(self, strs: List[str]) -> str:

        if (len(strs) == 0):
            return ""

        arr = []
        for s in strs:
            length = len(s)
            if length == 0:
                arr.append("EMPTY_,_")
            else:
                sList = list(s)
                for i in range(length):
                    sList[i] = chr(ord(sList[i]) + 3)
                arr.append("".join(sList) + "_,_")

        encoded = "".join(arr)

        return encoded[:len(encoded)]

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        
        strs = s.split("_,_")[:-1]
        decoded = []

        for string in strs:
            if (string == "EMPTY"):
                decoded.append("")
            else:
                length = len(string)
                sList = list(string)
                for i in range(length):
                    sList[i] = chr(ord(sList[i]) - 3)
                decoded.append("".join(sList))

        return decoded            
