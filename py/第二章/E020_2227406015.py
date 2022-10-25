import math
import random
a = random.uniform(10,50)
b = random.uniform(10,50)
x = complex(a, b)
c = math.sqrt(a**2+b**2)
d = math.degrees(math.atan(b/a))
print("{0:7.2f}{1:7.2f}{2:7.2f}".format(x,c,d))