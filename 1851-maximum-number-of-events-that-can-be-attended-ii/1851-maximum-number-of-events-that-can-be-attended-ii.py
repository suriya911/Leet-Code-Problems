class Solution:
    def maxValue(self, events, k):
        events.sort()
        n = len(events)
        next_idx = []
        for i in range(n):
            l, r = i+1, n
            while l < r:
                m = (l + r) // 2
                if events[m][0] > events[i][1]:
                    r = m
                else:
                    l = m + 1
            next_idx.append(l)

        prev = [0] * (n + 1)
        for _ in range(k):
            curr = [0] * (n + 1)
            for i in range(n - 1, -1, -1):
                curr[i] = max(curr[i + 1], events[i][2] + (prev[next_idx[i]] if next_idx[i] < n else 0))
            prev = curr

        return prev[0]