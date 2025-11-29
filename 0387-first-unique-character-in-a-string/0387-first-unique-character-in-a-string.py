from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = float("inf")

        for char in ascii_lowercase:
            first = s.find(char)
            last = s.rfind(char)

            if first!=-1 and first == last:
                result = min(result, first)

        return -1 if result == float("inf") else result