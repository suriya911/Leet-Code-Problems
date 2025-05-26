func largestPathValue(colors string, edges [][]int) int {
    adj := make([][]int, len(colors))
    indeg := make([]int, len(colors))
    for _, e := range edges {
        u, v := e[0], e[1]
        adj[u] = append(adj[u], v)
        indeg[v] += 1
    }
    stack := []int{}
    for u, d := range indeg {
        if d == 0 {
            stack = append(stack, u)
        }
    }
    dp := make([][26]int, len(colors))
    res := 0
    for len(stack) > 0 {
        u := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        dp[u][colors[u]-'a'] += 1
        res = max(res, dp[u][colors[u]-'a'])
        for _, v := range adj[u] {
            for c := range dp[u] {
                dp[v][c] = max(dp[v][c], dp[u][c])
            }
            if indeg[v] -= 1; indeg[v] == 0 {
                stack = append(stack, v)
            }
        }
    }
    for _, d := range indeg {
        if d != 0 {
            return -1
        }
    }
    return res
}