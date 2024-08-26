arr1 = input("Enter the first array: ").split()
arr2 = input("Enter the second array: ").split()
def commonelement(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                print(arr1[i])
commonelement(arr1, arr2)