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
