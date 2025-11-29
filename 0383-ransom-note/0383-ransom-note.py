class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash={}

        for c in magazine:
            hash[c] = 1 + hash.get(c,0)
        
        for i in ransomNote:
            if i not in hash or hash[i]<=0:
                return False
            hash[i]-=1
        return True