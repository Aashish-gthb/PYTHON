from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POSITION = [(0,0) , (-20,0) , (-40,0)]
MOVE_FORWARD = 20

class Snake:
    def __init__(self):   
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
       
    def  create_snake(self):
        for positions in STARTING_POSITION:
            self.add_segments(positions)
            

    def add_segments(self,positions):
        new_segment = Turtle(shape="square")
        new_segment.color("cyan")
        new_segment.penup()
        new_segment.goto(positions)
        self.segments.append(new_segment)   

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,0)
        self.segments.clear()
        self.create_snake()
        self.head =self.segments[0]
            

    def extend(self):
        self.add_segments(self.segments[-1].position())  


    def move(self):
        
        for seg_num in range(len(self.segments)- 1, 0 ,-1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_FORWARD)    


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)       
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)  
    def right(self):
        if self.head.heading() != LEFT:  
            self.head.setheading(RIGHT)      
    def left(self):
        if self.head.heading() != RIGHT:   
            self.head.setheading(LEFT)
   