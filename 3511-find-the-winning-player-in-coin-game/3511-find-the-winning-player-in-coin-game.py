class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        turns = min(x,y//4)
        return "Alice" if turns%2 else "Bob"