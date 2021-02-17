""" 
Anagram Solution
Problem
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".


 """

""" Steps
  
  1. replace the spaces with no spaces and convert all to a lower case for both strings
  2. check if s1 and s2 have diff len. if so return false - as they are not anagrams
  3. intialize a counter
  4. populate the counter with each of the element of s1 while adding 1 for each repeated element
  5. do the same for the s2 but here subtracting for each of the repeated element
  6. check the counter, if all elements freq is zero then both the strings are anagrams of each other
  7 return true

 """

def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    check = {}

    for char in s1:
        if char in check:
            check[char] +=1
        else:
            check[char] = 1

    for letter in s2:
        if letter in check:
            check[letter] -=1
        else:
            check[letter]= 1


    for element in check:
        if check[element] !=0 :
            return False

        
    return True

 

print(anagram("clint eastwood","old west action" ))
print(anagram('go go go','gggooo'))
print(anagram('abc','cba'))
print(anagram('123','1 2'))

