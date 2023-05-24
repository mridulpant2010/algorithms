import heapq
def nearly_sorted(arr,n):
    he=[]
    for i in range(n):
        heapq.heappush(he,arr[i])
    
    sort_list = []
    for _ in range(n):
        sort_list.append(heapq.heappop(he))
    return sort_list


if __name__ == '__main__':
    arr = [6, 5, 3, 2, 8, 10, 9]
    n=7
    sorted_list = nearly_sorted(arr,n)
    print(sorted_list)
