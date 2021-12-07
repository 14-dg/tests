

class birds():
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
    
    def show_picked_values(self):
        print(self.speed)
        print(self.color)


b1=birds(5, "red")
b1.show_picked_values()