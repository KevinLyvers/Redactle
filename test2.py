#480232000

import time
import random

nothing = 0

time1 = time.time()
for i in range(480232000):
    if i % 100000 == 0:
        print(i/480232000)
    nothing = random.random() * random.random()
    
print(time.time() - time1)