from math import sqrt

class Util():
    def findPrimes(self, upTo):
        sq = int(sqrt(upTo))

        numbers = [0, 0, 0]
        odd = True
        for i in xrange(3, upTo):
            if odd:
                numbers.append(1)
                odd = False
            else:
                numbers.append(0)
                odd = True

        primes = []

        for i in xrange(3, sq, 2):
            if numbers[i] == 1:
                numbers = self.removeFactors(i, upTo, numbers)

        for i in xrange(3, upTo):
            if numbers[i] == int(1):
                primes.append(i)

        return primes

    def removeFactors(self, i, upTo, primes):
        x = i * 2
        j = 2
        while x < upTo:
            primes[x] = 0
            j = j + 1
            x = i * j

        return primes


class Euler3():
    def run(self):

        n = int(raw_input())
        max = 0
        tmp = []
        for i in xrange(n):
            tmp.append(int(raw_input()))
            if tmp[i] > max:
                max = tmp[i]
        primes = Util().findPrimes(max)
        for i in tmp:
            print self.findMaxPrime(i, primes)

    def findMaxPrime(self, j, primes):
        max_prime = 0
        for p in primes:
            if p > j:
                return max_prime

            if j % p == 0:
                max_prime = p

        if max_prime > 0:
            return max_prime

        return j

class Euler1():
    def run(self):
        n = int(raw_input())

        for i in xrange(n):
            t = int(raw_input())
            self.findSum(t)

    def findFiveMultiple(self, t):
        n = t - 1
        while n > 0:
            if n % 5 == 0:
                return n
            n = n - 1
        return 0

    def findThreeMultiple(self, t):
        n = t - 1
        while n > 0:
            if n % 3 == 0:
                return n
            n = n - 1
        return 0

    def findSum(self, t):

        three = self.findThreeMultiple(t)
        five = self.findFiveMultiple(t)
        sum = three + five

        while three > 0 or five > 0:

            three = three - 3
            five = five - 5

            if three > 0:
                sum = sum + three

            if five > 0:
                sum = sum + five

        print sum

#Euler3().run()
Euler1().run()
