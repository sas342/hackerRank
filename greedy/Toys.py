import heapq

# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, rupees):
    q = []

    answer = 0
    for p in prices:
        heapq.heappush(q, p)

    while rupees > 0:
        try:
            p = heapq.heappop(q)
            rupees = rupees - p
            if rupees >= 0:
                answer = answer + 1
        except:
            return answer

    return answer

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  print max_toys(prices, k)
