def sieve_of_eratosthenes(n):
    primes = set(range(2, n + 1))
    
    for i in range(2, int(n ** 0.5) + 1):
        if i in primes:
            multiples = set(range(i * i, n + 1, i))
            primes.difference_update(multiples)
            
    return sorted(primes)

print(sieve_of_eratosthenes(50))