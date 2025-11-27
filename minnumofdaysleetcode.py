class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if(k*m>len(bloomDay)):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        while(low<=high):
            mid=(low+high)//2
            NOF=0
            NOB=0
            for num in bloomDay:
                if(num<=mid):
                    NOF+=1
                    if(NOF==k):
                        NOB+=1
                        NOF=0
                else:
                    NOF=0
            if(NOB>=m):
                high=mid-1
            else:
                low=mid+1
        return low
