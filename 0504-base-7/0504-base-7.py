import numpy as np
class Solution:
    def convertToBase7(self, num: int) -> str:
        return '-'+np.base_repr(-num,7) if num<0 else np.base_repr(num,7)