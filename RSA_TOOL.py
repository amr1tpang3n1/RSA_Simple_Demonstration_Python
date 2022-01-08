# RSA TOOL FOR KEY GENERATION AND ENCRYPTION

class RSA_TOOL:
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
            pass
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

    def encryption(self):
        pass


obj = RSA_TOOL()
