from functools import lru_cache
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m=len(grid)
        n=len(grid[0])
        if (m+n-1)%2!=0:
            return False
        @lru_cache(None)
        def dfs(i,j,balance):
            if i>=m or j>=n:
                return False

            if grid[i][j]=="(":
                balance+=1
            else:
                balance-=1
            if balance<0:
                return False
            if i==m-1 and j==n-1:
                return balance==0
            return dfs(i,j+1,balance) or dfs(i+1,j,balance)
        return dfs(0,0,0)

            
        