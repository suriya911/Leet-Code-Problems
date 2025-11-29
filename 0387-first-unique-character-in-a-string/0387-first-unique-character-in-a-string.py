class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}

        for c in s:
            freq[c] = 1+ freq.get(c,0)

        for i,c in enumerate(s):
            if freq[c] == 1:
                return i
        
        return -1