# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:

        weights = [Counter(word[i] for word in words) for i in range(6)]

        words.sort(key = lambda word: sum(weights[i][c] for i,c in enumerate(word)))
        while words:
            word = words.pop()
            matches = master.guess(word)

            words = [
                i for i in words if matches == sum(w== o for w,o in zip(word,i))
            ]