Assignment 6: Medians and Order Statistics & Elementary Data Structures

Shashwat Baral
University of the Cumberlands
Algorithms and Data Structures (MSCS-532-B01)
Date of Submission: 11/22/25

1. Introduction

This report explores two foundational areas of computer science: Selection Algorithms and Elementary Data Structures.

Part 1 focuses on the problem of finding the $k^{th}$ smallest element in an array (order statistics). We analyze and compare Randomized Quickselect, which offers excellent average-case performance, against Deterministic Selection (Median of Medians), which guarantees linear time complexity even in the worst case.

Part 2 examines the implementation and performance trade-offs of fundamental data structures: Arrays, Stacks, Queues, and Linked Lists. We discuss their theoretical time complexities and their practical applications in real-world software systems.

2. Part 1: Implementation and Analysis of Selection Algorithms

The goal of a selection algorithm is to find the $k^{th}$ smallest element in an unsorted list of $n$ elements.

2.1 Implementation Overview

1. Randomized Quickselect (Expected Linear Time)
This algorithm is a variation of Quicksort. Instead of recursively sorting both partitions, it recurses into only one partition—the one that contains the $k^{th}$ element.

Pivot Selection: Uses a random element.

Logic: Partition the array around the pivot. If the pivot's index is $k$, return the pivot. If $k$ is smaller, recurse left; otherwise, recurse right.

2. Deterministic Selection (Median of Medians)
This algorithm improves upon Quickselect by guaranteeing a "good" pivot, ensuring the recursion depth never degrades to $O(n)$.

Pivot Selection:

Divide the array into groups of 5 elements.

Find the median of each group.

Recursively find the median of those medians.

Use this "median of medians" as the pivot for partitioning.

2.2 Performance Analysis

Time Complexity

Randomized Quickselect:

Average Case: $O(n)$. On average, the random pivot splits the array roughly in half. The work done is $n + n/2 + n/4 + \dots = 2n$, which is linear.

Worst Case: $O(n^2)$. Like Quicksort, if the pivot is always the minimum or maximum, the problem size reduces by only 1 at each step ($n + (n-1) + \dots$).

Deterministic Selection:

Worst Case: $O(n)$. By finding the median of medians, we guarantee that the pivot is roughly in the middle 30-70% range of the data. This ensures a balanced split, preventing the worst-case recurrence. The recurrence relation is roughly $T(n) \approx T(n/5) + T(7n/10) + O(n)$, which solves to linear time $O(n)$.

Space Complexity

Randomized Quickselect: $O(1)$ auxiliary space if implemented iteratively (tail recursion optimization), or $O(\log n)$ stack space for recursion.

Deterministic Selection: $O(\log n)$ for recursion stack space.

2.3 Empirical Analysis

We compared both algorithms on arrays of size $n=5000$.

Input Type (n=5000)

Randomized Select

Deterministic Select

Analysis

Random Array

~0.002 sec

~0.015 sec

Randomized is significantly faster due to lower constant factors (no overhead of computing medians of groups).

Sorted Array

~0.003 sec

~0.016 sec

Randomized performs well. Deterministic remains consistent but slower due to overhead.

Reverse-Sorted

~0.002 sec

~0.016 sec

Both algorithms handle this well, though Deterministic is consistently slower.

Discussion:
While the Deterministic algorithm provides a superior theoretical worst-case guarantee ($O(n)$ vs $O(n^2)$), in practice, Randomized Quickselect is almost always preferred. The overhead of dividing arrays into groups of 5 and finding medians recursively makes the deterministic approach significantly slower (higher constant factors) for typical inputs.

3. Part 2: Elementary Data Structures

3.1 Implementation Overview

Array: Implemented as a wrapper around Python's list to demonstrate static size concepts.

Stack: Implemented using an array (LIFO - Last In First Out).

Queue: Implemented using an array (FIFO - First In First Out).

Singly Linked List: Implemented using Node objects with data and next pointers.

3.2 Performance Analysis

Operation

Array / Stack (Array)

Queue (Array)

Linked List

Access (Index)

$O(1)$

N/A

$O(n)$

Insert (Front)

$O(n)$ (Shift required)

N/A

$O(1)$

Insert (End)

$O(1)$ (Amortized)

$O(1)$

$O(1)$ (with tail ptr)

Delete (Front)

$O(n)$ (Shift required)

$O(n)$ (Shift required)

$O(1)$

Delete (End)

$O(1)$

N/A

$O(n)$ (No prev ptr)

Discussion on Trade-offs:

Arrays vs. Linked Lists:

Arrays provide $O(1)$ random access (indexing) and are cache-friendly due to contiguous memory. However, inserting or deleting from the beginning/middle is expensive ($O(n)$) because elements must be shifted.

Linked Lists allow $O(1)$ insertion and deletion (if the node reference is known), especially at the head. However, they lack random access ($O(n)$ search) and use more memory per element (storing the pointer).

Stacks and Queues:

Implementing a Stack with an array is efficient ($O(1)$ push/pop at end).

Implementing a Queue with a standard array is inefficient for dequeue ($O(n)$) because removing the first element requires shifting all remaining elements. A Linked List is often superior for Queues ($O(1)$ enqueue/dequeue).

3.3 Practical Applications

Arrays: Used for matrices, image processing buffers, and lookup tables where index-based access is frequent.

Stacks: Essential for function call management (recursion stack), undo mechanisms in editors, and syntax parsing (checking balanced parentheses).

Queues: Used in task scheduling (CPU, printers), breadth-first search (BFS) in graphs, and handling asynchronous data streams.

Linked Lists: Used in dynamic memory allocation, implementing graphs (adjacency lists), and as the underlying structure for flexible stacks/queues.

4. Conclusion

This assignment highlights the balance between theoretical guarantees and practical efficiency. In selection algorithms, while the deterministic "Median of Medians" is a theoretical triumph, the randomized approach dominates in practice. In data structures, the choice between arrays and linked lists dictates the efficiency of the entire system depending on whether read-access or write-flexibility is the priority.

5. References

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to Algorithms (4th ed.). MIT Press.

Sedgewick, R., & Wayne, K. (2011). Algorithms (4th ed.). Addison-Wesley Professional.
