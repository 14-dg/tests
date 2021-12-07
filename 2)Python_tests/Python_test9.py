import colorama
from colorama import Fore,Back,Style,colorama_text,Cursor
colorama.init()

a=[1,1,1,1,11,3,3,3,3,3,4,55,6,6,7,78,8,9,9,0,8,6,6,66,44,3,3,6,4,67,5,42,3,5,777,5,4,67,7,8,4,4,6,43,1,4,6,7,9,9,0,10]
b=sorted(a)
print(b)
#coords first & last 6
target=7
coords=[]
current_number=0

def solution():
    x=0
    for i in b:
        if i <= target:
            x+=1
            if i==target:
                if len(coords) <2 :
                    coords.append(x)
                else:
                    coords.pop()
                    coords.append(x)                
            else:
                pass
        else:
            return coords

print(solution())

for e in b:
    if e==target:     
        print(Style.RESET_ALL)    
        print(Back.CYAN) 
        print(Fore.BLACK)
        
        print(e)
    else:
        print(Style.RESET_ALL)
        print(e)
        