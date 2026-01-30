class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        n = len(source)
        str_to_id = {}
        curr_id = 0
        
        # Unique IDs for each string
        for s in original + changed:
            if s not in str_to_id:
                str_to_id[s] = curr_id
                curr_id += 1
        
        inf = float('inf')
        dist = [[inf] * curr_id for _ in range(curr_id)]
        for i in range(curr_id):
            dist[i][i] = 0
            
        for o, c, z in zip(original, changed, cost):
            u, v = str_to_id[o], str_to_id[c]
            dist[u][v] = min(dist[u][v], z)
            
        # Floyd-Warshall
        for k in range(curr_id):
            for i in range(curr_id):
                if dist[i][k] == inf: continue
                for j in range(curr_id):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        dp = [inf] * (n + 1)
        dp[0] = 0
        
        unique_lens = sorted(list(set(len(s) for s in original)))
        
        for i in range(n):
            if dp[i] == inf:
                continue
            
            # Case 1: Direct match
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            
            # Case 2: Substring transformations
            for length in unique_lens:
                if i + length > n:
                    break
                
                sub_s = source[i:i+length]
                sub_t = target[i:i+length]
                
                if sub_s == sub_t:
                    dp[i+length] = min(dp[i+length], dp[i])
                elif sub_s in str_to_id and sub_t in str_to_id:
                    u, v = str_to_id[sub_s], str_to_id[sub_t]
                    if dist[u][v] != inf:
                        dp[i+length] = min(dp[i+length], dp[i] + dist[u][v])
                        
        return dp[n] if dp[n] != inf else -1