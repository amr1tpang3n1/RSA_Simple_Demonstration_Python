# RSA_Simple_Demonstration_Python
RSA Simple Implementation using Python. 

## Theory
RSA (named after great mathematicians Rivest, Shamir and Adleman) is a public-key or asymmetric key crypto system which is widely used for secure data transmission all over the world. 

The idea of an asymmetric public-private key crypto system is attributed to Whitfield Diffie and Martin Hellman, who published this concept in 1976. They also introduced digital signatures and attempted to apply number theory. Their formulation used a shared-secret-key created from exponentiation of some number, modulo a prime number. However, they left open the problem of realizing a one-way function, possibly because the difficulty of factoring was not well-studied at the time which was settled by RSA. We will understand how in key generation process below. 

## Process
The RSA involves 4 process which are as follows:
1. Key generation 
2. Key Distribution
3. Encryption
4. Decryption

## Key Generation 

Firstly, Two large unique prime numbers are selected as follows.
The product of two unique prime number is used as modulus. Higher the modules more bits can be encrypted at once and more bits keys are generated. 
p = Prime_Number1
q = Prime_Number2
n = p * q (Modulus)

Phi_n = (p-1)*(q-1)

For the selection of e, we have certain criteria which are as follows:
1. 1 < e < phi_n 
2. HCF of e and Phi_n should be 1.

Larger Modules are preferred but for demonstration purpose, Let's suppose 3 and 11 as p and q.
p = 3
q = 11

### Step 1: 

Calculating n to use it as modulus. 

n = 3 * 11 

n = 33

### Step 2:

Calculating phi_n, 
phi_n = (3 - 1) * (11-1)
phi_n = 20

### Step 3:
we have these numbers between 1 and 20. 

According to 1st Criteria,

probable_e = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

According to 2nd Criteria, 

HCF(probable_e, phi_n) == 1

probable_e = [3, 7, 9,11, 13, 17, 19]

We may choose any from the list. Let's take e as 3.

e = 3

### Step 4:

Hence, Public Key will be  (e, n) which is (3, 33).

### Step 5:
For selection of private key (d) selection has some criteria which are as follows:
1. Greater than 1 and Less than phi_n
2. Must satisfy this condition (d * e) % phi_n == 1

With this we have following private key, 
d = 7

### Step 6:

Hence, Private key will be (d, n) which is (7, 33).

## Encryption

The encryption process is quite simple, Let's take a message (m), as already mentioned above, modulus of the key should be greater to encrypt the greater values. m < n for the encryption to work. we can use large prime numbers to generate large keys to encrypt the larger values. we can also divide the message to different shares as like shamir sharing concept. 

m = "a"

Let's suppose a = 20

In real case, we can use ASCII table for conversion of strings to numbers. 

m = 20

e = 3 

N = 33

Now, 

Cipher_text = m^e (mod n)

cipher_text = 20^3 (mod 33)

which gives, 

Cipher text =  14

## Decryption Process

cipher_text = 14

d = 7 

n = 33

Now, 

Plain text = cipher_text ^ d (mod n)

Plain text = 14 ^ 7 mod 33

Plain text = 20

Plain text = "a" (as supposed above)

## Implementation in python 

The simple demonstration of the RSA as per the above discussion is in rsa.py file which looks like this.
```Python
# Simple Implementation of Rivest–Shamir–Adleman (RSA) Asymmetric Encryption
# Simple Demonstration file for understanding the algorithms

P = 7
Q = 11

N = P * Q
phi_n = (P - 1) * (Q - 1)


# Calculating HCF to find, Relatively prime numbers with phi_n
# Euclidean Algorithm
def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x


public_key = None
for e in range(2, phi_n):
    if compute_hcf(e, phi_n) == 1:
        public_key = e
        break

if public_key is None:
    print("Unknown Error ... Exiting ")
    quit()

else:
    print("Public Key: ", (public_key, N))

private_key = None
for d in range(2, phi_n):
    if (d * public_key) % phi_n == 1:
        private_key = d
        break

if public_key is None:
    print("Unknown Error ..., Exiting ")
    quit()

else:
    print("Private Key: ", (private_key, N))
# Let's Try using our generated keys to encrypt and decrypt

message = "Hello"
lets_say = {"Hello": 20}

cipher_text = (20 ** public_key) % N
print(cipher_text)

# Cipher text of above operation was 48
plain_text = (48 ** private_key) % N
print(plain_text)


```
The tool made using the same concept is in RSA_TOOL.py which generates key in Base 64 and Encrypts and Decrypts the message using the key generated. 
