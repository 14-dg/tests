a=[[1, 1, 3, 5, 1, 3, 5], [1, 1, 3, 5, 1, 3, 5], [1, 1, 3, 5, 1, 3, 5], [1, 1, 3, 5, 1, 3, 5]]

def get_relavent_pos():  
    i=0
    x=0
    for target in a:
        i+=1
        x=0
        for goal in a:
            x+=1
            if target == goal and x != i:
                a.pop(x-1)
    return a
print(get_relavent_pos())