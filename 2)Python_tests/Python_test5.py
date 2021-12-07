import math

#name=input("please write your name: ")
#print ("Hello", name, "!")
#number=int(input("please write a number: "))
#print ("Here you are,", name, "!")

def prime(x):
    #assert x>1
    y = int (round(math.sqrt(x)))
    teiler = list()
    speicher = list()
   
    for i in range(1, y + 1):
        if x%i==0:
            teiler.append(i)
        else:
            pass 
    
    for element in teiler:
        add = x/element
        speicher.append(add)
    
    for element2 in speicher:
        teiler.append(element2)

    if teiler[1]==x:
        return  True#"Primzahl" , sorted(teiler)
    else: #return sorted(teiler)
        pass