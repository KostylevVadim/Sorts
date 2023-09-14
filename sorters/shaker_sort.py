def shaker_sort(a):
    left = 0
    right = len(a)-1
    while left< right:
        for i in range(right):
            if a[i]>a[i+1]:
                t = a[i]
                a[i] = a[i+1]
                a[i+1] = t
        right -=1
        for i in range(right, left,-1):
            if a[i]>a[i+1]:
                t = a[i]
                a[i] = a[i+1]
                a[i+1] = t
        left+=1
    return a