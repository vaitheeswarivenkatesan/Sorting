def insertion_sort(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        j =i-1
        while j >= 0 and ls[j] > key:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key

    return ls
