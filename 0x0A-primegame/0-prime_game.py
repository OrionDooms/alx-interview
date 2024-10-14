#!/usr/bin/python3

def checkForPrime(n):
    if n < 2:
        return [0] * (n + 1)

    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    prime_count = [0] * (n + 1)
    count = 0

    for i in range(2, n + 1):
        if is_prime[i]:
            count += 1
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
        prime_count[i] = count
        
    return prime_count


def isWinner(x, nums):
      if x > 0 or nums:
          max_n = max(nums)
          prime_count = checkForPrime(max_n)
          maria = 0
          ben = 0
          for n in nums:
              if prime_count[n] % 2 == 1:
                  maria += 1
              else:
                  ben += 1
          if maria > ben:
              return "Maria"
          else:
              return "Ben"
      
      return None
