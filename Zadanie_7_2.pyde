from collections import namedtuple

Circ = namedtuple("Circ", ("translate", "scale", "line"))

def setup():
    size(600, 600)
    noLoop()

def draw():

   background(100)
   smooth()
   strokeWeight(75)
   stroke(200)

   translate(width/2, height/2 - 100)
   line(-150,0,150,0)

   translate(0, 100)
   scale(0.66, 0.66)
   line(-150,0,150,0)
 
   translate(0, 100)
   scale(0.66, 0.66)
   line(-150,0,150,0)
