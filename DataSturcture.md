

https://freegeektime.com/posts/100017301/

https://github.com/javasmall/bigsai-algorithm/tree/master

https://doc.vercel.app/ds/article/39922.html

continue:
https://doc.vercel.app/ds/article/41222.html

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
Time complexity O(|E| + |V|log|V|)



**A star algorithm (heuristic functions)**

https://paul.pub/a-star-algorithm/

F = G + H
https://www.bilibili.com/video/BV1iG411v7b9/?spm_id_from=333.337.search-card.all.click&vd_source=1245de838130ee71ba0169feb6595e6d



# 3 Binary Tree / Binary Search Tree (BST)

Divide conquers
 a. 94. Binary Tree Inorder Traversal https://leetcode.com/problems/binary-... check
 b. 236. Lowest Common Ancestor of a Binary Tree https://leetcode.com/problems/lowest-...
 c. 297. Serialize and Deserialize Binary Tree https://leetcode.com/problems/seriali...
 d. 98. Validate Binary Search Tree https://leetcode.com/problems/validat...
 e. 102. Binary Tree Level Order Traversal https://leetcode.com/problems/binary-... (BFS)



# 4 Binary Search (二分法) O（logN）
 a. 34. Find First and Last Position of Element in Sorted Array https://leetcode.com/problems/find-fi... check
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




Information on this topic is now available on Wikipedia at: Search data structure

    +----------------------+----------+------------+----------+--------------+
    |                      |  Insert  |   Delete   |  Search  | Space Usage  |
    +----------------------+----------+------------+----------+--------------+
    | Unsorted array       | O(1)     | O(1)       | O(n)     | O(n)         |
    | Value-indexed array  | O(1)     | O(1)       | O(1)     | O(n)         |
    | Sorted array         | O(n)     | O(n)       | O(log n) | O(n)         |
    | Unsorted linked list | O(1)*    | O(1)*      | O(n)     | O(n)         |
    | Sorted linked list   | O(n)*    | O(1)*      | O(n)     | O(n)         |
    | Balanced binary tree | O(log n) | O(log n)   | O(log n) | O(n)         |
    | Heap                 | O(log n) | O(log n)** | O(n)     | O(n)         |
    | Hash table           | O(1)     | O(1)       | O(1)     | O(n)         |
    +----------------------+----------+------------+----------+--------------+

 * The cost to add or delete an element into a known location in the list (i.e. if you have an iterator to the location) is O(1). If you don't know the location, then you need to traverse the list to the location of deletion/insertion, which takes O(n) time.
 * The deletion cost is O(log n) for the minimum or maximum, O(n) for an arbitrary element.


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

* **单链表:** 链表通过指针将一组零散的内存块串联在一起。其中，我们把内存块称为链表的“结点”。为了将所有的结点串起来，每个链表的结点除了存储数据之外，还需要记录链上的下一个结点的地址。如图所示，我们把这个记录下个结点地址的指针叫作后继指针next。其中有两个结点是比较特殊的，它们分别是第一个结点和最后一个结点。我们习惯性地把第一个结点叫作**头结点**，把最后一个结点叫作**尾结点**。其中，头结点用来记录链表的基地址。有了它，我们就可以遍历得到整条链表。而尾结点特殊的地方是：指针不是指向下一个结点，而是指向一个**空地址NULL**，表示这是链表上最后一个结点。

* **循环链表:** 循环链表的优点是从链尾到链头比较方便。当要处理的数据具有环型结构特点时，就特别适合采用循环链表。比如著名的**约瑟夫问题**。尽管用单链表也可以实现，但是用循环链表实现的话，代码就会简洁很多。  


* **双向链表:** 单向链表只有一个方向，结点只有一个后继指针next指向后面的结点。而双向链表，顾名思义，它支持两个方向，每个结点不止有一个后继指针next指向后面的结点，还有一个前驱指针prev指向前面的结点。

双向链表需要额外的两个空间来存储后继结点和前驱结点的地址。所以，如果存储同样多的数据，双向链表要比单链表占用更多的内存空间。虽然两个指针比较浪费存储空间，但可以支持双向遍历，这样也带来了双向链表操作的灵活性。

从结构上来看，双向链表可以支持O(1)时间复杂度的情况下找到前驱结点，正是这样的特点，也使双向链表在某些情况下的插入、删除等操作都要比单链表简单、高效。

你可能会说，我刚讲到单链表的插入、删除操作的时间复杂度已经是O(1)了，双向链表还能再怎么高效呢？别着急，刚刚的分析比较偏理论，很多数据结构和算法书籍中都会这么讲，但是这种说法实际上是不准确的，或者说是有先决条件的。我再来带你分析一下链表的两个操作。



https://github.com/javasmall/bigsai-algorithm/blob/master/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E7%AE%97%E6%B3%95/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E7%AE%97%E6%B3%95%E2%80%94%E5%8F%8C%E9%93%BE%E8%A1%A8.md

这就是为什么在实际的软件开发中，双向链表尽管比较费内存，但还是比单链表的应用更加广泛的原因。如果你熟悉Java语言，你肯定用过LinkedHashMap这个容器。如果你深入研究LinkedHashMap的实现原理，就会发现其中就用到了双向链表这种数据结构。


### Search O(n) 

但是，有利就有弊。链表要想随机访问第k个元素，就没有数组那么高效了。因为链表中的数据并非连续存储的，所以无法像数组那样，根据首地址和下标，通过寻址公式就能直接计算出对应的内存地址，而是需要根据指针一个结点一个结点地依次遍历，直到找到相应的结点。

你可以把链表想象成一个队伍，队伍中的每个人都只知道自己后面的人是谁，所以当我们希望知道排在第k位的人是谁的时候，我们就需要从第一个人开始，一个一个地往下数。所以，链表随机访问的性能没有数组好，需要O(n)的时间复杂度。



对于一个有序链表，**双向链表**的按值查询的效率也要比单链表高一些。因为，我们可以记录上次查找的位置p，每次查询时，根据要查找的值与p的大小关系，决定是往前还是往后查找，所以平均只需要查找一半的数据。




### Insert O(1)

双向链表的插入删除操作的时间复杂度为O(1)，是因为双向链表中每个节点都有指向前一个节点和后一个节点的指针，所以在进行插入删除操作时，只需要改变相邻节点的指针指向即可，不需要像数组一样进行元素的移动，因此时间复杂度为O(1)。


    链表插入元素前，还是要先遍历找到需要插入的位置的地址O(n)，然后插入O(1)，为什么说链表的插入的时间复杂度是O(1)
    如题，这是我在看数据结构中链表的时候产生的疑惑。
    其实，这源于对链表认识不够深刻。今天闲着没事看了jdk中LinkedList的源码，突然惊觉一个事情，LinkedList中属性就size、first（用于储存第一个节点的地址）、last（用于储存最后一个节点的位置），serialVersionUID（序列化是验证版本一致性的值，Long类型）。所以链表的插入，并不会像顺序线性表一样，指定一个下标，然后插入，而是，要么头插法，要么尾插法，而头结点或者尾结点的地址，是可以直接拿到的，所以插入时，只需要判断last或者first是否为null，然后赋值就行了，时间复杂度固然是O(1).
    至于标题中所说的，什么时候链表的插入复杂度为O(n)呢，就是一个有序的链表，插入后，仍然要保持有序，此时，时间复杂度为O(n).（此处不会涉及到排序算法的时间复杂度，因为插入前的链表就已经是有序状态，所以只需要从第一个元素开始遍历找到刚好比需要插入元素大\小的位置即可）


        双向链表相比于单向链表，所谓的O(1)是指删除、插入操作。

       单向链表要删除某一节点时，必须要先通过遍历的方式找到前驱节点（通过待删除节点序号或按值查找）。若仅仅知道待删除节点，是不能知道前驱节点的，故单链表的增删操作复杂度为O(n)。 双链表（双向链表）知道要删除某一节点p时，获取其前驱节点q的方式为 q = p->prior，不必再进行遍历。故时间复杂度为O(1)。而若只知道待删除节点的序号，则依然要按序查找，时间复杂度仍为O(n)。

       单、双链表的插入操作，若给定前驱节点，则时间复杂度均为O(1)。否则只能按序或按值查找前驱节点，时间复杂度为O(n)。至于查找，二者的时间复杂度均为O(n)。 对于最基本的CRUD操作，双链表优势在于删除给定节点。但其劣势在于浪费存储空间（若从工程角度考量，则其维护性和可读性都更低）。

       双链表本身的结构优势在于，可以O(1)地找到前驱节点，若算法需要对待操作节点的前驱节点做处理，则双链表相比单链表有更加便捷的优势。


同理，如果我们希望在链表的某个指定结点前面插入一个结点，**双向链表**比**单链表**有很大的优势。双向链表可以在O(1)时间复杂度搞定，而单向链表需要O(n)的时间复杂度。


### delete O(1)


在实际的软件开发中，从链表中删除一个数据无外乎这两种情况：

删除结点中“值等于某个给定值”的结点；

删除给定指针指向的结点。

对于第一种情况，不管是**单链表**还是双**向链表**，为了查找到值等于给定值的结点，都需要从头结点开始一个一个依次遍历对比，直到找到值等于给定值的结点，然后再通过我前面讲的指针操作将其删除。

尽管单纯的删除操作时间复杂度是O(1)，但遍历查找的时间是主要的耗时点，对应的时间复杂度为O(n)。根据时间复杂度分析中的加法法则，删除值等于给定值的结点对应的链表操作的总时间复杂度为O(n)。

对于第二种情况，我们已经找到了要删除的结点，但是删除某个结点q需要知道其前驱结点，而单链表并不支持直接获取前驱结点，所以，为了找到前驱结点，我们还是要从头结点开始遍历链表，直到p->next=q，说明p是q的前驱结点。

但是对于双**向链表**来说，这种情况就比较有优势了。因为双向链表中的结点已经保存了前驱结点的指针，不需要像单链表那样遍历。所以，针对第二种情况，单链表删除操作需要O(n)的时间复杂度，而双向链表只需要在O(1)的时间复杂度内就搞定了！



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

实际上，这里有一个更加重要的知识点需要你掌握，那就是用空间换时间的设计思想。当内存空间充足的时候，如果我们更加追求代码的执行速度，我们就可以选择空间复杂度相对较高、但时间复杂度相对很低的算法或者数据结构。相反，如果内存比较紧缺，比如代码跑在手机或者单片机上，这个时候，就要反过来用时间换空间的设计思路。

还是开篇缓存的例子。缓存实际上就是利用了空间换时间的设计思想。如果我们把数据存储在硬盘上，会比较节省内存，但每次查找数据都要询问一次硬盘，会比较慢。但如果我们通过缓存技术，事先将数据加载在内存中，虽然会比较耗费内存空间，但是每次数据查询的速度就大大提高了。



# 链表VS数组性能大比拼
通过前面内容的学习，你应该已经知道，数组和链表是两种截然不同的内存组织方式。正是因为内存存储的区别，它们插入、删除、随机访问操作的时间复杂度正好相反。



不过，数组和链表的对比，并不能局限于时间复杂度。而且，在实际的软件开发中，不能仅仅利用复杂度分析就决定使用哪个数据结构来存储数据。

数组简单易用，在实现上使用的是连续的内存空间，可以借助CPU的缓存机制，预读数组中的数据，所以访问效率更高。而链表在内存中并不是连续存储，所以对CPU缓存不友好，没办法有效预读。

数组的缺点是大小固定，一经声明就要占用整块连续内存空间。如果声明的数组过大，系统可能没有足够的连续内存空间分配给它，导致“内存不足（out of memory）”。如果声明的数组过小，则可能出现不够用的情况。这时只能再申请一个更大的内存空间，把原数组拷贝进去，非常费时。链表本身没有大小的限制，天然地支持动态扩容，我觉得这也是它与数组最大的区别。

你可能会说，我们Java中的ArrayList容器，也可以支持动态扩容啊？我们上一节课讲过，当我们往支持动态扩容的数组中插入一个数据时，如果数组中没有空闲空间了，就会申请一个更大的空间，将数据拷贝过去，而数据拷贝的操作是非常耗时的。

我举一个稍微极端的例子。如果我们用ArrayList存储了了1GB大小的数据，这个时候已经没有空闲空间了，当我们再插入数据的时候，ArrayList会申请一个1.5GB大小的存储空间，并且把原来那1GB的数据拷贝到新申请的空间上。听起来是不是就很耗时？

除此之外，如果你的代码对内存的使用非常苛刻，那数组就更适合你。因为链表中的每个结点都需要消耗额外的存储空间去存储一份指向下一个结点的指针，所以内存消耗会翻倍。而且，对链表进行频繁的插入、删除操作，还会导致频繁的内存申请和释放，容易造成内存碎片，如果是Java语言，就有可能会导致频繁的GC（Garbage Collection，垃圾回收）。

所以，在我们实际的开发中，针对不同类型的项目，要根据具体情况，权衡究竟是选择数组还是链表。