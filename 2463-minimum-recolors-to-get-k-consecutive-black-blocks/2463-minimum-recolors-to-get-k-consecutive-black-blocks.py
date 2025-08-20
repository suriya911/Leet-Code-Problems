class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n=len(blocks)
        recolor=w=blocks[:k].count('W')
        for l in range(n-k):
            w+=(blocks[l+k]=='W')-(blocks[l]=='W')
            recolor = min(recolor,w)
        return recolor