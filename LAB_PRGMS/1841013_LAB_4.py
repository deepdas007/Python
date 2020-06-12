
#Program 1
print("\n Program 1 \n")
# sorted() method sorts the sequence either in ascending or descending and returns the sorted list.

# sort() is a method of lists class. It is very similar to sorted() function but unlike sorted()
# it returns nothing and makes changes in the original list only.

dlist = []
n = int(input("Enter no. of elements you want in the list: "))

for i in range(0,n):
    s = int(input("Enter elements in the list: "))
    dlist.append(s)

# Empty list
dlist_2 =[]
# Copy elements from list one to another.
dlist_2 = dlist.copy()

#sorted() function
print("Using sorted() function : \n")
print("Sorted list using sorted() function: ",sorted(dlist), "\n")

print("Original list: ", dlist, "\n")

# sort() function
print("Using sort() function : \n")
dlist_2.sort()
print("Sorted ist after using sort() function: ", dlist_2, "\n")

print("Original list:  ",dlist_2, "\n")

print("Program 2 \n")

# Selection sort
def selection_sort(input_list):

    for idx in range(len(input_list)):

        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
# Swap the minimum value with the compared value

        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]

# Heap sort

def heapify(InputList, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and InputList[i] < InputList[l]:
        largest = l

    if r < n and InputList[largest] < InputList[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        InputList[i], InputList[largest] = InputList[largest], InputList[i]
        heapify(InputList, n, largest)


def heapSort(InputList):
    n = len(InputList)

    # Build max heap
    for i in range(n // 2, -1, -1):
        heapify(InputList, n, i)

    for i in range(n - 1, 0, -1):
        # Swap
        InputList[i], InputList[0] = InputList[0], InputList[i]

        # Heapify root element
        heapify(InputList, i, 0)


f =1
list = []
n = int(input("Enter no. of elements: "))

for i in range(0, n):
    s = int(input("Enter elements in the list: "))
    list.append(s)

while f > 0:

        print("Select the program you want to perform: ")
        print("\n 1. Sequential sort")
        print("\n 2. Heap sort")

        ch = int(input("Enter the choice: "))

        if ch in (1, 2):

            if ch == 1:
                print("Original list: ", list)
                selection_sort(list)
                print("Sorted list: ",list)

            elif ch == 2:
                print("Original list: ", list)
                heapSort(list)
                print("Sorted list :", list)
            break