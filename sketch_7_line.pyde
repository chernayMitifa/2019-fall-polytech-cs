def setup():
    size(500, 500)
    smooth()
    background(255)
    strokeWeight(30)
    noLoop()

def draw(): 
    stroke(20)
    a=0 #сдвиг конца линии
    b=100
    i=0 
    while i<7:
        i=i+1; a=a+50; b=b+50
        line(a, 200, b, 300)
        
