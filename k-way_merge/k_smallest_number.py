import heapq

def find_k_closest_numbers(lis,k,n):
    he=[]
    #merged=[]
    heapq.heapify(he)
    for i in range(len(lis)):
        heapq.heappush(he,(lis[i][0],(i,0)))
    #print(he,len(he))
    numberCount=0
    top=0 
    while he:
        top,pos=heapq.heappop(he)   
        #print(top,pos) 
        x,y=pos
        numberCount+=1
        if numberCount==k:
            break
        if  n>y+1 :
            heapq.heappush(he,(lis[x][y+1],(x,y+1)))
    return top


if __name__ == '__main__':
    arr=[[2, 6, 8], [3, 6, 7], [1, 3, 4]]
    n=len(arr)
    ans=find_k_closest_numbers(arr, 5,n)
    arr2=[[2, 6, 8], [3, 7, 10], [5, 8, 11]]
    ans2=find_k_closest_numbers(arr2,5,n)
    print(ans,ans2)