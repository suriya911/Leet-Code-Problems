class Solution:
    def dayOfYear(self, date: str) -> int:
        parts = date.split('-')
        year = int(parts[0])
        
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if year % 4 == 0 and year != 1900:
            days[2] = 29
        
        month = int(parts[1])
        date = int(parts[2])
        return sum(days[:month]) + date