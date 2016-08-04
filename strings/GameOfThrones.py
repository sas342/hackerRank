'''
Created on Apr 9, 2016
Check if given string is anagram of palindrome

@author: sstimmel
'''

def isPalindrome(string):
    charArray = [0 for x in range(26)]
    
    for x in string:
        val = ord(x)-97
        charArray[val] = charArray[val] + 1
    
    numOfUneven = 0
    for x in range(0,26,1):    
        #print(x," => ",charArray[x]," ",charArray[x] % 2)        
        if (charArray[x] % 2 != 0):
            numOfUneven = numOfUneven + 1
    
    if (numOfUneven == 1 or numOfUneven == 0):
        return "YES"
    
    return "NO"



string = str(raw_input())
print isPalindrome(string)