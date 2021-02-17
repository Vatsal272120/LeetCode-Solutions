
""" Largest Continuous Sum
Problem
Given an array of integers (positive and negative) find the largest continuous sum.

Solution
If the array is all positive, then the result is simply the sum of all numbers. The negative numbers in the array will cause us to need to begin checking sequences.

The algorithm is, we start summing up the numbers and store in a current sum variable. After adding each element, we check whether the current sum is larger than maximum sum encountered so far. If it is, we update the maximum sum. As long as the current sum is positive, we keep adding the numbers. When the current sum becomes negative, we start with a new current sum. Because a negative current sum will only decrease the sum of a future sequence. Note that we don’t reset the current sum to 0 because the array can contain all negative integers. Then the result would be the largest negative number. """





def sum(arr) :
   
   currentSum = maxSum = arr[0]
   #print(currentSum)

   for num in arr[1:]:
     # set current sum as the higher of the current element in the iteration and current element
     currentSum = max( currentSum + num, num)
   
   # set maxSum as higher of currentSUm and maxSum
     maxSum = max(currentSum, maxSum)
     

   return maxSum

 

s = sum([1,2,-1,3,4,10,10,-10,-1]) # 29
d = sum([1,2,-1,3,4,-1]) # 9 
k = sum([-1,1]) # 1
 


print(s, d, k)