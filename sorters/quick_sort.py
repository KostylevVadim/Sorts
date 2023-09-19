import random
def quick_sort(data):
    if len(data) <= 1:
        return data
    else:
        q = data[len(data)//2]

    l_nums = [n for n in data if n < q]
    e_nums = [q] * data.count(q)
    b_nums = [n for n in data if n > q]
    return quick_sort(l_nums) + e_nums + quick_sort(b_nums)
