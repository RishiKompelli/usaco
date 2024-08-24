import math
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        True
        return
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
def allprimes(start, end):
    for num in range(start, end+1):
        if is_prime(num):
            print(num)
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
allprimes(start, end)