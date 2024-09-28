class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row=[[1]]
        for i in range(1,numRows):
            col=[]
            for j in range(0,i+1):
                if j==0 or j==i:
                    col.append(1)
                else:
                    col.append(row[i-1][j]+row[i-1][j-1])
            row.append(col)
        return row