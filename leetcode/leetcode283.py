class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] != 0:
                cur = i
                target = i - 1
                while target > -1:
                    if nums[target] != 0:
                        break
                    nums[cur], nums[target] = nums[target], nums[cur]
                    cur -= 1
                    target -= 1
        
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] != 0:
                found = False
                for j in range(i-1, -1, -1):
                    if nums[j] != 0:
                        found = True
                        nums[i], nums[j+1] = nums[j+1], nums[i]
                        break
                if not found:
                    nums[i], nums[0] = nums[0], nums[i]


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 앞에서 뒤로 가면서 숫자를 발견하면
        for i in range(len(nums)):
            # 이전으로 향하면서 0을 찾아내어 스왑한다.
            if nums[i] != 0 and i > 0:
                for j in range(i-1, -1, -1):
                    if j == 0 and nums[j] == 0:
                        nums[i], nums[j] = nums[j], nums[i]
                    elif j == 0 and nums[j] != 0:
                        nums[i], nums[j+1] = nums[j+1], nums[i]
                    elif nums[j] != 0:
                        nums[i], nums[j+1] = nums[j+1], nums[i]
                        break              