class Solution:
    def dayOfYear(self, date: str) -> int:
        y,m,d=date.split('-')
        days_31 = [1,3,5,7,8,10,12]
        days_30 = [4,6,9,11]
        days = int(d)

        def get_days(month,year):
            s=0
            if month == 1:
                return 0
            for i in range(1,month):
                if i in days_31:
                    s+=31
                elif i in days_30:
                    s+=30
                elif i==2:
                    if year%4==0 and (year%100!=0 or year%400==0):
                        s+=29
                    else:
                        s+=28
            return s

        days += get_days(int(m),int(y))


        return days