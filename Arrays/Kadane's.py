"""  kadane algorithm for max sub array  """

""" The simple idea of Kadane’s algorithm is to look for all positive contiguous segments of the array (max_ending_here is used for this). And keep track of maximum sum contiguous segment among all positive segments (max_so_far is used for this). Each time we get a positive-sum compare it with max_so_far and update max_so_far if it is greater than max_so_far  """

""" Initialize:
    max_so_far = 0
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  (c) if(max_ending_here < 0)
            max_ending_here = 0
return max_so_far

 """



def sum(arr) :

 max_so_far = max_ending_here = 0

 for num in arr:
   max_ending_here = max_ending_here + arr[num]
   if (max_so_far < max_ending_here):
     max_so_far  = max_ending_here
   else:
     if (max_ending_here < 0):
       max_ending_here = 0
   return max_so_far

  







s = sum([1,2,-1,3,4,10,10,-10,-1]) # 29
d = sum([1,2,-1,3,4,-1]) # 9 
k = sum([-1,1]) # 1
 


print(s, d, k)