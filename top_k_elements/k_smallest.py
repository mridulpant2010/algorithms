import heapq
def k_smallest(arr,k):
    he=[]
    heapq.heapify(he)
    for el in arr:
        heapq.heappush(he,-1*el)
        if len(he)>k:
            heapq.heappop(he)
    return -1*heapq.heappop(he)  

if __name__ == '__main__':
    arr=[5, 12, 11, -1, 12]
    k=3
    ans=k_smallest(arr,k)
    print(ans)