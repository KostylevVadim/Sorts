def bubble_sort(a):
    x = a[:]
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i]<x[j]:
                t = x[i]
                x[i] = x[j]
                x[j] = t
    return x