class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        cnt=len(arr1)
        for i in range(cnt):
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    cnt-=1
                    break
        return cnt