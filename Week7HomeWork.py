import numpy as np
import time

z = 0

vek1 = np.random.rand(100000)
vek2 = np.random.rand(100000)

start = time.time()

# for i, j in zip(vek1, vek2):
#     z += i * j



z = np.dot(vek1, vek2)

end = time.time()


print(end- start)