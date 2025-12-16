fmax = lambda x, y: x if x > y else y

def merge(A, B):
    C = [-inf] * len(A)
    for i, a in enumerate(A):
        for j in range(len(A) - i):
            C[i + j] = fmax(C[i + j], a + B[j])
    return C

class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:

        adj = [[] for _ in range(n)]
        for u, v in hierarchy:
            u -= 1
            v -= 1
            adj[u].append(v)

        def dfs(u, p):
            # res0[b] : max profit for budget b with no discount
            # res1[b] : max profit for budget b with this node discounted
            dp0 = [0] * (budget + 1)
            dp1 = [0] * (budget + 1)
            for v in adj[u]:
                if v != p:
                    res0, res1 = dfs(v, u)
                    dp0, dp1 = merge(dp0, res0), merge(dp1, res1)

            ans0 = dp0[:]
            ans1 = dp0[:]

            cost = present[u]
            for b in range(cost, budget + 1):
                ans0[b] = fmax(ans0[b], dp1[b - cost] + future[u] - cost)

            cost >>= 1
            for b in range(cost, budget + 1):
                ans1[b] = fmax(ans1[b], dp1[b - cost] + future[u] - cost)

            return ans0, ans1

        return max(dfs(0, -1)[0])