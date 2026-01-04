class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def valid(x):
            a = list(str(x))
            for d in a:
                if d=='0' or x % int(d) > 0:
                    return False
            return True

        res=[]
        for i in range(left,right+1):
            print(i)
            if valid(i):
                res.append(i)
        return res
