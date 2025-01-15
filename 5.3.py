n = int(input("Enter the value of n: "))
prime_sum = 0
for num in range(2, n + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        prime_sum += num

print(f"The sum of all prime numbers from 1 to {n} is: {prime_sum}")
