def bubblesort(list_):
    n = len(list_)
    for i in range(n):
        for j in range(0, n-i-1):
            if list_[j] > list_[j+1]:
                list_[j], list_[j+1] = list_[j+1], list_[j]
    return list_
list_ = [2, 9, 7, 1, 5, 3, 6, 4, 8]
sorted = bubblesort(list_)
print(sorted)