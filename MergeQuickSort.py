def mergesort(lista):
    tmp = [None] * len(lista)
    start = 0
    end = len(lista) - 1
    mergesort_aux(lista, start, end, tmp)


def mergesort_aux(lista, start, end, tmp):
    if start < end:
        mid = (start + end) // 2

        mergesort_aux(lista, start, mid, tmp)
        mergesort_aux(lista, mid + 1, end, tmp)

        merge_list(lista, start, mid, end, tmp)

        for i in range(start, end + 1):
            lista[i] = tmp[i]


def merge_list(lista, start, mid, end, tmp):
    i = start
    j = mid + 1

    for k in range(start, end + 1):
        if i > mid:
            tmp[k] = lista[j]
            j += 1
        elif j > end:
            tmp[k] = lista[i]
            i += 1
        elif lista[i] <= lista[j]:
            tmp[k] = lista[i]
            i += 1
        else:
            tmp[k] = lista[j]
            j += 1


lista = [3, 6, 1, 7, 2, 4, 6, 2]
mergesort(lista)
print(lista)


def quicksort(lista):
    start = 0
    end = len(lista) - 1
    quicksort_aux(lista, start, end)


def quicksort_aux(lista, start, end):
    if start < end:
        boundary = partition(lista, start, end)
        quicksort_aux(lista, start, boundary - 1)
        quicksort_aux(lista, boundary + 1, end)


def partition(lista, start, end):
    mid = (start + end) // 2
    pivot = lista[mid]
    swap(lista, start, mid)
    index = start
    for k in range(start + 1, end + 1):
        if lista[k] < pivot:
            index += 1
            swap(lista, index, k)
    swap(lista, index, start)
    return index


def swap(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]


lista = [3, 6, 1, 7, 2, 4, 6, 2]
quicksort(lista)
print(lista)












