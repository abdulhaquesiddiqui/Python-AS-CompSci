def drawLine(s, x):
    for i in range(0, s):
        print(" ", end="")
    for i in range(0, x):
        print("X", end="")
    print()
    return

def drawPicture():
    drawLine(4, 1)   
    drawLine(3, 1)
    drawLine(3, 1)
    drawLine(2, 1)
    drawLine(2, 5)   
    drawLine(2, 1)
    drawLine(2, 1)
    return

drawPicture()
