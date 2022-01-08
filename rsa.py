# Simple Implementation of Rivest–Shamir–Adleman (RSA) Asymmetric Encryption

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
for e in range(2, 200):
    if compute_hcf(e, phi_n) == 1:
        public_key = e
        break

if public_key is None:
    print("Increase the Range")
    quit()
else:
    print("Public Key: ", (public_key, N))

private_key = None
for d in range(2, 200):
    if (d * public_key) % phi_n == 1:
        private_key = d
        break

if public_key is None:
    print("Increase the Range")
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
