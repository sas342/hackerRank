'''
https://www.hackerrank.com/challenges/largest-permutation

Approach: always try to get the first k largest numbers to front of array
scott.stimmel
'''




def calcLargestPerm(A,k,n):
    indexArray = []

    for i in xrange(n):
        indexArray.append(0)

    j=0
    for i in A:
        indexArray[i-1] = j
        j += 1


    largestVal = n
    i = 0
    swapped = 0
    while swapped < k and i < n:

        #3print A
        #print indexArray

        if A[i] < largestVal:
            tmp = A[i]
            A[i] = largestVal
            largestIndex = indexArray[largestVal-1]
            A[largestIndex] = tmp
            #print "tmp=",tmp," largestVal=",largestVal," largestIndex=",largestIndex
            indexArray[largestVal-1] = i #update largestVal index to i
            #print "setting indexArray[",largestVal-1,"] to ",i
            indexArray[tmp-1] = largestIndex
            #print "setting indexArray[",tmp,"] to ",largestIndex

            swapped += 1

        largestVal -= 1
        i += 1
    return A

n,k = [int(x) for x in raw_input().split(' ')]
A = [int(x) for x in raw_input().strip().split(' ')]

A = calcLargestPerm(A,k,n)
print ' '.join([str(x) for x in A])