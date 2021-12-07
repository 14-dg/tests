import Python_test5 as pt5

def primesum(x):
    primes= list()
    psum=0
    psum_prime=[]
    
    for i in range (1, x, 2):
        if pt5.prime(i) == True:
            primes.append(i)
    

    for i in primes:        
        if psum+i<x:         
            psum+=i
            for e in primes:
                if psum==e:
                    psum_prime.append(psum)    
        else:
            return psum_prime
    
        
               
print(primesum(100))

