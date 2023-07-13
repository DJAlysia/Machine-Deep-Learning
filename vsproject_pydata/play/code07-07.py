import turtle
import random
import math

myTurtle, tX, tY, tColor, tSize, tShape = [None] * 6
shapeList=[]
playerTurtles=[]
swidth, sheight = 500, 500

def find_line_angle(x, y):
    distance = math.sqrt(x**2 + y**2)
    angle_radians = math.atan(y / x)
    angle_degrees = math.degrees(angle_radians)
    if x < 0 and y < 0:  # 3사분면
        angle_degrees += 180
    elif x < 0 and y > 0: # 1사분면
        angle_degrees -= 180
    elif x < 0:  # 2사분면
        angle_degrees += 90
    return angle_degrees
    

if __name__ =="__main__":
    turtle.title('거북 리스트 활용')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    
    shapeList=turtle.getshapes()
    print(shapeList)
    for i in range(0, 100):
        random.shuffle(shapeList)
        myTurtle = turtle.Turtle('turtle')
        tX = random.randrange(-swidth / 2, swidth / 2)
        tY = random.randrange(-sheight / 2, sheight / 2)
        r = random.random(); g = random.random(); b = random.random()
        tSize = random.randrange(1, 5)
        playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])
        
    for tList in playerTurtles:
        myTurtle = tList[0]
        angle_degrees = find_line_angle(tList[1], tList[2])
        myTurtle.setheading(angle_degrees)  # 거북이의 방향을 설정
        myTurtle.speed(0)
        myTurtle.color((tList[4], tList[5], tList[6]))
        myTurtle.pencolor((tList[4], tList[5], tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.goto(tList[1], tList[2])