
""" 
Find the Missing Element

Problem
Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

5 is the missing number

Solution
The naive solution is go through every element in the second array and check whether it appears in the first array. Note that there may be duplicate elements in the arrays so we should pay special attention to it. The complexity of this approach is O(N^2), since we would need two for loops.

A more efficient solution is to sort the first array, so while checking whether an element in the first array appears in the second, we can do binary search (we'll learn about binary search in more detail in a future section). But we should still be careful about duplicate elements. The complexity is O(NlogN).

 most interviews, you would be expected to come up with a linear time solution. We can use a hashtable and store the number of times each element appears in the second array. Then for each element in the first array we decrement its counter. Once hit an element with zero count that’s the missing element. Here is this solution: the first iterator is the missing element. This solution is also O(NlogN). Here is the solution for this approach: """


"""  

1. intiate the defaut dict
 2. loop thru second array and create a hash table
 3. loop thru first array and check if each element freqeuncy is 0, if so return 
 else decrement the num

 
 """
import collections

def finder(arr1, arr2):
  d = collections.defaultdict(int)

  for num in arr2:
     d[num] +=1
  
  for num in arr1:
    if d[num] == 0:
      return num
    else :
      d[num] -=1

    

print(finder([5,5,7,7],[5,7,7])) # 5
print(finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])) # 5 
print(finder([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1])) # 6
print(finder([1, 4, 5, 7, 9], [4, 5, 7, 9])) #1
