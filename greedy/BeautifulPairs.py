class BeautifulPairs():

    def __init__(self):
        self.counts = {}


    def findPairs(self, A, B):
        matches = 0
        mismatch = False
        for _a in A:
            try:
                B.remove(_a)
                matches = matches + 1
            except:
                if not mismatch:
                    matches = matches + 1

                mismatch = True

        if not mismatch:
            matches = matches - 1
        print matches

n = int(raw_input())
A = raw_input().strip().split(' ')
B = raw_input().strip().split(' ')
b = BeautifulPairs()
b.findPairs(A,B)

