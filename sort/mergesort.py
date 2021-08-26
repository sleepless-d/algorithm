#병합정렬 O(NlogN) 시간복잡도, O(N) 공간복잡도

def mergesort(lst):
    if len(lst) == 1: return lst
    elif len(lst) == 2:
        if lst[0] <= lst[1]:
            return lst
        else:
            return [lst[1],lst[0]]
    else:
        leftlst = lst[:(len(lst)//2)+len(lst)%2]
        rightlst = lst[len(lst)-(len(lst)//2):]
        leftlst = mergesort(leftlst)
        rightlst = mergesort(rightlst)
        sorted_lst = []
        while(len(leftlst) or len(rightlst)):
            if len(leftlst) == 0:
                sorted_lst += rightlst
                break
            elif len(rightlst) == 0:
                sorted_lst += leftlst
                break
            if leftlst[0] <= rightlst[0]:
                sorted_lst.append(leftlst[0])
                leftlst = leftlst[1:]
            else:
                sorted_lst.append(rightlst[0])
                rightlst = rightlst[1:]
        return sorted_lst
