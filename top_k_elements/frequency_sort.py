import heapq
from collections import defaultdict

def print_d(func):
    def inner_func(*args, **kwargs):
        ans=func(*args, **kwargs)
        print(ans)
        return ans
    return inner_func

@print_d
def sort_character_by_frequency(arr):
    he=[]
    heapq.heapify(he)
    d=defaultdict(int)
    for el in arr:
        d[el]+=1
    
    for k,v in d.items():
        heapq.heappush(he,(-1*v,k))
    
    sortedString=[]
    while he:
        freq,char=heapq.heappop(he)
        for _ in range(-freq):
            sortedString.append(char)
    return ''.join(sortedString)

if __name__ == '__main__':
    sort_character_by_frequency("Programming")
    sort_character_by_frequency("abcbab")