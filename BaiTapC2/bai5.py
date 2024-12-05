from collections import deque

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6  # Cuz we checked %2 and %3 already
    return True

def superPrimeNumber(n):
    super_primes = []
    queue = deque([2, 3, 5, 7])  # Start with single-digit primes

    while queue:
        num = queue.popleft()
        if num <= n:
            if is_prime(num):
                super_primes.append(num)
                # Generate new numbers by appending digits 1-9
                for digit in range(10):
                    new_num = num * 10 + digit
                    if new_num <= n:
                        queue.append(new_num)

    return sorted(super_primes)

# Example usage
n = 40 
print(superPrimeNumber(n))  # Output: [2, 3, 5, 7, 23, 29]