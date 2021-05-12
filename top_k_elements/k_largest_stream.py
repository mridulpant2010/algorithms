import heapq


def print_d(func):
    def inner_func(*args, **kwargs):
        ans=func(*args, **kwargs)
        print(ans)
        return ans
    return inner_func


@print_d
def kthlargest_instream(arr,k):
    he=[]
    heapq.heapify(he)
    #arr.append(num)
    for el in arr:
        heapq.heappush(he,el)
        if len(he)>k:
            heapq.heappop(he)
    return he[0]

if __name__ == '__main__':
    arr=[3, 1, 5, 12, 2, 11]
    arr.append(6)
    kthlargest_instream(arr, 4)
    arr.append(13)
    kthlargest_instream(arr, 4)
    arr.append(4)
    kthlargest_instream(arr, 4)
