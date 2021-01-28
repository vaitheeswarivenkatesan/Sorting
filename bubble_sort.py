def bubble_sort(ls):
    n = len(ls)

    for i in range(n):
        for j in range(n - i - 1):
             if ls[j] > ls[j + 1]:
                 ls[j], ls[j + 1] = ls[j + 1], ls[j]
                 sorted = False
        if sorted:
            break

    return ls
