class Solution:
    def getProbability(self, balls: List[int]) -> float:
        nxt = lambda x,y: x | 1 << balls[y]

        @lru_cache(None)
        def dp(i,cnt0,box0,box1):
            cnt1 = i-cnt0
            if cnt0>sm//2 or cnt1>sm//2: 
                return 0

            if i==len(balls):
                return box0.bit_count() ==box1.bit_count()

            return (dp(i+1,cnt0+1,nxt(box0,i),box1)+
            dp(i+1,cnt0,box0,nxt(box1,i)))

        sm = sum(balls)
        balls = list(chain(*([i] * ball for i, ball in enumerate(balls))))

        return dp(0,0,0,0) / comb(sm,sm//2)