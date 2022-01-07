import random
import math
from math import gcd as bltin_gcd

def co_prime_calculation(phii_n):
    while True:
        co_prime_number = random.randrange(phii_n)
        if math.gcd(co_prime_number, phii_n) == 1:
            return co_prime_number

def coprime2(a, b):
    return bltin_gcd(a, b) == 1

print(co_prime_calculation(phii_n=10))
print(coprime2(3,10))