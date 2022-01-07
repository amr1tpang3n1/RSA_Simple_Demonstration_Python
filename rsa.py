import math
print("===========================================")
print("RSA Encryption and Decryption")
print("Simple Demonstration")
# RSA Algorithm Simplified
print("===========================================")
dummy_flag = "SOFTWARICA{DUMMY_FLAG}"
encoded_flag = []
print()
print("Encoded Flag in ASCII DECIMAL:")
print("===========================================")
print()

for i in dummy_flag:
    encoded_flag.append(ord(i))
print("Original:")
print(encoded_flag)

p, q = 2, 7

N = p * q

phi_n = (p - 1) * (q - 1)

# For Public E
"""
e must be smaller than phi_n and is co-prime of phi_n. 
For Considered P = 2 and Q = 7 , N = 14, phi_n = 6 
so, e must be in range of 2*,3*,4*,5
Only Possible Co-prime is 5 so, 
e = 5
Writing Algorithm for above task. 
"""

# Possible e
range_list = []
for i in range(phi_n):
    if i != 1:
        range_list.append(i)

print()
print("===========================================")
print("The Possible values of e are:")
print(range_list)
print()
print("===========================================")
print("Finding the e that satisfy the condition")

def co_prime_calculation(range_list, phi_n):
    for i in range_list:
        if math.gcd(i, phi_n) == 1:
            return i

e_encryption = co_prime_calculation(range_list, phi_n)
print("Hence, e = ",e_encryption)

print("Encryption Key (e,n):", f"{e_encryption,N}")
print()
final_encrypted_flag = []
for i in encoded_flag:
    encrypted_flag = i ** e_encryption % N
    final_encrypted_flag.append(encrypted_flag)

print("===========================================")
print("Encrypted ASCII: ")
print(final_encrypted_flag)

# For Decryption, we require decryption key
"""
For calculating d, 
Let's generate 10 multiples of e. 
de = 1 mod phi_n
"""

print()
print("===========================================")
print("Decryption:")
print("===========================================")
print()
multiples_of_e = []

for i in range(1, 10):
    multiples_of_e.append(i * e_encryption)
print(multiples_of_e)

for i in multiples_of_e:
    d_key = i * 1 % phi_n
    if d_key == 1:
        print(i)
