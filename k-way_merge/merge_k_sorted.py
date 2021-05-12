import heapq 

def merge_k_sorted_arrays(arr_lst):
    he=[]
    sortedFinal=[]
    heapq.heapify(he)
    for i in range(len(arr_lst)):
        ele=arr_lst[i][0]
        heapq.heappush(he,(ele,(i,0)))
    #print(he)
    while len(he)>0:
        top,pos= heapq.heappop(he)
        x,y=pos
        sortedFinal.append(top)
        if y+1<len(arr_lst[x]):
            heapq.heappush(he,(arr_lst[x][y+1],(x,y+1)))
    return sortedFinal  

def prepare_arr(ar):
    b=[]
    a=[]
    c=0
    while c<len(ar):
        d=0
        a=[]
        while d<n:
            a.append(ar[c+d])
            d+=1
        b.append(a)
        c+=n
    return b      

if __name__ == '__main__':
    k,n=list(map(int,input().split()))
    arr= list(map(int,input().split()))
    ar= prepare_arr(arr)
    #print(ar)
    an= merge_k_sorted_arrays(ar)
    print(*an)