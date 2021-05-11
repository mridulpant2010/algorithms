import heapq
def print_d(func):
    def inner_func(*args, **kwargs):
        ans=func(*args, **kwargs)
        print(ans)
        return ans
    return inner_func


@print_d 
def connect_ropes(arr):
    he= []
    heapq.heapify(he)
    for i in range(len(arr)):
        heapq.heappush(he,arr[i])
    result=0
    while len(he)>1:
        an=heapq.heappop(he)
        an2=heapq.heappop(he)
        result+=an+an2
        heapq.heappush(he,an+an2)
    return result

if __name__ == '__main__':
    connect_ropes([1, 3, 11, 5])    
    connect_ropes([3, 4, 5, 6])
    connect_ropes([1, 3, 11, 5, 2])
    
    '''
    TC: O(nlogn)
    SC: O(n)
    '''