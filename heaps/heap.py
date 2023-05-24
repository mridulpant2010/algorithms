import heapq,math
'''
following are the important method associated with the heap 

1. heappush(heap, item)
2. heappop(heap)
3. heapify(x) : transforms list x into  a heap, in-place, in linear-time.
4. heappushpop(heap,item)
5. heapreplace(heap,item)
6. heapq.merge
7. heapq.nsmallest
8. heapq.nlargest


https://docs.python.org/3/library/heapq.html





'''


# implementing heap sort

iterable = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]

def heapsort(iterable):
    new_heap =[]
    for each_value in iterable:
        heapq.heappush(new_heap,each_value)
    sort_list = []
    for _ in new_heap:
        sort_list.append(heapq.heappop(new_heap))
    return sort_list


#heap python implementation
'''
    main operations
        - constructors
        - insert
        - extract min
        - decrease key
        - delete
        - constructor(enhanced with the build heap)


    utility functions
        - left child
        - right child
        - min-heapify
        - parent


'''


class Heap:        

    def __init__(self,new_arr=[]):
        self.heap_list = []
        if len(self.heap_list) == 0:
            self.heap_list = new_arr
            for i in range(len(self.heap_list),-1,-1):
                parent = self._parent(i)
                self.min_heapify(parent,len(self.heap_list))
        

    def insert(self,val):
        """inserts a new value to the heap
        """
        self.heap_list.append(val)
        last_index = len(self.heap_list)-1
        while last_index>0 and self.heap_list[last_index]<self.heap_list[self._parent(last_index)]:
            self.heap_list[last_index] , self.heap_list[self._parent(last_index)] = self.heap_list[self._parent(last_index)] , self.heap_list[last_index] 
            last_index = self._parent(last_index)
        #self.heapify(0,len(self.heap_list))


    def extract_min(self):
        """extracts the minimum value from the heap and the heap properties should be there.
        """
        n = len(self.heap_list)
        if n == 0:
            return math.inf
        res = self.heap_list[0]
        self.heap_list[0] = self.heap_list[n-1]
        self.heap_list.pop()
        self.min_heapify(0,n)
        return res

    def _left_child(self,node):
        print(2*node+1)
        return 2*node+1

    def _right_child(self,node):
        print(2*node+2)
        return 2* node+2

    def _parent(self,node):
        return (node-1)//2

    def min_heapify(self,i,n):
        """build heap function

        Args:
            i (current node): current node
            n (total): total number of elements in the heap
        """
        left_child = self._left_child(i)
        right_child = self._right_child(i)
        smallest = i

        if left_child < n and self.heap_list[left_child] < self.heap_list[smallest]:
            smallest = left_child

        if right_child < n and self.heap_list[right_child] < self.heap_list[smallest]:
            smallest = right_child

        if smallest!=i :
            print(self.heap_list[i],self.heap_list[smallest])
            self.heap_list[i],self.heap_list[smallest] = self.heap_list[smallest],self.heap_list[i]
            self.heap_list[i],self.heap_list[smallest]
            self.min_heapify(smallest,n)
        

    def delete(self,i):
        pass
    def build_heap(self):
        # how the build heap function looks like.
        pass

    def __str__(self):
        return str(self.heap_list)


if __name__ == "__main__":

    
    li = [45, 25, 100, 50, 40, 20, 10, 15]
    print(li)
    heap = Heap(li)
    # for each in li:
    #     heap.insert(each)
    print(li)
    print(heap)
    #print(heap.extract_min())
    #print(heap.heap_list)
