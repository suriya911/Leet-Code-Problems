class Solution:
    def robotWithString(self, s: str) -> str:
        s = collections.deque(s)
        t = []
        paper = []
        for c in sorted(set(s)):
            while t and t[-1] <= c:
                paper.append(t.pop())  # t -> paper
            while c in s:
                while s[0] != c:
                    t.append(s.popleft())  # s -> t
                paper.append(s.popleft())  # s -> t -> paper
        return "".join(paper)