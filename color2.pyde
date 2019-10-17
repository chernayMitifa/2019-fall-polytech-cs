from collections import namedtuple
MyLine = namedtuple("MyLine", ("weight", "color", "coords"))

lines =  (
          MyLine(color=(94, 206, 40, 50),
                 weight=140,
                 coords=(100, 100, 400, 100)),
          MyLine(color=((94, 206, 40, 100)),
                 weight=140,
                 coords=(100, 200, 400, 200)),
          MyLine(color=(94, 206, 40, 150),
                 weight=140,
                 coords=(100, 300, 400, 300)),
          MyLine(color=(94, 206, 40, 200),
                 weight=140,
                 coords=(100, 400, 400, 400))
)
def setup():
    size(500, 500)
    smooth()
    noLoop()
    
def draw():
    background(50)

    for my_line in lines:
        stroke(*(my_line.color)) # (136, 29, 203) -> 136, 29, 203
        strokeWeight(my_line.weight)
        line(*(my_line.coords))
