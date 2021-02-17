""" LeetCode #01 """

""" Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice. """


def twoSum(arr, k):
    counter = dict()
    
    for i, num in enumerate(arr):
        if num not in counter:
            counter[k - num] = i
        else:
            return [counter[num], i]
        
        
        
        
        
        
        
s = twoSum([2,7,11,15], 9)
print(s)