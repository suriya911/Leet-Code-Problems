class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows, cols =len(grid), len(grid[0])

        leftDiag = [[x for x in y] for y in grid]
        rightDiag = [[x for x in y] for y in grid]

        for i in range(rows):
            for j in range(cols):
                if i+1<rows and j-1>=0:
                    leftDiag[i+1][j-1]+=leftDiag[i][j]
                if i+1<rows and j+1<cols:
                    rightDiag[i+1][j+1]+=rightDiag[i][j]
        
        sums=[]
        for i in range(rows):
            for j in range(cols):
                maxLen=min((rows-i+1)//2,j+1,cols-j)
                for k in range(maxLen):
                    if k==0:
                        sums.append(grid[i][j])
                    else:
                        s1=leftDiag[i+k][j-k]-leftDiag[i][j]
                        s2=leftDiag[i+2*k][j]-leftDiag[i+k][j+k]
                        s3=rightDiag[i+k][j+k]-rightDiag[i][j]
                        s4=rightDiag[i+2*k][j]-rightDiag[i+k][j-k]
                        sums.append(s1+s2+s3+s4-grid[i+k*2][j]+grid[i][j])
        
        sums=set(sums)
        return heapq.nlargest(3,sums)
                        

                    