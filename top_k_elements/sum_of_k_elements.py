import heapq

def find_sum_of_elements(arr,k1,k2):
    he=[]
    heapq.heapify(he)
    for el in arr:
        heapq.heappush(he,el)
    kk=k2-k1-1
    while k1!=0 :#and he:
        ans=heapq.heappop(he)
        k1-=1
    
    sum_final=0
    while kk!=0 :#and he:
        sum_final+=heapq.heappop(he)
        kk-=1
    return sum_final


if __name__ == "__main__":
    ans=find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)
    print(ans)