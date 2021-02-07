# Day 4

def find_prime(high_num):
  nums = range(high_num+1)
  prime_list = []

  for num in nums:
    if num == 0 or num == 1:
      # print(f'{num} is not a prime')
      continue

    res = []
    for d in range(2,num):
      res.append(num % d)
    
    if 0 in res:
      # print(f'{num} is not a prime')
      pass
    else:
      # print(f'{num} is a prime')
      prime_list.append(num)

  return(prime_list)

print('List of prime numbers between 0 and 100 \n', find_prime(100))