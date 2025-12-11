class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        minRowIndices = [n + 1] * (n + 1)
        maxRowIndices = [0] * (n + 1)
        minColIndices = [n + 1] * (n + 1)
        maxColIndices = [0] * (n + 1)

        for building in buildings:
            row = building[0]
            col = building[1]

            if row < minRowIndices[col]:
                minRowIndices[col] = row
            if row > maxRowIndices[col]:
                maxRowIndices[col] = row

            if col < minColIndices[row]:
                minColIndices[row] = col
            if col > maxColIndices[row]:
                maxColIndices[row] = col

        count = 0
        for building in buildings:
            row = building[0]
            col = building[1]

            if (minRowIndices[col] < row and
                maxRowIndices[col] > row and
                minColIndices[row] < col and
                maxColIndices[row] > col):
                count += 1

        return count