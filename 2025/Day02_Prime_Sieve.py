# Day02_Prime_Sieve.py
# Prime Number Generator using Sieve of Eratosthenes

def sieve_of_eratosthenes(limit: int) -> list:
    """Generate prime numbers up to given limit using Sieve of Eratosthenes."""
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1

    return [i for i, is_prime in enumerate(primes) if is_prime]


if __name__ == "__main__":
    n = int(input("Generate primes up to: "))
    prime_list = sieve_of_eratosthenes(n)
    print(f"Prime numbers up to {n} are:\n{prime_list}")
