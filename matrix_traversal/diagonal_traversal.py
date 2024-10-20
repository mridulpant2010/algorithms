from typing import *
from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        # store the scoring inside the dictionary
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[i + j].append(mat[i][j])
        
        n = len(mat)
        m = len(mat[0])
        for i in range(n*m):
            value = d[i]
            if i%2!=0:
                for e in value:
                    print(e,end=' ')
            else:
                for e in range(len(value)-1,-1,-1):
                    print(value[e],end=' ')
                    
if __name__ == '__main__':
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    s.findDiagonalOrder(mat)
    
        