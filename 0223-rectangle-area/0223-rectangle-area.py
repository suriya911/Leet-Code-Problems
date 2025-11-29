class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = abs(ax1-ax2)*abs(ay1-ay2) 
        area2 = abs(bx1-bx2)*abs(by1-by2)

        overlap_width = max(0,min(ax2,bx2) - max(ax1,bx1))
        overlap_height = max(0,min(ay2,by2) - max(ay1,by1))

        overlap_area = overlap_width * overlap_height
        total_area = area1 + area2 - overlap_area

        return total_area