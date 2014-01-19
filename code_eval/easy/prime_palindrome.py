"""
CHALLENGE DESCRIPTION:

Write a program to determine the biggest prime palindrome under 1000.

INPUT SAMPLE:

There is no input for this program.

OUTPUT SAMPLE:

Your program should print the largest palindrome on stdout, i.e.

 929
"""

def is_prime(n):
    for i in range(2,n):
        if (n % i) == 0:
            return False
    return True


def find_primes(rang):
    primes_ = []
    numbers = range(1,rang)
    for num in numbers:
        if num % 2 != 0:
            if is_prime(num):
               primes_.append(num)
    return primes_

primes = find_primes(1000)
biggest = 0
for prime in primes:
    test_pal = str(prime)[::-1]
    str_prime = str(prime)
    if test_pal == str_prime:
        if prime > biggest:
            biggest = prime

print biggest 

