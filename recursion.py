

def merge(li):
    left = []
    right = []
    if len(li) != 1:
        for i in range(0, len(li)//2):
            left.append(li[i])
        for i in range(len(li)//2, len(li)):
            right.append(li[i])
    else:
        return li
    left = merge(left)
    right = merge(right)
    for i in range(len(li)):
        if len(left) == 0 and len(right) == 0:
            return li
        elif len(left) == 0:
            li[i] = right.pop(0)
        elif len(right) == 0:
            li[i] = left.pop(0)
        elif left[0] > right[0]:
            li[i] = right.pop(0)
        elif left[0] < right[0]:
            li[i] = left.pop(0)
        else:
            li[i] = left.pop(0)
            li[i+1] = right.pop(0)
            i += 1
    return li



def merge_sort(li):
    if len(li) == 1:
        return li
    else:
        mid = (len(li))//2
        l1 = merge_sort(li[:mid])
        l2 = merge_sort(li[mid:])
        rtn = []
        while not len(l1) == 0 and not len(l2) == 0:
            if l1[0] < l2[0]:
                rtn.append(l1.pop(0))
            else:
                rtn.append(l2.pop(0))
        while len(l2) == 0 and not len(l1) == 0:
            rtn.append(l1.pop(0))
        while len(l1) == 0 and not len(l2) == 0:
            rtn.append(l2.pop(0))
        return rtn



li = [6, 11, 9, 1, 3, 7, 20, 12, 2, 8, 8, 5]
li = merge_sort(li)
print(li)

li = [6, 11, 9, 1, 3, 7, 20, 12, 2, 8, 8, 5]
li = merge(li)
print(li)
