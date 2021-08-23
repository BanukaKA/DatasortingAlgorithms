# Python program for Insertion sort


def insertionSort(arr):
    
    for keys in range(1, len(arr)):

        key = arr[keys]

        vals = keys - 1
        while vals >= 0 and key < arr[vals]:
            arr[vals + 1] = arr[vals]
            vals -= 1
        arr[vals + 1] = key



arr = [12, 11, 13, 54, 65, 45, 87, 34, 55, 98, 67, 85, 76]
insertionSort(arr)
print("Sorted array is:")
for keys in range(len(arr)):
    print("%d" % arr[keys])
    
#contributed by BanukaAmbegoda