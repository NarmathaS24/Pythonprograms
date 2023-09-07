# Function to check if a number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Loop to check prime numbers up to 10,000
for num in range(2, 10001):
    if is_prime(num):
        print(num)
