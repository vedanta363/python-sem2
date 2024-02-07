#Python program to generate the prime numbers from 1 to N

def generate_primes_up_to_n(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

upper_limit = int(input("Enter an upper limit (N): "))

result = generate_primes_up_to_n(upper_limit)
print(f"Prime numbers up to {upper_limit}: {result}")
