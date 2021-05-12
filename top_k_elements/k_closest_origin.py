
import heapq,math
from collections import defaultdict
def closest_dist(a,b):
    ans= math.sqrt(a*a+ b*b)
    return ans
def kClosest(arr,K):
    he=[]
    heapq.heapify(he)
    d=defaultdict(tuple)
    for el in arr:
        ans = closest_dist(el[0],el[1])
        d[(el[0],el[1])] = ans
    
    for k,v in d.items():
        heapq.heappush(he,(-1*v,k))
        if len(he)>K:
            heapq.heappop(he)
    return he[0][1]        
print(kClosest([[1,3],[-2,2]],1))