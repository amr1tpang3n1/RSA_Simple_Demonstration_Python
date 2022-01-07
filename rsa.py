# 2 Prime Numbers
p = 7
q = 17

N = 7 * 17

print("N : ",N)

phi_N = (p-1)*(q-1)
print("Phi N : ", phi_N)

# No common factorials with
Public_Key = 5
D = 77
Private_key = 77
if ((D*Public_Key) % phi_N) == 1:
    print("Yes")
    Private_key = D

encryption = (83**Public_Key) % N
print(encryption)

decryption = (104**Private_key) % N
print(decryption)