from typing import *
from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        ans =[]
        m=-1
        # store the scoring inside the dictionary
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                d[i + j].append(mat[i][j])
                m = max(m,i+j)
        for i in range(m+1):
            value = d[i]
            #if i%2!=0:
            for e in range(len(value)-1,-1,-1):
                ans.append(value[e])
        return ans
                    
if __name__ == '__main__':
    #nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
    nums = [[6],[8],[6,1,6,16]]
    s = Solution()
    ans = s.findDiagonalOrder(nums)
    print(ans)