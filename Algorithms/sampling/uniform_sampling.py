import random
import bisect
from collections import defaultdict

array = [4, 12, 5, 9, 10]
probab = []
eq_probab = 1./len(array)
cum_sum = 0
for i in range(len(array)):
    cum_sum += eq_probab
    probab.append(cum_sum)

for i in range(10):
    num=random.uniform(0, 1)
    for i, pro in enumerate(probab):
        if pro>=num:
            print(num, array[i])
            break