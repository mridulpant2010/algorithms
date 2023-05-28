theory.md



## This file contains relevant theorertical information related to heaps and doubts in case we have them.

https://practice.geeksforgeeks.org/batch/ppc-1/track/ppc-heap/article/MjM3OA%3D%3D


### questions

- what is a heap?
- how heap is better than an array or any other primitive data structure.
- heap vs tree, what is the significance and comparison? what is a complete binary tree
- when to use heapsort and is it better than quicksort or mergesort?
- does directly calling the heappush operation also perform heapify internally?




## Heap theory
- the only interesting theory about the heap is that a[0] is always the smallest element.
- heaps are basically binary trees for which every parent node has a value less than or equal to any of its children. This implementation uses arrays for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k, counting elements from zero.


Binary Heap
	



## HeapSort



## Implementation

- python has an algorithm which does the same, 




## References
- https://practice.geeksforgeeks.org/batch/ppc-1/track/ppc-heap/article/MjM3OA%3D%3D

