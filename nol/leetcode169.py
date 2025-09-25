class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        curNum = nums[0]
        hash[nums[0]] = 1

        for i in range(1, len(nums)):
            n = nums[i]
            if n in hash:
                hash[n] += 1
            else:
                hash[curNum] -= 1
                if hash[curNum] == -1:
                    del hash[curNum]
                    curNum = n
                    hash[curNum] = 1
            print(hash)
        return curNum