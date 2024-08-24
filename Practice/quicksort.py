list_ = [2, 9, 7, 1, 5, 3, 6, 4, 8]
def quicksort(list_):
    if len(list_) <= 1:
        return list_
    pivot = list_[0]
    less = [x for x in list_ if x < pivot]
    greater = [x for x in list_ if x > pivot]
    equal = [x for x in list_ if x == pivot]
    return quicksort(less) + equal + quicksort(greater)
sorted_list = quicksort(list_)
print(sorted_list)