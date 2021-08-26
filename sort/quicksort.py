#퀵정렬 O(NlogN) 시간복잡도, O(N) 공간복잡도

def quicksort(lst):
    if len(lst) == 0: return []
    elif len(lst) == 1: return lst
    pivot = len(lst)//2
    leftlst = []
    rightlst = []
    for i in range(len(lst)):
        if i == pivot: continue
        if lst[i] <= lst[pivot]:
            leftlst.append(lst[i])
        elif lst[i] > lst[pivot]:
            rightlst.append(lst[i])
    return quicksort(leftlst) + [lst[pivot]] + quicksort(rightlst)
