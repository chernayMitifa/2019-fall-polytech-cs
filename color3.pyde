from collections import namedtuple
MyEllipse = namedtuple("MyEllipse", ("weight", "color", "coords"))

More_ellipse =  (
          MyEllipse(color=(94, 206, 40, 50),
                 weight=50,
                 coords=(250, 400, 100, 100)),
          MyEllipse(color=((94, 206, 40, 100)),
                 weight=50,
                 coords=(250, 300, 100, 100)),
          MyEllipse(color=(94, 206, 40, 150),
                 weight=50,
                 coords=(250, 200, 100, 100)),
          MyEllipse(color=(94, 206, 40, 200),
                 weight=50,
                 coords=(250, 100, 100, 100))
)
def setup():
    size(500, 500)
    smooth()
    noLoop()
    
def draw():
    background(50)

    for MyEllipse in More_ellipse:
        stroke(*(MyEllipse.color)) # (136, 29, 203) -> 136, 29, 203
        strokeWeight(MyEllipse.weight)
        ellipse(*(MyEllipse.coords))
