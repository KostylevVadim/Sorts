def isertions_sort(a):
    for i in range(len(a)):
        j = i-1
        data = a[i]
        while a[j]>data and j>=0:
            t = a[j+1]
            a[j+1] = a[j]
            a[j] = t
            j-=1
        a[j+1] = data
    return a