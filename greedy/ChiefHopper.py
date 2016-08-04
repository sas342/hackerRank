'''
https://www.hackerrank.com/challenges/chief-hopper


'''
def findMinimumEnergy(n, H):

    k = 0
    botEnergy = -1

    start = -1
    while botEnergy < 0:
        start += 1
        botEnergy = start

        for k in xrange(n):

            #find bot energy after leap to next building
            if H[k] > botEnergy:
                botEnergy -= (H[k] - botEnergy)
            else:
                botEnergy += (botEnergy - H[k])


            if botEnergy < 0:
                break

        #print "botEnergy=", botEnergy, " start=",start





    return start

n = int(raw_input())
H = [int(x) for x in raw_input().strip().split(" ")]

#n=100
#H = [int(x) for x in range(1,101,1)]
#print H
print findMinimumEnergy(n,H)