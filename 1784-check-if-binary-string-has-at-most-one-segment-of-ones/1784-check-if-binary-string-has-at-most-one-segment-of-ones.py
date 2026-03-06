class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # if len(s)==1 and s[0]=='1':
        #     return True
        # if len(s)<=1 : 
        #     return False
        # for i in range(len(s)-1):
        #     print(s[i])
        #     if s[i]=='1' and s[i]==s[i+1]:
        #         return True
        # return False
        # flag=0
        # i=0
        # p=[1]
        # while i<len(s)-1:
        #     if flag==0 and s[i]=='1' and s[i]==s[i+1]:
        #         if flag==1:
        #             p.append(0)
        #         flag=0
        #     else:
        #         if flag==0:
        #             p.append(0)
        #         flag=1
        #     i+=1
        # if len(s)>1 and (s[-1]==s[-2] and s[-1]=='0') :
        #     p.append(0)
        # print(p)
        # return True if len(p)<=2 else False
        i, comp = 0, 0
        while i < len(s):
            print(f"i: {i}")
            if comp and s[i] == "1":
                return False
            if s[i] == "1":
                print(f"Hi, i = {i}")
                while (i+1 < len(s) and s[i+1] == "1"):
                    i+= 1
                comp = 1
            i+= 1
        return True
