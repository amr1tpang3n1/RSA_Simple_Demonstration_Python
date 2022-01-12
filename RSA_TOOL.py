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
                final_public_key = str((public_key, n))
                final_private_key = str((private_key, n))
                ####################################################
                final_public_key = final_public_key.encode('ascii')
                final_public_key = base64.b64encode(final_public_key)
                final_public_key = final_public_key.decode('ascii')
                ####################################################
                final_private_key = final_private_key.encode('ascii')
                final_private_key = base64.b64encode(final_private_key)
                final_private_key = final_private_key.decode('ascii')

                print(f"================================================\n"
                      f"* --- --- --- --- --- --- --- ---- --- --- - *"
                      f"\nPublic Key: \n {final_public_key} \n"
                      f"* --- --- --- --- --- --- --- ---- --- --- - *"
                      f"\nPrivate Key: \n {final_private_key} \n"
                      f"* --- --- --- --- --- --- --- ---- --- --- - *\n"
                      f"================================================")

                print()
                print("Public Key :", (public_key, n), "\nPrivate Key :", (private_key, n))
        else:
            print("================================================")
            print("Given Numbers are not prime. Exiting ..")

    @staticmethod
    def encryption():
        print("================================================")
        message = input("Message to Encrypt (M) : ")
        public_key = input("Encryption Key - B64 (E) : ")
        print("================================================")

        message = message.encode().hex()
        message = int(message, 16)

        public_key = public_key.encode('ascii')
        public_key = base64.b64decode(public_key)
        public_key = public_key.decode('ascii')
        public_key = eval(public_key)

        try:
            e = int(public_key[0])
            N = int(public_key[1])

        except Exception:
            print("Wrong Key Provided, Exiting .. ")
            print("================================================")
            quit()

        if message > N:
            print("Choose large prime for key,\n your key can't encrypt the message.")
            print("================================================")

        else:
            cipher_text = (message ** e) % N
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
        M = input("Cipher Text B64 (c) : ")
        private_key = input("Decryption Key B-64 (D) :")
        print("================================================")
        private_key = private_key.encode('ascii')
        private_key = base64.b64decode(private_key)
        private_key = private_key.decode('ascii')
        private_key = eval(private_key)

        M = M.encode('ascii')

        try:
            M = base64.b64decode(M)
            M = int(M)
            d = int(private_key[0])
            N = int(private_key[1])
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
