import math
import hashlib
from hashlib import sha1

import Cryptodome.Hash.SHA1
from sympy import isprime
from Cryptodome.Signature import PKCS1_v1_5
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
import random

minPrime = 100
maxPrime = 1000
cached_primes = [i for i in range(minPrime, maxPrime) if isprime(i)]
p, q = random.sample(cached_primes, 2)
tot = math.lcm(p-1, q-1)
print(p)
print(q)
print(tot)
e = random.randrange(1, tot)
print(f"ini e = {e}")
g = math.gcd(e, tot)
print(f"g = {g}")
if g == 1:
    d = pow(e, -1, tot)
    print(e)
    print(d)
while g != 1:
    e = random.randrange(1, tot)
    print(f"e = {e}")
    g = math.gcd(e, tot)
    if g == 1:
        d = pow(e, -1, tot)
        print(e)
        print(d)
        break






#
# def check_prime(n):
#     if isprime(n):
#         print(n)
#     else:
#         n = int(input("Not a prime number, please input a prime number: "))
#         check_prime(n)
#
#
# def check_e(n, x):
#     if 1 < n < x:
#         if math.gcd(n, x) == 1:
#             print(n)
#         else:
#             n = int(input("Invalid, input e: "))
#             check_e(n, x)
#     else:
#         n = int(input("Invalid, input e: "))
#         check_e(n, x)
#
#
# p = int(input("Input p: "))
# check_prime(p)
# q = int(input("Input q: "))
# check_prime(q)
#
# tot = math.lcm(p - 1, q - 1)
# print(tot)
#
# e = int(input(f"Choose e where 1 < e < {tot} and e is coprime to {tot} (Common choices: 3, 17, 65537): "))
# check_e(e, tot)
#
# d = pow(e, -1, tot)
# print(d)
#
# m = input("Input message: ")
# m = sha1(m.encode('utf-8')).hexdigest()
# md_1 = int(m, base=16)
# print(md_1)
