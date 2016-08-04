


def insertionSort(ar):
    n = len(ar[0])

    for r in range(0,n,1):
        for c in range(1, n, 1):
            e = ar[r][c]
            innerIndex = c
            while (innerIndex > 0 and e <= ar[r][innerIndex - 1]):
                tmp = ar[r][innerIndex - 1]
                ar[r][innerIndex - 1] = e
                ar[r][innerIndex] = tmp
                innerIndex = innerIndex - 1

    return ar

def printMatrix(ar):
    n = len(ar[0])
    for r in range(0,n,1):
        print ar[r]

def validateMatrix(ar):
    n = len(ar)

    #left to right
    for r in range(0,n,1):
        for i in range(1,n,1):
            if ar[r][i] < ar[r][i-1]:
                #print 'comparing ',ar[r][i],' and ',ar[r][i-1]
                #print '[',r,']','[',i,']',' and [',r,']','[',i-1,']'
                return False

    #top to botoom
    for c in range(0,n,1):
        for i in range(1,n,1):
            if ar[i][c] < ar[i-1][c]:
                #print 'comparing ', ar[i][c], ' and ', ar[i-1][c]
                #print '[', i, ']', '[', c, ']', ' and [', i-1, ']', '[',c, ']'
                return False
    return True



n = int(raw_input())
for i in xrange(n):
    cnt = int(raw_input())
    w, h = cnt, cnt
    Matrix = [[0 for x in range(w)] for y in range(h)]
    for row in xrange(cnt):
        characters = raw_input()
        for c in xrange(cnt):
            Matrix[row][c] = characters[c]

    #print Matrix
    insertionSort(Matrix)
    #printMatrix(Matrix)
    valid = validateMatrix(Matrix)
    if valid:
        print "YES"
    else:
        print "NO"