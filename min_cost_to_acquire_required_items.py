class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        commn=min(need1,need2)
        a=commn*min(costBoth,cost1+cost2)
        rem1=need1-commn
        rem2=need2-commn
        a+=rem1*min(cost1,costBoth)
        a+=rem2*min(cost2,costBoth)
        return a