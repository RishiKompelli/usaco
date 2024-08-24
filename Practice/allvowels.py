vowels = ['a', 'e', 'i', 'o', 'u']
def allvowels(string):
    for i in string:
        if i in vowels:
            print(i)
allvowels(input())