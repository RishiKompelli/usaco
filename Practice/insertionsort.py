def insertionsort(list_):
    for i in range(1, len(list_)):
        while list_[i-1] > list_[i] and i > 0:
            list_[i], list_[i-1] = list_[i-1], list_[i]
            i -= 1
    print(list_)
list_ = [2, 9, 7, 1, 5, 3, 6, 4, 8]
insertionsort(list_)