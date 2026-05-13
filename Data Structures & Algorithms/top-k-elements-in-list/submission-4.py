class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCount = {}

        for x in nums:
            if (x in numsCount):
                numsCount[x] += 1
            else:
                numsCount[x] = 1

        print(numsCount)

        found = []

        while (len(found) < k):
            largest = -1

            for x in numsCount:
                if not largest in numsCount:
                    print("HI")
                    largest = x
                elif numsCount[x] > numsCount[largest]:
                    largest = x

            del numsCount[largest]
            found.append(largest)

        return found[:k]