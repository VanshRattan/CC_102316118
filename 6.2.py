def sumprime(n):
    prime_sum = 0
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_sum += num
    return prime_sum

n = int(input("Enter the value of n: "))
print(f"The sum of all prime numbers from 1 to {n} is: {sumprime(n)}")
