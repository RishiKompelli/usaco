import math
def primeorcomposite(num):
    if num < 2:
        return "Neither prime nor composite"
    if num == 2:
        print("Prime")
        return
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            print("Composite")
            return
    print("Prime")
primeorcomposite(int(input()))