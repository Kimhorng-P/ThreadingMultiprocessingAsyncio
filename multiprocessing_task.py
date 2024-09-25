import multiprocessing
import math

def is_prime(n):
  if n <= 1: 
    return False 
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i ==0: 
      return False
  else:
    return True
  pass

def check_prime_chunk(numbers):
  prime_numbers = []
  for number in numbers:
    if is_prime(number):
      prime_numbers.append(number)
  return prime_numbers
  pass

def find_primes_in_range(numbers, chunk_size):
  chunks = []
  for number in range(0, len(numbers), chunk_size):
    chunk = numbers[number:number + chunk_size]
    chunks.append(chunk)

  with multiprocessing.Pool() as pool:
    result = pool.map(check_prime_chunk, chunks)
  
  primes = []
  for sublist in result:
    for prime in sublist:
      primes.append(prime)
  pass
