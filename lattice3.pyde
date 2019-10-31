def setup():
    size(600, 500)
    smooth()
    background(255)
    strokeWeight(30)
    noLoop()

def draw():
    stroke(20, 100)
    for i in range (1,5):
        i=2*(i+1)
        line(i*50-100, 200, 50 + (i-1)*50, 300);
        line(i*50, 200, -50 + (i-1)*50, 300);
