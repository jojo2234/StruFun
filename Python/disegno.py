import turtle
def drawSquare(t,sz):
    for i in range(98):
        t.forward(sz)
        t.left(146) #solo questo stella
        #t.left(146) #cerchio
me=turtle.Turtle()
drawSquare(me,390)
