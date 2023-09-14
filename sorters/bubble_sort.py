def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i]>a[j]:
                t = a[i]
                a[i] = a[j]
                a[j] = t
    return a