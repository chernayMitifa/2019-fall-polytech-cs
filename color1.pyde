from collections import namedtuple
MyLine = namedtuple("MyLine", ("weight", "color", "coords")) #создаем сборку

        
lines =  (
           MyLine(color=(136, 29, 203),
                 weight=110,
                 coords=(100, 350, 400, 350)),
           MyLine(color=(203, 29, 163),
                 weight=60,
                 coords=(100, 250, 400, 250)),
           MyLine(color=(203, 29, 29),
                 weight=110,
                 coords=(100, 150, 400, 150))
)
 
def setup():
    size(500, 500)
    smooth()
    noLoop()

def draw():
    background(0)
    
    for my_line in lines:
        stroke(*(my_line.color)) # (136, 29, 203) -> 136, 29, 203
        strokeWeight(my_line.weight)
        line(*(my_line.coords))
        
