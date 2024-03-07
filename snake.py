from turtle import Turtle

tup = [(0, 0), (-20, 0), (-40, 0)]
move_dis = 20
UP = 90
DOWN = 270
R = 0
L = 180
class Snake:

    def __init__(self):
        self.sqs = []
        self.create_snake()
        self.head = self.sqs[0]

    def create_snake(self):
        for i in tup:
            self.new_snake(i)

    def new_snake(self,i):
        sq = Turtle(shape="square")
        sq.color("white")
        sq.penup()
        sq.goto(i)
        self.sqs.append(sq)

    def extend(self):
        self.new_snake(self.sqs[-1].position())

    def reset_snake(self):
        for i in self.sqs:
            i.goto(1000,1000)
        self.sqs.clear()
        self.create_snake()
        self.head = self.sqs[0]
    def move(self):
        for i in range(len(self.sqs) - 1, 0, -1):
            newx = self.sqs[i - 1].xcor()
            newy = self.sqs[i - 1].ycor()
            self.sqs[i].goto(newx, newy)
        self.head.forward(move_dis)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != R:
            self.head.setheading(L)

    def right(self):
        if self.head.heading() != L:
            self.head.setheading(R)