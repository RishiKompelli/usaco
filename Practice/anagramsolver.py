word = input("Enter a word: ")
anagram = input("Enter an anagram: ")
def anagramsolver(word, anagram):
    for i in range(len(word)):
        for j in range(len(anagram)):
            if word[i] == anagram[j]:
                print(word[i])
anagramsolver(word, anagram)