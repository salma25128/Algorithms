                                                                             
Think  First
----------
# Algorithms(steps player use different techniques to score a goal)
## step-by-step procedures or formulas for solving problems
### Algorithms classified into several types based on different criteria


## 1. Functionality:

**Sorting Algorithms:** Arrange elements in a list in a particular order.

**Examples:** Bubble Sort, Quick Sort, Merge Sort, Heap Sort.

**Searching Algorithms:** Find specific elements within a data structure.

**Examples:** Binary Search, Linear Search, Depth-First Search (DFS), Breadth-First Search (BFS).

**Dynamic Programming Algorithms:** Solve complex problems by breaking them down into simpler subproblems.

**Examples:** Fibonacci Sequence, Knapsack Problem, Longest Common Subsequence.

**Greedy Algorithms:** Make the most optimal choice at each step with the hope of finding the global optimum.

**Examples**: Dijkstra's Algorithm, Prim's Algorithm, Kruskal's Algorithm.

**Backtracking Algorithms:** Solve problems by trying out different solutions and discarding those that fail to satisfy the problem's constraints.

**Examples:** N-Queens Problem, Sudoku Solver, Subset Sum Problem.

**Divide and Conquer Algorithms**: Divide the problem into smaller subproblems, solve them independently, and then combine their solutions.

**Examples:** Merge Sort, Quick Sort, Binary Search.

## 2. Paradigm:

**Recursive Algorithms:** Solve problems by calling themselves with a simpler version of the original problem.

**Examples**: Factorial Calculation, Tower of Hanoi, Tree Traversal.

**Iterative Algorithms**: Solve problems through repetitive loops until a condition is met.

**Examples:** Iterative Deepening Search, Iterative Binary Search.

**Brute Force Algorithms**: Solve problems by trying every possible solution to find the best one.

**Examples**: Traveling Salesman Problem, String Matching.

**Randomized Algorithms:** Use random numbers to make decisions during execution.

**Examples:** Randomized Quick Sort, Monte Carlo Algorithm.

## 3.  Design Approach:

**Greedy Algorithms:** Make a series of choices, each of which looks best at the moment, with the hope that this will lead to a global optimum.

**Dynamic Programming Algorithms:** Use past results to solve subproblems and build up the solution to the overall problem.

**Backtracking Algorithms**: Build up a solution incrementally and abandon solutions ("backtrack") as soon as it is determined that they cannot lead to a valid solution.

**Divide and Conquer Algorithms:** Break the problem into smaller pieces, solve each piece independently, and combine the results.

## 4.Application Domain:

**Graph Algorithms**: Specifically designed to solve problems related to graph data structures.

**Examples:** Dijkstra's Algorithm, Bellman-Ford Algorithm, Floyd-Warshall Algorithm.

**String Algorithms**: Deal with problems related to string processing.

Examples: KMP Algorithm, Rabin-Karp Algorithm, Boyer-Moore Algorithm.

**Cryptographic Algorithms**: Used in cryptography for secure data transmission.

**Examples**: RSA, AES, DES, SHA.

**Machine Learning Algorithms**: Used in machine learning for making predictions or classifications.

**Examples**: Decision Trees, Neural Networks, Support Vector Machines, K-Means Clustering.

## 5.Complexity:

**Linear Time Algorithms**: Have a time complexity of O(n).

**Logarithmic Time Algorithms**: Have a time complexity of O(log n).

**Quadratic Time Algorithms**: Have a time complexity of O(n²).

**Exponential Time Algorithms**: Have a time complexity of O(2^n).

## 6. Problem Type:

**Optimization Algorithms**: Aim to find the best solution among a set of possible solutions.

**Examples:** Genetic Algorithms, Simulated Annealing, Particle Swarm Optimization.

**Decision Algorithms**: Answer yes/no questions or determine if a solution exists.	

**Approximation Algorithms**: Provide approximate solutions to complex problems within a specified degree of accuracy.


------------------------------------------------------------------------------------------------------------


* RECURSION :
  -----------
	 * https://github.com/salma25128/Algorithms/blob/725a244d59ac96cfab7d92dc55ea04a70486d337/recursion.py#L1

	* In Math recursion means a relationship defined by itself 
	* Some of the sorting and searching algorithms depending on Recursion as (quicksort , mergesort , binary search......).
  
	 ![image](https://github.com/user-attachments/assets/623dfc12-08b2-4c96-b054-aaf96203bbad)


* Divide & Conquer:
  --------------------- 
	* https://github.com/salma25128/Algorithms/blob/725a244d59ac96cfab7d92dc55ea04a70486d337/divide_and_conquer.py#L3
 		

* QuickSort :
   ----------------
    * https://github.com/salma25128/Algorithms/blob/725a244d59ac96cfab7d92dc55ea04a70486d337/Quicksort.py#L4
  
        1. Pick a pivot.
		2. Partition the array into two sub-arrays: elements less than the pivot and elements greater than the pivot.
		3. Call quicksort recursively on the two sub-arrays.
   ![image](https://github.com/user-attachments/assets/228113c4-6851-4d7b-bee7-f485aea42e7c)
  
		
				 
	A brute force algorithm solves a problem through exhaustion: it goes through all possible choices until a solution is found.
The time complexity of a brute force algorithm is often proportional to the input size.
Brute force algorithms are simple and consistent, but very slow.


	  
