# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


def calc_primes():
    primes = []
    poss_prime = 2
    while len(primes) < 10001:
        is_prime = True
        for num in range(2, int(poss_prime ** 0.5) + 1):
            if poss_prime % num == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(poss_prime)

        poss_prime += 1

    return primes


print(calc_primes()[-1])

