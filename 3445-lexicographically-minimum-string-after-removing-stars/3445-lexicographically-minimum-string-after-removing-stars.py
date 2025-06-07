class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)

        # Step 1: Track which characters are removed
        removed = [False] * n

        # Step 2: Track indices of each character a-z
        char_indices = [[] for _ in range(26)]

        # Step 3: Traverse string and process each character
        for i, c in enumerate(s):
            if c == '*':
                removed[i] = True

                # Step 3.1: Find smallest character to the left
                for j in range(26):
                    if char_indices[j]:
                        idx = char_indices[j].pop()
                        removed[idx] = True
                        break
            else:
                # Step 3.2: Add character index to tracking list
                char_indices[ord(c) - ord('a')].append(i)

        # Step 4: Build result string
        result = []
        for i in range(n):
            if not removed[i] and s[i] != '*':
                result.append(s[i])

        return ''.join(result)