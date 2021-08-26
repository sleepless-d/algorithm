#버블정렬 O(N^2) 시간복잡도, O(N) 공간복잡도

def bubblesort(lst): #오름차순: 낮은 것 -> 높은 것
    n = len(lst)
    for _ in range(n):
        for j in range(1,n):
            if lst[j-1] > lst[j]: #왼쪽이 더 크면 좌우 스왑
                lst[j-1],lst[j] = lst[j],lst[j-1]
    return lst
