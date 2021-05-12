import heapq
def klargest(arr,k):
    he=[]
    heapq.heapify(he)
    for i in range(len(arr)):
        heapq.heappush(he,arr[i])
        #print(i, " iteration and heap arr is ",he)
        if len(he)>k:
            heapq.heappop(he)
    return heapq.heappop(he)


if __name__ == '__main__':
    arr=[3, 1, 5, 12, 2, 11]
    an =klargest(arr,3)
    print(an)
    
'''
TC: O(N*logk)
SC: O(logk)
'''