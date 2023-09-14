from sorters.bubble_sort import bubble_sort
from sorters.shaker_sort import shaker_sort
from sorters.insertions_sort import isertions_sort
from sorters.selections_sort import selections_sort
from sorters.merge_sort import merge_sort
from sorters.quick_sort import quick_sort

from decorators import Decorators

a = list(input())
a = list(map(lambda a: int(a),a))

res = Decorators.decorator_reverse(bubble_sort)
print(res(a))



    


