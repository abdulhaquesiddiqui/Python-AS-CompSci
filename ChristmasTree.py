def drawLine(s, x):
    for i in range(0,s):
        print(" ", end = ""),
    for i in range(0, x):
        print("X", end = ""),
    print()
    return

def drawPicture():
    drawLine(5, 1)
    drawLine(4, 3)
    drawLine(3, 5)
    drawLine(2, 7)
    drawLine(1, 9)
    drawLine(4, 3)
    drawLine(4, 3)
    return
drawPicture()
