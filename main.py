from sorters.bubble_sort import bubble_sort
from sorters.shaker_sort import shaker_sort
from sorters.insertions_sort import isertions_sort
from sorters.selections_sort import selections_sort
from sorters.merge_sort import merge_sort

import random
from decorators import Decorators, decorator
from list_defender import List_Defender
import asyncio
a = []
b = []

for i in range(1000000):
    a.append(random.randint(0,1000000))
    b.append(random.randint(0,1000000))
x= bubble_sort(a)
y = bubble_sort(b)




    


