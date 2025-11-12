class Solution:
    def sumDistance(self, A: List[int], s: str, d: int) -> int:
        n = len(A)
        B = sorted(A[i] + (d if s[i] == 'R' else -d) for i in range(n))
        return sum((i + i + 1 - n) * a for i,a in enumerate(B)) % (10 ** 9 + 7)