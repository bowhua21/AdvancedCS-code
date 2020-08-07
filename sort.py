import random

a = [10, 2, 5, 7, 3]


def selection_Sort(a):
    for i in range(len(a)):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        temp = a[i]
        a[i] = a[min]
        a[min] = temp
    return a


def insertion_Sort(a):
    for i in range(len(a)):
        for j in range(i, 0, -1):
            while a[j] < a[j - 1]:
                temp = a[j]
                a[j] = a[j - 1]
                a[j - 1] = temp
    return a


def bubble_Sort(a):
    num_swap = 1
    while num_swap != 0:
        num_swap = 0
        for i in range(0, len(a) - 1):
            if a[i] > a[i + 1]:
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
                num_swap += 1
    return a


def is_Sorted(a):
    i = 0
    while i < len(a) - 1:
        if a[i] > a[i + 1]:
            return False
        i += 1
    return True


def bogo_Sort(a):
    while is_Sorted(a) == False:
        for i in range(len(a)):
            temp = a[i]
            b = random.randint(0, len(a) - 1)
            a[i] = a[b]
            a[b] = temp
    return a


print(selection_Sort(a))
a = [10, 2, 5, 7, 3]
print(a)
print(insertion_Sort(a))
a = [10, 2, 5, 7, 3]
print(a)
print(bubble_Sort(a))
a = [10, 2, 5, 7, 3]
print(a)
print(bogo_Sort(a))
