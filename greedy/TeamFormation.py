import sys

def findMinimumTeam(A,n):

    if n == 0:
        print 0
        return

    Groups = []
    previous = A[0]

    minGroup = sys.maxint
    Groups.append([previous])


    #print 'n=',n
    for i in xrange(1,n,1):
        current = A[i]
        added = False
        #remove any groups no longer needed
        for T in Groups:
            l = len(T)
            if current > T[l-1] + 1:
                if l < minGroup:
                    minGroup = l
                print T
                Groups.remove(T)

            elif current == T[l-1] + 1:
                #add
                T.append(current)
                added = True
                break

        if not added:
            newGroup = []
            newGroup.append(current)
            Groups.append(newGroup)

    for T in Groups:
        l = len(T)
        print T
        if l < minGroup:
            minGroup = l




    print minGroup

numTests = int(raw_input())
for i in xrange(numTests):
    A = [int(x) for x in raw_input().strip().split(' ')]
    n=A[0]
    A.remove(n)

    A.sort()
    findMinimumTeam(A,n)