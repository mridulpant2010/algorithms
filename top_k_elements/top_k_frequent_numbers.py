from collections import defaultdict
import heapq

def print_d(func):
    def inner_func(*args, **kwargs):
        ans=func(*args, **kwargs)
        print(ans)
        return ans
    return inner_func

@print_d
def top_k_frequent_numbers(arr,K):
    he=[]
    heapq.heapify(he)
    d=defaultdict(int)
    for el in arr:
        d[el]+=1
    
    for k,v in d.items():
        heapq.heappush(he,(v,k))
        if len(he)>K:
            heapq.heappop(he)
    return he

if __name__ == '__main__':
    top_k_frequen t_numbers([1, 3, 5, 12, 11, 12, 11],K=2)
