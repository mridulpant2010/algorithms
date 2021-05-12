import heapq
from collections import defaultdict

def find_floor(arr,x):
    start=0
    ans=-1
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        first=arr[mid]
        if first==x:
            return mid
        elif first>x:
            end=mid-1
        else:
            ans=mid 
            start=mid+1
    return ans
    

def find_k_closest_numbers(arr,K,target):
    idx=find_floor(arr,target)
    
    low , high = idx-K, idx+K
    low = max(low,0)  #ideally low should not move away from 0
    high = min(high,len(arr)-1)
    #print(low,high,idx)
    d=defaultdict(int)
    he=[]
    heapq.heapify(he)
    for el in range(low,high+1):
        d[arr[el]]=abs(arr[el]-target)
    
    #creating a max_heap
    for k,v in d.items():
        heapq.heappush(he,(-v,k))
        if len(he)>K:
            heapq.heappop(he)
        #print(he)
    return [el[1] for el in he]

if __name__ == '__main__':
    arr=[5, 6, 7, 8, 9]
    arr2=[2, 4, 5, 6, 9]
    ans = find_k_closest_numbers(arr,3,7)
    ans2 = find_k_closest_numbers(arr2,3,6)
    ans3=find_k_closest_numbers([2, 4, 5, 6, 9], 3, 10)
    print(ans,ans2,ans3)