import heapq


def topKElements(arr,n,k):
    he =[]
    for i in range(n):
        heapq.heappush(he,arr[i])
        if len(he) > k:
            heapq.heappop(he)
    return he



if __name__ == '__main__':
    #arr = [12,5,787, 1,23]
    arr = [1,23,12,9,30,2,50]
    he = topKElements(arr,len(arr),3)
    print(he)