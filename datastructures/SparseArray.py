def matches(wordlist, query):
    numMatches = 0
    for x in wordlist:
        if x == query:
            numMatches = numMatches + 1
    
    return numMatches

n = int(raw_input())
wordlist = list()
for i in xrange(n):
    wordlist.append(raw_input())

q = int(raw_input())
for i in xrange(q):
    print(matches(wordlist, i))
