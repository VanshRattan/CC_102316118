def sumodd(n):
    totalsum = 0
    for num in range(1, n + 1, 2):
        totalsum += num
    return totalsum

n = int(input("Enter the value of n: "))
print(f"The sum of all odd numbers from 1 to {n} is: {sumodd(n)}")
