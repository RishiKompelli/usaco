def decimaltobinary():
    num = int(input())
    n=num.bit_length()
    binary = ""
    for i in range(n):
        power=2**(n-i-1)
        if num >= power:
            binary += "1"
            num -= power
        else:
            binary += "0"
    print(binary)
decimaltobinary()