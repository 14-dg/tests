import time

def timer(f):
    def wrapper():
        start=time.time()
        f()        
        total=time.time()-start
        return total
    return wrapper

@timer
def test():
    for _ in range(10000000):
        pass

print(test())