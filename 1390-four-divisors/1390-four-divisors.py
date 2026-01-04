class Solution:
    def sumFourDivisors(self, nums):
        total = 0
        for n in nums:
            cnt = 0
            s = 0
            root = int(n ** 0.5)
            for i in range(1, root + 1):
                if n % i == 0:
                    j = n // i
                    if i == j:
                        cnt += 1
                        s += i
                    else:
                        cnt += 2
                        s += i + j
                    if cnt > 4:
                        break
            if cnt == 4:
                total += s
        return total