
def findMaxToysToBuy(t):
    cnt = 0
    current = None
    for i in t:
        v = int(i)
        #print v
        if current == None:
            current = v
            cnt = cnt + 1
        elif current + 4 >= v:
            #print "skipping ",v
            continue
        else:
            current = v
            cnt = cnt + 1

        #print "current=",current
    return cnt


n = int(raw_input())
t = [int(x) for x in raw_input().split(' ')]
t.sort()
print findMaxToysToBuy(t)