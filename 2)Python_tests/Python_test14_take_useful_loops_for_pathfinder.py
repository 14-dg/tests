def found():
    print("found")            
    self.x_find = self.goal2[0] - self.goal1[0]
    self.y_find = self.goal1[1] - self.goal2[1]

    self.vec_find = []            
    self.vec_find.extend([self.x_find/self.distance, self.y_find/self.distance])
    
    self.way.append([self.x_find, self.y_find])

    #print(self.vec_find)
    
    find_way(1)
    find_way(2)

def find_way(which):
    #pass            
    if found_way()==False and which ==1:
        a=self.vec_find[0]                
        #print(self.vec_find)
        #print(a)
        if a>=0:
            for i in range(0, round(a, None)):
                time.sleep(0.3)
                if alternative_route()==False:
                    self.x_find +=self.distance                   
                    self.way.append([self.x_find, self.y_find]) 
                    go("right")     
                else:
                    pass                                           
                pygame.draw.rect(screen , ORANGE, (self.current_pos[0], self.current_pos[1], height, height))
                
        else:
            for i in range(0, round(a, None), -1):
                time.sleep(0.3)
                if alternative_route()==False:
                    self.x_find +=self.distance                   
                    self.way.append([self.x_find, self.y_find]) 
                    go("left")     
                else:
                    pass               
                pygame.draw.rect(screen , ORANGE, (self.current_pos[0], self.current_pos[1], height, height))
                

    if found_way()==False and which ==2:
        b=self.vec_find[1]
        #print(self.vec_find)
        #print(b)
        if b>=0:
            for x in range(0, round(b, None)):
                time.sleep(0.3)
                if alternative_route()== False:
                    self.y_find +=self.distance                   
                    self.way.append([self.x_find, self.y_find])
                    go("up")  
                else:
                    pass   
                pygame.draw.rect(screen , ORANGE, (self.current_pos[0], self.current_pos[1], height, height))
                
        else:
            for x in range(0, round(b, None), -1):
                time.sleep(0.3)
                if alternative_route()== False:
                    self.y_find +=self.distance                   
                    self.way.append([self.x_find, self.y_find])
                    go("down")  
                else:
                    pass                             
                pygame.draw.rect(screen , ORANGE, (self.current_pos[0], self.current_pos[1], height, height))
                

    elif found_way==True:
        pygame.draw.rect(screen , GREEN, (self.goal2[0], self.goal2[1], height, height))

def alternative_route():
    
    if go("up") == self.obstacle:
        print("...")
        go("down")
        go("left")
        return True

    elif go("down") == self.obstacle:
        go("up")
        go("left") 
        return True

    elif go("right") == self.obstacle:
        go("left")
        go("up")
        return True

    elif go("left") == self.obstacle:
        go("right")
        go("up")
        return True
    else:
        return False

def go(which):
    if which=="up":
        self.current_pos[1]-=self.distance
    elif which=="right":
        self.current_pos[0]+=self.distance
    elif which=="down":
        self.current_pos[1]+=self.distance
    elif which=="left":
        self.current_pos[0]-=self.distance
    return self.current_pos

def found_way():
    if self.vec_find[0]==0 and self.vec_find[1]==0:
        print("done")
    else:
        return False






for z in self.next_goal:
                for i in range(1, len(self.way)):
                    for x in self.way:
                        #print(z)
                        if x[1]==self.duration-i and x[0] != z[0]:
                            #print(x)
                            #print(self.goal2)
                            self.way.remove(x)
                        elif x[1]==self.duration and x[0] == z[0]:
                            get_relavent_pos("next_goal", x)
                            self.next2+=1