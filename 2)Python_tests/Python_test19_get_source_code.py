import inspect
from queue import Queue
import matplotlib
import math

#inspect funktioniert bei allem außer built-in-methods
#funktioniert sogar bei inspect, aber nicht bei math weil math aus python stammt

print(inspect.getsource(inspect))
print(inspect.getabsfile(inspect))

class P(Queue):
    def __init__(self, maxsize):
        super().__init__(maxsize)
        print(maxsize)

P(10)