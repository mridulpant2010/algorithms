
import java.util.*;
import java.io.*;
import java.lang.*;


class BuildHeap{
	
	public static void main(String args[]){

		Queue<Integer> max_heap = new PriorityQueue<>(Collections.reverse_order());

		max_heap.add(10);
		max_heap.add(20);
		max_heap.add(30);
		max_heap.add(40);
		max_heap.add(5);
		max_heap.add(1);


		while(!max_heap.isEmpty()){

			System.out.println(max_heap.peek()+", ");

			max_heap.poll();
		}

	}	

}