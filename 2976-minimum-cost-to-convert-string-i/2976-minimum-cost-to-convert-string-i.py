class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        import heapq

        if len(source) != len(target):
            return -1

        adj = [[] for _ in range(26)]
        for o, c, w in zip(original, changed, cost):
            adj[ord(o) - 97].append((ord(c) - 97, w))

        INF = 10**18
        dist = [[INF] * 26 for _ in range(26)]

        def dijkstra(src):
            pq = [(0, src)]
            dist[src][src] = 0
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[src][u]:
                    continue
                for v, w in adj[u]:
                    if dist[src][v] > d + w:
                        dist[src][v] = d + w
                        heapq.heappush(pq, (dist[src][v], v))

        for i in range(26):
            dijkstra(i)

        ans = 0
        for s, t in zip(source, target):
            u, v = ord(s) - 97, ord(t) - 97
            if u == v:
                continue
            if dist[u][v] == INF:
                return -1
            ans += dist[u][v]

        return ans