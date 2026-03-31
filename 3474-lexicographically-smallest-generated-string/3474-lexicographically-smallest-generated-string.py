class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        word = ['?'] * (n + m - 1)
        locked = [False] * (n + m - 1)

        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if word[i+j] == '?' or word[i+j] == str2[j]:
                        word[i+j] = str2[j]
                        locked[i+j] = True
                    else:
                        return ""

        for i in range(len(word)):
            if word[i] == '?':
                word[i] = 'a'

        for i in range(n):
            if str1[i] == 'F':
                match = True

                for j in range(m):
                    if word[i+j] != str2[j]:
                        match = False
                        break

                if match:
                    done = False

                    for j in range(m-1, -1, -1):
                        if not locked[i+j]:
                            for c in range(26):
                                ch = chr(ord('a') + c)
                                if ch != str2[j]:
                                    word[i+j] = ch
                                    done = True
                                    break
                        if done:
                            break

                    if not done:
                        return ""

        return "".join(word)      