
def heapify(li):
    li.insert(0, None)
    for i in range(len(li)-1, 1, -1):
        height = 1
        index = i
        while index//2 != 1:
            index = index//2
            height+=1
        x = i
        for j in range(height):
            if li[x] < li[x//2]:
                temp = li[x]
                li[x] = li[x//2]
                li[x//2] = temp
                x = x//2
    li.pop(0)


def insert(x, heap):
    heap.append(x)


def deleteMin(heap):
    if heap[0] == None:
        min_index = 1
    else:
        min_index = 0
    for i in range(1, len(heap)):
        if heap[i] == None:
            continue
        elif heap[min_index] > heap[i]:
            min_index = i
    return heap.pop(min_index)


def heapSort(li):
    heap = []
    for i in range(len(li)):
        heap.append(deleteMin(li))
    return heap


li = [6, 11, 9, 1, 3, 7, 20, 2, 8, 8, 5]
heap = heapSort(li)
print(li)
print(heap)


