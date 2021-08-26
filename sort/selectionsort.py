#선택정렬 O(N^2) 시간복잡도, O(N) 공간복잡도

def selectionsort(lst): #오름차순
    n = len(lst)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if lst[min] > lst[j]: #최솟값 갱신
                min = j
        lst[i],lst[min] = lst[min],lst[i] #리스트 정렬 안 된 거 가장 왼쪽하고, 그 오른쪽의 원소 중 가장 작은 애하고 스왑
    return lst
