import itertools
import operator
print(1, *itertools.accumulate((range(1, int(input()) + 1)), operator.mul))
