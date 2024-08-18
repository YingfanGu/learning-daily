# Recursion / Backtracking
 a. 39. Combination Sum https://leetcode.com/problems/combina...
 b. 40. Combination Sum II https://leetcode.com/problems/combina...
 c. 78. Subsets https://leetcode.com/problems/subsets/
 d. 90. Subsets II https://leetcode.com/problems/subsets...
 e. 46. Permutations https://leetcode.com/problems/permuta...
 f. 47. Permutations II https://leetcode.com/problems/permuta...



# Graph Traversal - DFS, BFS, Topological Sorting
 a. 133. Clone Graph https://leetcode.com/problems/clone-g... BFS / DFS
 b. 127. Word Ladder https://leetcode.com/problems/word-la... BFS
 c. 490. The Maze https://leetcode.com/problems/the-maze/ 

Kahn’s algorithm
 d. 210. Course Schedule II https://leetcode.com/problems/course-... (Topological Sorting)
 e. 269. Alien Dictionary https://leetcode.com/problems/alien-d... (Topological Sorting)

**Dijkstra’s algorithm (weight)**

**A star algorithm (heuristic functions)**


# Binary Tree / Binary Search Tree (BST)

Divide conquers
 a. 94. Binary Tree Inorder Traversal https://leetcode.com/problems/binary-...
 b. 236. Lowest Common Ancestor of a Binary Tree https://leetcode.com/problems/lowest-...
 c. 297. Serialize and Deserialize Binary Tree https://leetcode.com/problems/seriali...
 d. 98. Validate Binary Search Tree https://leetcode.com/problems/validat...
 e. 102. Binary Tree Level Order Traversal https://leetcode.com/problems/binary-... (BFS)



# Binary Search (二分法) OlogN
 a. 34. Find First and Last Position of Element in Sorted Array https://leetcode.com/problems/find-fi...
 b. 162. Find Peak Element https://leetcode.com/problems/find-pe...
 c. 69. Sqrt(x) https://leetcode.com/problems/sqrtx/
  

# Data Structure
 a. 242. Valid Anagram https://leetcode.com/problems/valid-a... (Hash Table)
 b. 133. Clone Graph https://leetcode.com/problems/clone-g... (Hash Table)
 c. 127. Word Ladder https://leetcode.com/problems/word-la... (Hash Table)
 d. 155. Min Stack https://leetcode.com/problems/min-stack/ (Stack)
 e. 225. Implement Stack using Queues https://leetcode.com/problems/impleme... (Stack / Queue)
 f. 215. Kth Largest Element in an Array https://leetcode.com/problems/kth-lar... (PriorityQueue)
 g. 23. Merge k Sorted Lists https://leetcode.com/problems/merge-k... (PriorityQueue)


**Insertion**: Adding a new element to the data structure.
**Deletion**: Removing an element from the data structure.
**Traversal**: Accessing each element of the data structure systematically to perform some operation on them.
**Searching**: Finding a specific element or set of elements in the data structure.
**Sorting**: Arranging the elements of the data structure in a specified order.
**Access**: Retrieving an element from a specific position within the data structure.




Search
Insert
delete

## Hash Table 




## Queue
In a queue, the operations of search, insert (enqueue), and delete (dequeue) typically have the following time complexities:
1.	Enqueue (Insert): O(1)O(1)O(1)
o	Adding an element to the rear of the queue is done in constant time because the location to insert is always known and does not depend on the size of the queue.
2.	Dequeue (Delete): O(1)O(1)O(1)
o	Removing an element from the front of the queue is also a constant time operation. The position to remove from is always the front, so no searching or shifting of elements is required.
3.	Search: O(n)O(n)O(n)
o	Searching for an element in a queue, however, does not have a direct access mechanism like arrays do. To find an element, you may need to traverse from the front to the back of the queue, inspecting each element. Therefore, this operation is linear in time complexity, depending on the number of elements in the queue.
These complexities are typical of most queue implementations, assuming no additional optimizations or data structures are used to facilitate faster search operations.

## Stack
In a stack, the time complexities for the search, insert (push), and delete (pop) operations are as follows:
1.	Push (Insert): O(1)O(1)O(1)
o	Adding an element to the top of the stack is a constant time operation because it simply involves placing the element at the top of the stack.
2.	Pop (Delete): O(1)O(1)O(1)
o	Removing the element from the top of the stack is also a constant time operation, as it only involves removing the topmost element.
3.	Search: O(n)O(n)O(n)
o	Searching for an element in a stack requires traversing the stack from the top to the bottom (or vice versa), which means the time complexity is linear, depending on the number of elements in the stack.
The O(1)O(1)O(1) time complexity for push and pop operations makes stacks highly efficient for scenarios where only the most recently added element needs to be accessed, while the linear time complexity for search reflects that stacks are not optimized for finding arbitrary elements quickly.

## Heap
A heap is a specialized tree-based data structure that satisfies the heap property (in a max-heap, the parent node is always greater than or equal to its children; in a min-heap, the parent node is always less than or equal to its children). Here are the time complexities for the search, insert, and delete operations in a heap:
1.	Insert: O(log⁡n)O(\log n)O(logn)
o	When inserting an element into a heap, the element is initially added at the end of the heap (at the next available position in the array representation). Then, the heap property is restored by "bubbling up" the element (also known as "heapify-up" or "sift-up"). This process takes logarithmic time because it might require comparing and swapping elements along the height of the tree, which is log⁡n\log nlogn for a heap with nnn elements.
2.	Delete (or Extract Max/Min): O(log⁡n)O(\log n)O(logn)
o	Deletion in a heap typically refers to removing the root element (the maximum element in a max-heap or the minimum element in a min-heap). After removing the root, the last element in the heap is moved to the root position, and the heap property is restored by "bubbling down" (or "heapify-down" or "sift-down") the element. This operation also takes logarithmic time, as it might involve moving down the tree's height.
3.	Search: O(n)O(n)O(n)
o	Searching for a specific element in a heap requires a linear scan of the elements because the heap does not have a sorted structure, only a partial order property. Therefore, in the worst case, the time complexity for searching an element is O(n)O(n)O(n).
To summarize:
•	Insert: O(log⁡n)O(\log n)O(logn)
•	Delete (or Extract Max/Min): O(log⁡n)O(\log n)O(logn)
•	Search: O(n)O(n)O(n)
Heaps are particularly useful for priority queues, where the most important element (highest or lowest) needs to be efficiently accessed and removed.






# Linked List Manipulation
 a. 237. Delete Node in a Linked List https://leetcode.com/problems/delete-...
 b. 92. Reverse Linked List II https://leetcode.com/problems/reverse...
 c. 876. Middle of the Linked List https://leetcode.com/problems/middle-...
 d. 143. Reorder List https://leetcode.com/problems/reorder...





