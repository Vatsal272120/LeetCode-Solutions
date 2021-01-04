""" 
Anagram Check

Problem

Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".

Solution

There are two ways of thinking about this problem, if two strings have the same frequency of letters/element (meaning each letter shows up the same number of times in both strings) then they are anagrams of eachother. On a similar vien of logic, if two strings are equal to each other once they are sorted, then they are also anagrams of each other.

 """


def anagram(s1,s2):

    # Removing spaces and replacing all with lower case letters
    s1= s1.replace(' ','').lower()
    s2 = s2.replace(' ', '').lower()
    

    # check in length are similar, if yes then only move forward
    if len(s1) != len(s2):
        return False

    #intialize a counter 
    count ={}
    

    #add the frequency of each character of s1 into the dictionary
    for char in s1 :
        if char in count: 
            count[char]+=1
        else:
            count[char] = 1
    
    # check if the frequency of each character in the s2 is same in dict
    for char in s2:
        if char in count:
            count[char] -=1
        else:
            count[char] = 1

    # check the number in dict, if it is 0 then both are anagram, else return
    for k in count:
        if count[k] != 0:
            return False
        
    return True



print(anagram('clint eastwood', 'old west action'))