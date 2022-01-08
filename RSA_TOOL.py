# RSA TOOL FOR KEY GENERATION AND ENCRYPTION

class RSA_TOOL:
    def __init__(self):
        print("=========================================================================================")
        print("- Choose large prime numbers, RSA can't encrypt bigger numbers than its modulus.")
        mode = input("Key generation (1), Encrypt with existing keys (2): ")
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
        p = input("Please Choose 1st Prime Number (1) : ")
        q = input("Please Choose 2nd Prime Number (2) : ")

        try:
            p = int(p)
            q = int(q)

        except Exception:
            print("Invalid Key, Program Exiting ... ")

        if self.isprime(int(p)) and self.isprime(int(q)):
            n = p * q
            phi_n = (p - 1) * (q-1)

            public_key = None
            for e in range(2, phi_n):
                if compute_hcf(e, phi_n) == 1:
                    public_key = e
                    break

            if public_key is None:
                print("Unknown Error ... ")
                quit()

            else:
                print("Public Key: ", (public_key, N))

            if public_key is None:
                print("Unknown Error ...")
                quit()

            else:
                print("Private Key: ", (private_key, N))

        else:
            print("Only Prime Numbers, Program Exiting ...")


obj = RSA_TOOL()
