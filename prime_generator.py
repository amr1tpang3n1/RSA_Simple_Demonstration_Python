# Tool to generate the prime numbers of choices.

def isprime(num):
    for n in range(2, int(num ** 1 / 2) + 1):
        if num % n == 0:
            return False
    return True


def prime_generator(start, stop):
    prime_numbers = []
    for i in range(start, stop + 1):
        if isprime(i):
            prime_numbers.append(i)
    return prime_numbers


if __name__ == "__main__":
    start_range = input("Start: ")
    stop_range = input("Upto: ")

    try:
        start_range = int(start_range)
        stop_range = int(stop_range)
        print(prime_generator(start_range,stop_range))
    except Exception:
        print("Wrong Range Provided")