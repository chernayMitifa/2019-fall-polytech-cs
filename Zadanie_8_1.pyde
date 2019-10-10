def setup():
    size(600, 600)
    noLoop()

def drawMyScene(myColor = float()):
    fill(myColor)
    rect(0,50, 150, 50)
    rect(50,0, 50, 150)
def draw():
    background(20)
    smooth()
    noStroke()

    pushMatrix()
    translate(100, 0)
    rotate(PI/4) 
    drawMyScene(180)
    pushMatrix()
    translate(150, 0)
    rotate(-PI/8)
    scale(2)
    drawMyScene(220)
    popMatrix()

    pushMatrix()
    translate(455, 80)
    rotate(-PI/3)
    scale(1.4)
    drawMyScene(80)
    popMatrix()
