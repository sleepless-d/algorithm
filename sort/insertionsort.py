#삽입정렬 O(N^2) 시간복잡도, O(N) 공간복잡도

def insertionsort(lst):
    n = len(lst)
    for i in range(1,n):
        j = i
        while(j > 0 and lst[j-1] > lst[j]):
            lst[j-1],lst[j] = lst[j],lst[j-1]
            j -= 1
    return lst
