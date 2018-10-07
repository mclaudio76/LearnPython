
def merge(listA:list, listB:list) -> list:
    result  = list()
    while len(listA) * len(listB) > 0:
        targetList = listA if listA[0] <= listB[0] else listB
        result.append(targetList.pop(0))
    result.extend(listA)
    result.extend(listB)
    return result

def mergeSort(lst: list) -> list:
    if len(lst) <= 1:
        return lst
    idx = int(len(lst) / 2)
    sxSubList = lst[:idx]
    dxSubList = lst[idx:]
    return merge(mergeSort(sxSubList) , mergeSort(dxSubList))

def qsort(l: list) -> list:
    if len(l) <= 1:
        return l
    idxPivot = int(len(l) / 2)
    pValue   = l[idxPivot]
    sxSubList = [x for x in l if x < pValue]
    dxSubList = [x for x in l if x > pValue]
    locList   = [x for x in l if x == pValue]
    return merge(merge(qsort(sxSubList), locList), qsort(dxSubList))
    
    

l1 = [1,8,10,7,5,3,9,4,2,6,7,10,19,15,11,13,14,17,18,12]


print(mergeSort(l1))
print(qsort(l1))