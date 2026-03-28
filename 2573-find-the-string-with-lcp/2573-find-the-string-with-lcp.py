class Solution:
    def compute(self, word, dp):
        n = len(word)
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word[i] == word[j]:
                    if i+1 < n and j+1 < n:
                        dp[i][j] = 1 + dp[i+1][j+1]
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = 0

    def findTheString(self, lcp):
        n = len(lcp)

        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        word = ['?'] * n
        c = ord('a')

        for i in range(n):
            if word[i] == '?':
                if c > ord('z'):
                    return ""
                word[i] = chr(c)
                for j in range(i+1, n):
                    if lcp[i][j] > 0:
                        word[j] = chr(c)
                c += 1

        dp = [[0]*n for _ in range(n)]
        self.compute(word, dp)

        if dp == lcp:
            return "".join(word)
        return ""