n = int(input("Enter the value of n: "))
sum = 0
for num in range(1, n + 1):
    if num % 7 == 0 and num % 9 == 0:
        sum += num
print(f"The sum of all numbers divisible by 7 and 9 from 1 to {n} is: {sum}")
