class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)
        valid = sorted([ch for ch in freq if freq[ch] >= k], reverse=True)
        
        def is_subseq(x):
            t = x * k
            i = 0
            for ch in s:
                if i < len(t) and ch == t[i]:
                    i += 1
            return i == len(t)
        
        queue = deque([""])
        res = ""
        
        while queue:
            curr = queue.popleft()
            for ch in valid:
                next_candidate = curr + ch
                if is_subseq(next_candidate):
                    if len(next_candidate) > len(res) or (len(next_candidate) == len(res) and next_candidate > res):
                        res = next_candidate
                    queue.append(next_candidate)
        
        return res