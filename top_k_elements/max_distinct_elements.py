'''
Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the
array such that we are left with maximum distinct numbers.
'''
from collections import defaultdict
import heapq

def find_maximum_distinct_elements(arr,K):
    he=[]
    ans=[]
    heapq.heapify(he)
    d=defaultdict(int)
    for el in arr:
        d[el]+=1
    
    for k,v in d.items():
        heapq.heappush(he,(-v,k))
    print(d,he)
    while K!=0:
        v,k = heapq.heappop(he)
        v=-1*v
        v=v-1
        v=-1*v
        heapq.heappush(he,(v,k))
        K-=1
    he=list(map(lambda x: (-1*x[0],x[1]),he))
    print(he)
    for el in he:
        if el[0]==1:
            ans.append(el[1])
    print(ans,len(ans))
    
if __name__ == '__main__':
    #arr= [7, 3, 5, 8, 5, 3, 3]
    #K=2
    #find_maximum_distinct_elements(arr,K)
    #find_maximum_distinct_elements(arr=[3,5,12,11,12],K=3)
    find_maximum_distinct_elements(arr=[1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5],K=2)
    
