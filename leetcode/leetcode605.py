class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = n
        if len(flowerbed) == 1:
            count -= 1 if flowerbed[0] == 0 else 0
            return True if count <= 0 else False

        idx = 1
        if flowerbed[idx-1] == 0 and flowerbed[idx] == 0:
            flowerbed[idx-1] = 1
            count -= 1

        while idx < len(flowerbed) - 1:
            if flowerbed[idx-1] == 0 and flowerbed[idx] == 0 and flowerbed[idx+1] == 0:
                flowerbed[idx] = 1
                count -= 1
                idx += 2
            else:
                idx += 1
        
        if flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0:
            count -= 1

        return True if count <= 0 else False