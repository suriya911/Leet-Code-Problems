class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num=[]
        fact=1
        for i in range(1,n):
            fact = fact*i
            num.append(i)
        num.append(n)
        ans=''
        k-=1
        while(1):
            x = k//fact
            ans += str(num[x])
            num.pop(x)
            if len(num) == 0:
                break
            k%=fact
            fact//=len(num)            
        return ans
