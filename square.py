from rectangle import Rectangle # importing the class
import time
'''
making the new class
'''

class Square (Rectangle):
    
    def __init__(self,length):

        super (Square,self).__init__(length , length)

    ##############################################

        
    ##############################################
        
    def get_area(self):
        return self.length*self.length
    
    ##############################################

    def draw_shape(self):
        self.turtle.clear() 
        self.turtle.penup()
        self.turtle.goto(0,0)
        self.turtle.pendown()
        self.turtle.goto(self.length,0)
        self.turtle.goto(self.length,self.length)
        self.turtle.goto(0,self.height)
        self.turtle.goto(0,0)
        self.turtle.penup()
        time.sleep(1)
        self.has_been_drawn=True

        
    ##############################################

    def set_length(self,new_length):

        if new_length>=0 :
            self.length=new_length
            self.height=new_length
            if self.has_been_drawn :
                self.draw_shape()

    def set_height(self,new_height):

        if new_height>=0 :
            self.height=new_height
            self.length=new_height
            if self.has_been_drawn :
                self.draw_shape()
                
   ################################################
    


