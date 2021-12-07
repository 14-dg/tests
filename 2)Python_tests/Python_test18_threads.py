import threading
import time

def compute(a, b, c):
    print("here")
    while a<100:
        a, b= b ,a+b
        c.append(a)
    print(c)

z=threading.Timer(10, compute, (1, 1, [], ))
z.start()