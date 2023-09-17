from sorters.bubble_sort import bubble_sort
from sorters.shaker_sort import shaker_sort
from sorters.insertions_sort import isertions_sort
from sorters.selections_sort import selections_sort
from sorters.merge_sort import merge_sort


from decorators import Decorators, decorator
from list_defender import List_Defender
a = input().split()
b = input().split()
a = list(map(lambda x: int(x),a))
b = list(map(lambda x: int(x),b))
try:
    with List_Defender(a) as a_temp:
        for i in range(len(a_temp)):
            a_temp[i]+=b[i]
except Exception as e:
    print(e)
print(a)



    


