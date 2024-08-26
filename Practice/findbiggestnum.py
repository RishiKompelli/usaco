list_ = [2, 9, 7, 1, 5, 3, 6, 4, 8, 2, 9, 7, 1, 5, 3, 6, 4, 8, 12, 11, 15, 16, 21, 100, 101, 23, 40, 52, 26, 7, 3, 75, 8, 897, 45, 3, 45, 67, 95, 34, 59, 35, 96]
def bubblesort(list_):
    n = len(list_)
    for i in range(n):
        for j in range(0, n-i-1):
            if list_[j] > list_[j+1]:
                list_[j], list_[j+1] = list_[j+1], list_[j]
    return list_
def insertionsort(list_):
    for i in range(1, len(list_)):
        key = list_[i]
        j = i-1
        while j >= 0 and key < list_[j]:
            list_[j+1] = list_[j]
            j -= 1
        list_[j+1] = key
    return list_
def quicksort(list_):
    if len(list_) <= 1:
        return list_
    pivot = list_[0]
    less = [x for x in list_ if x < pivot]
    greater = [x for x in list_ if x > pivot]
    equal = [x for x in list_ if x == pivot]
    return quicksort(less) + equal + quicksort(greater)
def mergesort(list_):
    if len(list_) > 1:
        mid = len(list_) // 2
        L = list_[:mid]
        R = list_[mid:]
        mergesort(L)
        mergesort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list_[k] = L[i]
                i += 1
            else:
                list_[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            list_[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            list_[k] = R[j]
            j += 1
            k += 1
    return list_
bubblesort(list_)
insertionsort(list_)
quicksort(list_)
mergesort(list_)