class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        c=0
        for i in columnTitle:
            c= c*26 + (ord(i)-64)
        return c