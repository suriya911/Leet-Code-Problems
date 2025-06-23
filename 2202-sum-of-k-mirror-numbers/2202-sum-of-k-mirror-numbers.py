class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def isPal(x):
            digs = []
            while x > 0:
                digs.append(x % k)
                x //= k
            return digs == digs[::-1]
    
        total, cnt, length = 0, 0, 1
        while cnt < n:
            half_len = (length + 1) // 2
            start = 10**(half_len - 1)
            end = 10**half_len
            for half in range(start, end):
                s = str(half)
                if length % 2 == 0:
                    pal_s = s + s[::-1]
                else:
                    pal_s = s + s[-2::-1]
                pal = int(pal_s)
                if isPal(pal):
                    total += pal
                    cnt += 1
                    if cnt == n:
                        return total
            length += 1
        return total