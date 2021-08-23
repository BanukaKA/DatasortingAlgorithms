#Python code for bubble sort
def BSort(list):
    for item in list:
        for units in range(len(list)):
            if units == 0:
                continue
            if list[units-1] > list[units]:
                list[units-1], list[units] = list[units], list[units-1]
    return list


List = [23, 43, 25, 54, 65, 56, 27, 98, 34, 76, 87, 89, 46]
print(BSort(List))
#Contributed by BanukaAMbegoda
