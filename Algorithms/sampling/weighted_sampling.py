import random
import bisect
from collections import defaultdict

array = [4, 12, 5, 9, 10]
probab = []
cum_sum = 0
for i in range(len(array)):
    cum_sum += array[i]
    probab.append(cum_sum)

for i in range(len(probab)):
    probab[i] = probab[i] / cum_sum

hashmap = defaultdict(int)
for i in range(40):
    num = random.uniform(0, 1)
    for i, pro in enumerate(probab):
        if pro >= num:
            # print(num, i, array[i])
            hashmap[i] += 1
            break
print(sorted(hashmap.items()))

