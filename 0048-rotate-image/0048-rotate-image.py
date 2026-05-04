class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(mat)
        for i in range(n >> 1):
            for j in range(i, n - 1 - i):
                mat[i][j], mat[j][~i], mat[~i][~j], mat[~j][i] = \
                mat[~j][i], mat[i][j], mat[j][~i], mat[~i][~j]