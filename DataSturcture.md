# 1 Recursion / Backtracking
 a. 39. Combination Sum https://leetcode.com/problems/combina...  check
 b. 40. Combination Sum II https://leetcode.com/problems/combina... check
 c. 78. Subsets https://leetcode.com/problems/subsets/ check
 d. 90. Subsets II https://leetcode.com/problems/subsets... check
 e. 46. Permutations https://leetcode.com/problems/permuta... check
 f. 47. Permutations II https://leetcode.com/problems/permuta... check



# 2 Graph Traversal - DFS, BFS, Topological Sorting  **
 a. 133. Clone Graph https://leetcode.com/problems/clone-g... BFS / DFS check
 b. 127. Word Ladder https://leetcode.com/problems/word-la... BFS check
 c. 490. The Maze https://leetcode.com/problems/the-maze/ 

Kahn’s algorithm
 d. 210. Course Schedule II https://leetcode.com/problems/course-... (Topological Sorting)
 e. 269. Alien Dictionary https://leetcode.com/problems/alien-d... (Topological Sorting)

**Dijkstra’s algorithm (weight)**



**A star algorithm (heuristic functions)**




# 3 Binary Tree / Binary Search Tree (BST)

Divide conquers
 a. 94. Binary Tree Inorder Traversal https://leetcode.com/problems/binary-...
 b. 236. Lowest Common Ancestor of a Binary Tree https://leetcode.com/problems/lowest-...
 c. 297. Serialize and Deserialize Binary Tree https://leetcode.com/problems/seriali...
 d. 98. Validate Binary Search Tree https://leetcode.com/problems/validat...
 e. 102. Binary Tree Level Order Traversal https://leetcode.com/problems/binary-... (BFS)



# 4 Binary Search (二分法) OlogN
 a. 34. Find First and Last Position of Element in Sorted Array https://leetcode.com/problems/find-fi...
 b. 162. Find Peak Element https://leetcode.com/problems/find-pe...
 c. 69. Sqrt(x) https://leetcode.com/problems/sqrtx/
  

# 5 Data Structure
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

## Array

针对数组类型，很多语言都提供了容器类，比如Java中的ArrayList、C++ STL中的vector。在项目开发中，什么时候适合用数组，什么时候适合用容器呢？

这里我拿Java语言来举例。如果你是Java工程师，几乎天天都在用ArrayList，对它应该非常熟悉。那它与数组相比，到底有哪些优势呢？

我个人觉得，ArrayList最大的优势就是可以将很多数组操作的细节封装起来。比如前面提到的数组插入、删除数据时需要搬移其他数据等。另外，它还有一个优势，就是支持动态扩容。

https://doc.vercel.app/ds/article/40961.html#%E8%AD%A6%E6%83%95%E6%95%B0%E7%BB%84%E7%9A%84%E8%AE%BF%E9%97%AE%E8%B6%8A%E7%95%8C%E9%97%AE%E9%A2%98
### Search O(1) 根据下标

这里我要特别纠正一个“错误”。我在面试的时候，常常会问数组和链表的区别，很多人都回答说，“链表适合插入、删除，时间复杂度O(1)；数组适合查找，查找时间复杂度为O(1)”。

实际上，这种表述是不准确的。数组是适合查找操作，但是查找的时间复杂度并不为O(1)。即便是排好序的数组，你用二分查找，时间复杂度也是O(logn)。所以，正确的表述应该是，数组支持随机访问，根据下标随机访问的时间复杂度为O(1)。


### Insert O(n)
假设数组的长度为n，现在，如果我们需要将一个数据插入到数组中的第k个位置。为了把第k个位置腾出来，给新来的数据，我们需要将第k～n这部分的元素都顺序地往后挪一位。那插入操作的时间复杂度是多少呢？你可以自己先试着分析一下。
如果在数组的末尾插入元素，那就不需要移动数据了，这时的时间复杂度为O(1)。但如果在数组的开头插入元素，那所有的数据都需要依次往后移动一位，所以最坏时间复杂度是O(n)。 因为我们在每个位置插入元素的概率是一样的，所以平均情况时间复杂度为(1+2+…n)/n=O(n)。

### delete O(n)
跟插入数据类似，如果我们要删除第k个位置的数据，为了内存的连续性，也需要搬移数据，不然中间就会出现空洞，内存就不连续了。

和插入类似，如果删除数组末尾的数据，则最好情况时间复杂度为O(1)；如果删除开头的数据，则最坏情况时间复杂度为O(n)；平均情况时间复杂度也为O(n)。



## Linked list
数组需要一块连续的内存空间来存储，对内存的要求比较高。如果我们申请一个100MB大小的数组，当内存中没有连续的、足够大的存储空间时，即便内存的剩余总可用空间大于100MB，仍然会申请失败。

而链表恰恰相反，它并不需要一块连续的内存空间，它通过“指针”将一组零散的内存块串联起来使用，所以如果我们申请的是100MB大小的链表，根本不会有问题。

三种最常见的链表结构，它们分别是：单链表、双向链表和循环链表







## Hash Table 
Here’s a summary of the time complexities for the search, insert, and delete operations in hash tables:
1.	Insert:
o	Average Case: O(1)O(1)O(1)
o	Worst Case: O(n)O(n)O(n)
o	Explanation: In the average case, inserting an element into a hash table is constant time because it involves computing the hash of the key and placing the element in the appropriate bucket. However, in the worst case, if many elements hash to the same bucket (causing a collision), and the collision resolution strategy involves traversing a linked list or another data structure, the time complexity can degrade to linear in the number of elements.
2.	Delete:
o	Average Case: O(1)O(1)O(1)
o	Worst Case: O(n)O(n)O(n)
o	Explanation: Deletion follows a similar pattern to insertion. In the average case, it's constant time because the element can be directly accessed and removed using the hash value. In the worst case, if there are many collisions, finding the element to delete might require traversing a linked list or another structure, resulting in linear time complexity.
3.	Search:
o	Average Case: O(1)O(1)O(1)
o	Worst Case: O(n)O(n)O(n)
o	Explanation: Searching for an element in a hash table is typically constant time on average because the hash function allows direct access to the bucket where the element should reside. However, in the worst case, with many collisions, searching might require traversing through elements in a bucket, resulting in a linear time complexity.
To summarize:
•	Insert: O(1)O(1)O(1) average, O(n)O(n)O(n) worst case
•	Delete: O(1)O(1)O(1) average, O(n)O(n)O(n) worst case
•	Search: O(1)O(1)O(1) average, O(n)O(n)O(n) worst case
The efficiency of hash tables heavily depends on the quality of the hash function and the load factor (the ratio of the number of elements to the number of buckets). A well-designed hash table with a good hash function and appropriate load factor will generally provide constant time performance for these operations.




## Queue
In a queue, the operations of search, insert (enqueue), and delete (dequeue) typically have the following time complexities:
1.	Enqueue (Insert): O(1)
o	Adding an element to the rear of the queue is done in constant time because the location to insert is always known and does not depend on the size of the queue.  
2.	Dequeue (Delete): O(1)
o	Removing an element from the front of the queue is also a constant time operation. The position to remove from is always the front, so no searching or shifting of elements is required.
3.	Search: O(n)
o	Searching for an element in a queue, however, does not have a direct access mechanism like arrays do. To find an element, you may need to traverse from the front to the back of the queue, inspecting each element. Therefore, this operation is linear in time complexity, depending on the number of elements in the queue.
These complexities are typical of most queue implementations, assuming no additional optimizations or data structures are used to facilitate faster search operations.

## Stack
In a stack, the time complexities for the search, insert (push), and delete (pop) operations are as follows:
1.	Push (Insert): O(1)
o	Adding an element to the top of the stack is a constant time operation because it simply involves placing the element at the top of the stack.
2.	Pop (Delete): O(1)
o	Removing the element from the top of the stack is also a constant time operation, as it only involves removing the topmost element.
3.	Search: O(n)
o	Searching for an element in a stack requires traversing the stack from the top to the bottom (or vice versa), which means the time complexity is linear, depending on the number of elements in the stack.
The O(1) time complexity for push and pop operations makes stacks highly efficient for scenarios where only the most recently added element needs to be accessed, while the linear time complexity for search reflects that stacks are not optimized for finding arbitrary elements quickly.

## Heap (priority queue find K smallest sth)


而堆就是**一类特殊的数据结构**的统称。堆通常是一个可以被看做一棵树(完全)的数组对象。且总是满足以下规则：

- 堆总是一棵**完全二叉树** 
- 每个节点总是大于(或小于)它的孩子节点。

**对于完全二叉树**，我想大家都能明白，就是最底层叶子节点要严格按照从左向右来。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201006234654325.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwNjkzMTcx,size_1,color_FFFFFF,t_70)
**堆有大根堆和小根堆**，如果是所有父节点都大于子节点的时候，那么这就是个大根堆，反之则为小根堆，以下就是一个大根堆：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201019214838156.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwNjkzMTcx,size_1,color_FFFFFF,t_70)
最后需要注意的是我们并不是用链式去储存这个二叉树而是用**数组去存储这个树**，虽然链式的使用场景可能更多一些，但是在完全二叉树的情况下空间使用率较好没有斜树的出现。并且在操作的时候可以直接通过编号找到位置进行交换。


A heap is a specialized tree-based data structure that satisfies the heap property (in a max-heap, the parent node is always greater than or equal to its children; in a min-heap, the parent node is always less than or equal to its children). Here are the time complexities for the search, insert, and delete operations in a heap:
1.	Insert: O(log⁡n)
o	When inserting an element into a heap, the element is initially added at the end of the heap (at the next available position in the array representation). Then, the heap property is restored by "bubbling up" the element (also known as "heapify-up" or "sift-up"). This process takes logarithmic time because it might require comparing and swapping elements along the height of the tree, which is log⁡n\log nlogn for a heap with nnn elements.
2.	Delete (or Extract Max/Min): O(log⁡n)
o	Deletion in a heap typically refers to removing the root element (the maximum element in a max-heap or the minimum element in a min-heap). After removing the root, the last element in the heap is moved to the root position, and the heap property is restored by "bubbling down" (or "heapify-down" or "sift-down") the element. This operation also takes logarithmic time, as it might involve moving down the tree's height.
3.	Search: O(n)
o	Searching for a specific element in a heap requires a linear scan of the elements because the heap does not have a sorted structure, only a partial order property. Therefore, in the worst case, the time complexity for searching an element is O(n).
To summarize:
•	Insert: O(log⁡n)O(\log n)O(logn)
•	Delete (or Extract Max/Min): O(log⁡n)O(\log n)O(logn)
•	Search: O(n)O(n)O(n)
Heaps are particularly useful for priority queues, where the most important element (highest or lowest) needs to be efficiently accessed and removed.



**The time complexity to find the minimum element in a min-heap is O(1).**

Explanation:
Min-Heap Property: In a min-heap, the smallest element is always at the root, which is the first element in the array representation of the heap.
Accessing the Minimum: Since the minimum element is always located at the root, accessing it requires no traversal or additional computation, making the operation a constant time operation.
Therefore, finding the minimum element in a min-heap is an O(1) operation.


# 6 Linked List Manipulation (链表)

search O(n)


 a. 237. Delete Node in a Linked List https://leetcode.com/problems/delete-...
 b. 92. Reverse Linked List II https://leetcode.com/problems/reverse...
 c. 876. Middle of the Linked List https://leetcode.com/problems/middle-...
 d. 143. Reorder List https://leetcode.com/problems/reorder...


# 7 Pointer Manipulation
 a. 239. Sliding Window Maximum https://leetcode.com/problems/sliding...
 b. 3. Longest Substring Without Repeating Characters https://leetcode.com/problems/longest...
 c. 76. Minimum Window Substring https://leetcode.com/problems/minimum...



# 8 Sorting
 a. Time -- O(N log N)
 b. Merge Sort -- Space O(N)
 c. Quick Sort
 Merge Sort Quick Sort different
 d. 148. Sort List https://leetcode.com/problems/sort-list/



# 9 Convert Real Life Problem to Code 
 a. 146. LRU Cache https://leetcode.com/problems/lru-cache/
 b. 1066. Compus Bike https://leetcode.com/problems/campus-...
 c. 490. The Maze https://leetcode.com/problems/the-maze/ 



 

# 10 Time Space Complexity
 a. 一般面试的时候 你说完算法 就要说 这个算法的 time / space complexity是什么
 b. 每次你做完一道题 给自己养成一个习惯 就是想一下他的时间空间复杂度是多少


### 空间复杂度

**概念**：是对一个算法在运行过程中临时占用存储空间大小的量度，记做S(n)=O(f(n))

空间复杂度其实在算法的衡量占比是比较低的(我们经常使用牺牲空间换时间的数据结构和算法)，但是不能忽视空间复杂度中重要性。无论在刷题还是实际项目生产内存都是一个极大额指标。对于Java而言更是如此。本身内存就大，如果采用的存储逻辑不太好会占用更多的系统资源，对服务造成压力。

而算法很多情况都是牺牲空间换取时间(效率)。就比如我们熟知的字符串匹配`String.contains()`方法，我们都知道他是暴力破解，时间复杂度为O(n^2),不需要借助额外内存。而`KMP`算法在效率和速度上都原生暴力方法，但是KMP要借助其他数组(`next[]`)进行标记储存运算。就用到了空间开销。再比如归并排序也会借助新数组在递归分冶的适合进行逐级计算，提高效率，但增加点影响不大的内存开销。

当然，算法的空间花销最大不能超过jvm设置的最大值，一般为2G.(2147483645)如果开二维数组多种多维数据不要开的太大，可能会导致`heap OutOfMemoryError`。 

### 时间复杂度

**概念**：计算机科学中，算法的时间复杂度是一个`函数`，它定性描述了该算法的运行时间。这是一个关于代表算法输入值的字符串的长度的函数。时间复杂度常用大O符号表述，**不包括这个函数的低阶项和首项系数**。使用这种方式时，时间复杂度可被称为是渐近的，它考察当输入值大小趋近无穷时的情况。

**时间复杂度的排序**：O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(n^3) < O(2^n) <O(n!) < O(n^n)

**常见时间复杂度**：对于时间复杂度，很多人的概念是比较模糊的。下面举例子说明一些时间复杂度。

O(1):  常数函数
- `a=15`

O(logn): 对数函数

- `for(int i=1;i<n;i*=2)`
分析：假设执行`t`次使得`i=n`;有2^t=n; t=log2~n,为log级别时间复杂度为O(logn)。
- 还有典型的二分查找，拓展欧几里得，快速幂等算法均为O(logn)。属于高效率算法。

O(n): 线性函数
- `for (int i=0;i<n;i++)`
- 比较常见，能够良好解决大部分问题。

O(nlogn): 
- `for (int i=1;i<n;i++)`
` for (int j=1;j<i;j*=2)`
- 常见的排序算法很多正常情况都是nlogn，比如快排、归并排序。这种算法效率大部分也还不错。

O(n^2)

- `for(int i=0;i<n;i++)`
 `for(int j=0;j<i;j++)`
 - 其实O(n^2)的效率就不敢恭维了。对于大的数据O(n^2)甚至更高次方的执行效果会很差。

当然如果同样是n=10000.那么不同时间复杂度额算法执行次数、时间也不同。



|    具体    |     n | 执行次数      |
| :--------: | ----: | ------------- |
|    O(1)    | 10000 | 1             |
|  O(log2n)  | 10000 | 14            |
| O( n^1/2)  | 10000 | 100           |
|    O(n)    | 10000 | 10000         |
| O(nlog2 n) | 10000 | 140000        |
|   O(n^2)   | 10000 | 100000000     |
|   O(n^3)   | 10000 | 1000000000000 |

降低算法复杂度有些会靠数据结构的特性和优势，比如二叉排序树的查找，线段树的动态排序等等，这些数据结构解决某些问题有些非常良好的性能。还有的是靠算法策略解决，比如同样是排序，冒泡排序这种笨而简单的方法就是O(n2),但快排、归并等聪明方法就能O(nlogn)。要想变得更快，那就得掌握更高级的数据结构和更精巧的算法。

**时间复杂度计算**
时间复杂度计算一般`步骤`：1、找到执行次数最多的语句; 2、计算语句执行的数量级 ; 3、用O表示结果。并且有两个规则：

加法规则： 同一程序下如果多个并列关系的执行语句那么取最大的那个,eg:

``` 
T(n)=O(m)+O(n)=max(O(m),O(n)); 
T(n)=O(n)+O(nlogn)=max(O(n),O(nlogn))=O(nlogn);
```

乘法规则：循环结构，时间复杂度按乘法进行计算,eg：

```
T(n)=O(m)*O(n)=O(mn)
T(n)=O(m)*O(m)=O(m^2)(两层for循环)
```

当然很多算法的时间复杂度还跟输入的数据有关，分为还会有最优时间复杂度(可能执行次数最少时)，最坏时间复杂度(执行次数最少时)，平均时间复杂度，这在排序算法中已经具体分析，但我们通常使用**平均时间复杂度**来衡量一个算法的好坏。

