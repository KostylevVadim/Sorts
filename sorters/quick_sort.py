#Not ready
def part(a, start, end):
    piv = a[end]
    st_temp = start
    for i in range(start, end):
        if a[i]<piv:
            t = a[i]
            a[i] = piv
            piv = t
            st_temp+=1
    t = a[st_temp]
    a[st_temp] = piv
    piv = t
    st_temp+=1
    return st_temp

def quick_sort_req(a, start, end):
    if start<end:
        piv = part(a,start,end)
        quick_sort_req(a, start, piv-1)
        quick_sort_req(a, piv+1, end)

def quick_sort(a):
    quick_sort_req(a,0,len(a)-1)
    return a
            
