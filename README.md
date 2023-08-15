# Flip_Bits

Given an array A[] consisting of 0’s and 1’s. A flip operation is one in which you turn 1 into 0 and a 0 into 1. You have to do at most one “Flip” operation of any subarray. Formally, select a range (l, r) in the array A[], such that (0 ≤ l ≤ r < n) holds and flip the elements in this range to get the maximum ones in the final array. You can possibly make zero operations to get the answer.

Example 1:

Input:

N = 5
A[] = {1, 0, 0, 1, 0} 

Output:

4

Explanation:

We can perform a flip operation in the range [1,2]
After flip operation array is : [ 1 1 1 1 0 ]
Count of one after fliping is : 4
