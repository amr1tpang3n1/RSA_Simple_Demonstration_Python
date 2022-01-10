# RSA TOOL FOR KEY GENERATION AND ENCRYPTION
import base64


class RSA_Implementation:
    def __init__(self):
        print("================================================"
              "\n* --- --- --- --- --- --- --- ---- --- --- - *"
              "\n !!!! Warning: "
              "\n >> Choose Larger Prime Numbers."
              "\n* --- --- --- --- --- --- --- ---- --- --- - *")
        print("================================================")
        print("1. Key generation\n2. Encryption/Decryption: ")
        mode = input("Choose any one option :  ")
        if mode == '1':
            self.key_generation()
        elif mode == '2':
            print("================================================")
            print("1. Encryption\n2. Decryption")
            en_dc = input("Choose a option: ")
            if en_dc == "1":
                self.encryption()
            elif en_dc == "2":
                self.decryption()
            else:
                print("================================================")
                print("Invalid Option, Exiting ... ")
        else:
            print("Invalid Mode, Program Exiting ... ")

    @staticmethod
    def isprime(num):
        for n in range(2, int(num ** 1 / 2) + 1):
            if num % n == 0:
                return False
        return True

    @staticmethod
    def compute_hcf(x, y):
        while y:
            x, y = y, x % y
        return x

    def key_generation(self):
        print("================================================")
        p = input("Choose 1st Prime Number: ")
        q = input("Choose 2nd Prime Number: ")

        try:
            p = int(p)
            q = int(q)

        except Exception:
            print("Invalid Key, Program Exiting ... ")

        if self.isprime(int(p)) and self.isprime(int(q)) and p != 1 and q != 1:
            n = p * q
            phi_n = (p - 1) * (q - 1)

            public_key = None
            for e in range(2, phi_n):
                if self.compute_hcf(e, phi_n) == 1:
                    public_key = e
                    break

            if public_key is None:
                print("================================================")
                print("Calculation not possible, Try larger primes")

            else:
                private_key = None
                for d in range(2, phi_n):
                    if (d * public_key) % phi_n == 1:
                        private_key = d
                        break
                print(f"================================================\n"
                      f"* --- --- --- --- --- --- --- ---- --- --- - *"
                      f"\nPublic Key : \n {(public_key, n)} \n"
                      f"* --- --- --- --- --- --- --- ---- --- --- - *"
                      f"\nPrivate Key: \n {(private_key, n)} \n"
                      f"* --- --- --- --- --- --- --- ---- --- --- - *\n"
                      f"================================================")
        else:
            print("================================================")
            print("Given Numbers are not prime. Exiting ..")

    @staticmethod
    def encryption():
        print("================================================")
        print("Please Provide Encryption Key for Encryption: (e,N)")
        print("================================================")
        e = input("Provide value (e) : ")
        N = input("Provide value (N) : ")
        M = input("Message to Encrypt (m) : ")
        print("================================================")
        M = M.encode().hex()
        M = int(M, 16)
        try:
            e = int(e)
            N = int(N)
        except Exception:
            print("Wrong Key Provided, Exiting .. ")
            print("================================================")

        if M > N:
            print("Choose large prime for key,\n your key can't encrypt the message.")
            print("================================================")
        else:
            cipher_text = (M ** e) % N
            cipher_text = str(cipher_text)
            cipher_text = cipher_text.encode('ascii')
            cipher_text = base64.b64encode(cipher_text)
            cipher_text = cipher_text.decode('ascii')
            print("Cipher text : ", cipher_text)

    @staticmethod
    def decryption():
        print("================================================")
        print("Please Provide Decryption Key: (d,N)")
        print("================================================")
        d = input("Provide value (d) : ")
        N = input("Provide value (N) : ")
        M = input("Cipher Text B64 (c) : ")
        print("================================================")

        M = M.encode('ascii')

        try:
            M = base64.b64decode(M)
            M = int(M)
            d = int(d)
            N = int(N)
        except Exception:
            print("Wrong Key Provided")
            quit()

        if M > N:
            print("Invalid Key, Can't Decrypt message.")
            print("================================================")
        else:
            plain_text = (M ** d) % N
            plain_text = format(plain_text, 'X')
            byte_array = bytearray.fromhex(plain_text)
            byte_array = byte_array.decode()
            plain_text = byte_array

            print("Plain text : ", plain_text)


if __name__ == "__main__":
    obj = RSA_Implementation()
