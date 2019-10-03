windowWidth = int(1000)
windowHeight = int(1000)
ellipseSize = int(200)
 
def setup():
    size(windowWidth , windowHeight)
    smooth()
    background(255)
    fill(50, 80)
    stroke(100)
    strokeWeight(3)
    noLoop()
def draw():
   ellipse(windowWidth/2, windowHeight/2 - ellipseSize/2,
ellipseSize , ellipseSize)
   ellipse(windowWidth/2 - ellipseSize/2, windowHeight/2,
ellipseSize , ellipseSize)
   ellipse(windowWidth/2 + ellipseSize/2, windowHeight/2,
ellipseSize , ellipseSize)
   ellipse(windowWidth/2, windowHeight/2 + ellipseSize/2,
ellipseSize , ellipseSize)
