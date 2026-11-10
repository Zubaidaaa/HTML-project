from turtle import*
tom=Turtle()
tom.shape('turtle')
tom._tracer(0)
#tom.speed(0)
tom.penup()
tom.goto(-630,300)
tom.pendown()

def move(l):
    tom.penup()
    tom.forward(l)
    tom.pendown()

def square(c,c1,l):
    tom.color(c,c1)
    tom.begin_fill()
    for i in range (4):
        tom.forward(l)
        tom.right(90)
    tom.end_fill()

def square2():
    tom.penup()
    tom.backward(17*6)
    tom.right(90)
    tom.forward(6)
    tom.left(90)
    tom.pendown()

def nextline(tom):
    tom.penup()
    tom.left(180)
    tom.forward(160)
    tom.left(90)
    tom.forward(10)
    tom.left(90)
    tom.pendown()




for p in range (2):
    for t in range (7):
        for i in range(6):
            if i % 2 == 0:
                tom.color("green")
            else:
                tom.color("yellow green")
            
            tom.begin_fill()
            for _ in range(4):
                tom.forward(10)
                tom.left(90)
            tom.end_fill()
            move(10)
        tom.color('black', 'black') 
        tom.begin_fill() 
        for i in range(2): 
            tom.forward(30) 
            tom.left(90) 
            tom.forward(10) 
            tom.left(90) 
        tom.end_fill()
        move(30)
        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        tom.fd(10)

        for i in range(6):
            # Alternate colors
            if i % 2 == 0:
                tom.color("green")
            else:
                tom.color("yellow green")
            
            tom.begin_fill()
            for _ in range(4):
                tom.forward(10)
                tom.left(90)
            tom.end_fill()
            move(10)
        nextline(tom)
        for i in range(3):
            if i % 2 == 0:
                tom.color("yellow green")
            else:
                tom.color("green")
            
            tom.begin_fill()
            for _ in range(4):
                tom.forward(10)
                tom.left(90)
            tom.end_fill()
            move(10)

        tom.color('black', 'black') 
        tom.begin_fill() 
        for i in range(2): 
            tom.forward(30) 
            tom.left(90) 
            tom.forward(10) 
            tom.left(90) 
        tom.end_fill()
        move(30)
        for i in range(3):
            if i % 2 == 0:
                tom.color("yellow green")
            else:
                tom.color("green")
            
            tom.begin_fill()
            for _ in range(4):
                tom.forward(10)
                tom.left(90)
            tom.end_fill()
            move(10)
        tom.color('black', 'black') 
        tom.begin_fill() 
        for i in range(2): 
            tom.forward(30) 
            tom.left(90) 
            tom.forward(10) 
            tom.left(90) 
        tom.end_fill()
        move(30)
        tom.color('black', 'black') 
        tom.begin_fill() 
        for i in range(2): 
            tom.forward(30) 
            tom.left(90) 
            tom.forward(10) 
            tom.left(90) 
        tom.end_fill()

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()
        tom.fd(10)
        for i in range(3):
            # Alternate colors
            if i % 2 == 0:
                tom.color("green")
            else:
                tom.color("yellow green")
            
            tom.begin_fill()
            for _ in range(4):
                tom.forward(10)
                tom.left(90)
            tom.end_fill()

            tom.penup()
            tom.forward(10)
            tom.pendown()

        nextline(tom)
        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
    
        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        
        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        
        tom.color('green','green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        
        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)


        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()
        move(10)
        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()
        tom.penup()
        tom.fd(10)
        tom.pendown()

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        
        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        
        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        
        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        
        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        
        nextline(tom)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)


        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green','dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        nextline(tom)


        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)


        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.penup()
        tom.left(180)
        tom.fd(160)
        tom.left(90)
        tom.fd(10)
        tom.left(90)
        tom.pendown()

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)


        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)


        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        nextline(tom)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        for i in range(7):
            if i % 2 == 0:
                tom.color("dark green")
            else:
                tom.color("green")
            
            tom.begin_fill()
            for _ in range(4):
                tom.forward(10)
                tom.left(90)
            tom.end_fill()

            move(10)

        for i in range(3):
            if i % 2 == 0:
                tom.color("black")
            else:
                tom.color("dark green")
            
            tom.begin_fill()
            for _ in range(4):
                tom.forward(10)
                tom.left(90)
            tom.end_fill()

            move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        nextline(tom)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        for i in range(6):
            if i % 2 == 0:
                tom.color("green")
            else:
                tom.color("dark green")
            
            tom.begin_fill()
            for _ in range(4):
                tom.forward(10)
                tom.left(90)
            tom.end_fill()

            move(10)

        for i in range(7):
            if i % 2 == 0:
                tom.color("black")
            else:
                tom.color("dark green")
            
            tom.begin_fill()
            for _ in range(4):
                tom.forward(10)
                tom.left(90)
            tom.end_fill()

            move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        nextline(tom)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        for i in range(9):
            if i % 2 == 0:
                tom.color("black")
            else:
                tom.color("dark green")
            
            tom.begin_fill()
            for _ in range(4):
                tom.forward(10)
                tom.left(90)
            tom.end_fill()

            move(10)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        nextline(tom)

        for i in range(3):
            if i % 2 == 0:
                tom.color("black")
            else:
                tom.color("dark green")
            
            tom.begin_fill()
            for _ in range(4):
                tom.forward(10)
                tom.left(90)
            tom.end_fill()

            move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(2):
            tom.forward(50)
            tom.left(90)
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(50)

        for i in range(4):
            if i % 2 == 0:
                tom.color("black")
            else:
                tom.color("dark green")
            
            tom.begin_fill()
            for _ in range(4):
                tom.forward(10)
                tom.left(90)
            tom.end_fill()


        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(2):
            tom.forward(20)
            tom.left(90)
            tom.fd(10)
            tom.left(90)
        tom.end_fill()

        move(20)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        nextline(tom)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(2):
            tom.forward(20)
            tom.left(90)
            tom.fd(10)
            tom.left(90)
        tom.end_fill()

        move(20)

        for i in range(10):
            if i % 2 == 0:
                tom.color("dark green")
            else:
                tom.color("black")
            
            tom.begin_fill()
            for _ in range(4):
                tom.forward(10)
                tom.left(90)
            tom.end_fill()
            tom.forward(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        nextline(tom)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        for i in range(5):
            if i % 2 == 0:
                tom.color("black")
            else:
                tom.color("dark green")
            
            tom.begin_fill()
            for _ in range(4):
                tom.forward(10)
                tom.left(90)
            tom.end_fill()
            tom.forward(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(2):
            tom.forward(20)
            tom.left(90)
            tom.fd(10)
            tom.left(90)
        tom.end_fill()

        move(20)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(2):
            tom.forward(30)
            tom.left(90)
            tom.fd(10)
            tom.left(90)
        tom.end_fill()

        move(30)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        nextline(tom)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(2):
            tom.forward(30)
            tom.left(90)
            tom.fd(10)
            tom.left(90)
        tom.end_fill()

        move(30)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(2):
            tom.forward(70)
            tom.left(90)
            tom.fd(10)
            tom.left(90)
        tom.end_fill()

        move(70)
        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        nextline(tom)
        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(2):
            tom.forward(40)
            tom.left(90)
            tom.fd(10)
            tom.left(90)
        tom.end_fill()

        move(40)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(2):
            tom.forward(20)
            tom.left(90)
            tom.fd(10)
            tom.left(90)
        tom.end_fill()

        move(20)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(2):
            tom.forward(30)
            tom.left(90)
            tom.fd(10)
            tom.left(90)
        tom.end_fill()

        move(30)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)


        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        nextline(tom)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(2):
            tom.forward(20)
            tom.left(90)
            tom.fd(10)
            tom.left(90)
        tom.end_fill()

        move(20)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(2):
            tom.forward(20)
            tom.left(90)
            tom.fd(10)
            tom.left(90)
        tom.end_fill()

        move(20)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)
        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        nextline(tom)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)


        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(2):
            tom.forward(20)
            tom.left(90)
            tom.fd(10)
            tom.left(90)
        tom.end_fill()

        move(20)

        tom.color('black', 'black')
        tom.begin_fill()
        for _ in range(2):
            tom.forward(40)
            tom.left(90)
            tom.fd(10)
            tom.left(90)
        tom.end_fill()

        move(40)

        tom.color('dark green', 'dark green')
        tom.begin_fill()
        for _ in range(2):
            tom.forward(20)
            tom.left(90)
            tom.fd(10)
            tom.left(90)
        tom.end_fill()

        move(20)

        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()       
        move(10)
        tom.color('yellow green', 'yellow green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()
        move(10)
        tom.color('green', 'green')
        tom.begin_fill()
        for _ in range(4):
            tom.forward(10)
            tom.left(90)
        tom.end_fill()

        move(10)

        tom.penup()
        tom.left(90)
        tom.fd(150)
        tom.right(90)
        tom.pendown()
    tom.backward(160*7)
    tom.right(90)
    tom.forward(450)
    tom.left(90)

tom.goto(-630,150)
tom.color('dark grey','dark grey')
tom.begin_fill()
for i in range(2):
    tom.forward(160*7)
    tom.right(90)
    tom.forward(30)
    tom.right(90)
tom.end_fill()

tom.penup()
tom.right(90)
tom.forward (30)
tom.left(90)
tom.pendown()
tom.color("#a28765")
tom.begin_fill()
for i in range(2):
    tom.forward(160*7)
    tom.right(90)
    tom.forward(260)
    tom.right(90)
tom.end_fill()

tom.penup()
tom.goto(-330,-35)
tom.left(360)
tom.pendown()


tom.penup()
tom.forward(70)
tom.left(90)
tom.forward(120)
tom.right(90)
tom.pendown()

def square_panda(c,c1):
    tom.color(c,c1)
    tom.begin_fill()
    for i in range (4):
        tom.forward(6)
        tom.right(90)
    tom.end_fill()
    tom.forward(6)





def range_panda(c,c1,num):
    for i in range (num):
        square_panda(c,c1)

for s in range (2):
    for o in range (2):       
        for _ in range (2):
            for x in range(2):
                range_panda('black','black',4)
                tom.penup()
                tom.forward(6*9)
                tom.pendown()
                range_panda('black','black',3)


                tom.penup()
                tom.forward(6)
                tom.right(90)
                tom.forward(6)
                tom.left(90)
                tom.backward(6*18)
                tom.pendown()


                range_panda('black','black',18)
                tom.right(90)
                tom.forward(6)
                tom.left(90)
                tom.backward(24)
                range_panda('black','black',5)
                tom.backward(6*19)
                range_panda('black','black',5)
                range_panda('white','white',9)



                tom.penup()
                tom.backward(14*6)
                tom.right(90)
                tom.forward(6)
                tom.left(90)
                tom.pendown()


                range_panda('black','black',4)
                range_panda('white','white',11)
                range_panda('black','black',4)

                tom.penup()
                tom.backward(19*6)
                tom.right(90)
                tom.forward(6)
                tom.left(90)
                tom.pendown()
                range_panda('black','black',3)
                range_panda('white','white',13)
                range_panda('black','black',3)
                tom.penup()
                tom.backward(18*6)
                tom.right(90)
                tom.forward(6)
                tom.left(90)
                tom.pendown()
                square_panda('black','black')
                range_panda('white','white',15)
                square_panda('black','black')

                square2()


                square_panda('black','black')
                range_panda('white','white',3)
                range_panda('black','black',3)
                range_panda('white','white',5)
                range_panda('black','black',2)
                range_panda('white','white',2)
                square_panda('black','black')

                square2()

                square_panda('black','black')
                range_panda('white','white',2)
                range_panda('black','black',4)
                range_panda('white','white',4)
                range_panda('black','black',4)
                square_panda('white','white')
                square_panda('black','black')

                square2()


                square_panda('black','black')
                range_panda('white','white',2)
                range_panda('black','black',2)
                square_panda('white','white')
                square_panda('black','black')
                range_panda('white','white',4)
                square_panda('black','black')
                square_panda('white','white')
                range_panda('black','black',2)
                square_panda('white','white')
                square_panda('black','black')


                square2()


                square_panda('black','black')
                range_panda('white','white',2)
                range_panda('black','black',4)
                square_panda('white','white')
                range_panda('black','black',2)
                square_panda('white','white')
                range_panda('black','black',4)
                square_panda('white','white')
                square_panda('black','black')


                square2()

                square_panda('black','black')
                range_panda('white','white',3)
                range_panda('black','black',2)
                range_panda('white','white',3)
                square_panda('black','black')
                range_panda('white','white',2)
                range_panda('black','black',2)
                square_panda('white','white')
                square_panda('black','black')
                square_panda('dark green','dark green')
                tom.penup()
                tom.forward(6)
                tom.right(90)
                tom.forward(6)
                tom.left(90)
                tom.backward(6*17)
                tom.pendown()
                square_panda('black','black')
                range_panda('white','white',6)
                range_panda('black','black',3)
                range_panda('white','white',3)
                range_panda('black','black',2)
                square_panda('dark green','dark green')
                square_panda("#a28765","#a28765")
                range_panda('dark green','dark green',2)
                tom.penup()
                tom.forward(6)
                tom.right(90)
                tom.forward(6)
                tom.left(90)
                tom.backward(6*19)
                tom.pendown()
                square_panda('black','black')
                range_panda('white','white',10)
                range_panda('black','black',2)
                square_panda("#a28765","#a28765")
                range_panda('dark green','dark green',3)
                tom.penup()
                tom.forward(6)
                tom.right(90)
                tom.forward(6)
                tom.left(90)
                tom.backward(6*17)
                tom.pendown()
                range_panda('black','black',3)
                range_panda('white','white',6)
                square_panda('black','black')
                range_panda('dark green','dark green',4)
                tom.penup()
                tom.forward(6)
                tom.right(90)
                tom.forward(6)
                tom.left(90)
                tom.backward(6*16)
                tom.pendown()
                range_panda('black','black',10)
                range_panda('dark green','dark green',3)
                square_panda('black','black')
                square_panda("#a28765","#a28765")
                range_panda('dark green','dark green',2)
                tom.penup()
                tom.forward(6)
                tom.right(90)
                tom.forward(6)
                tom.left(90)
                tom.backward(6*18)
                tom.pendown()
                range_panda('black','black',5)
                range_panda('white','white',3)
                square_panda('black','black')
                range_panda('dark green','dark green',2)
                range_panda('black','black',4)
                range_panda("#a28765","#a28765",2)
                square_panda('dark green','dark green')
                tom.penup()
                tom.forward(6)
                tom.right(90)
                tom.forward(6)
                tom.left(90)
                tom.backward(6*20)
                tom.pendown()
                square_panda('black','black')
                range_panda('white','white',2)
                range_panda('black','black',6)
                range_panda('dark green','dark green',2)
                range_panda('black','black',5)
                tom.penup()
                tom.forward(6)
                tom.right(90)
                tom.forward(6)
                tom.left(90)
                tom.backward(6*17)
                tom.pendown()
                square_panda('black','black')
                range_panda('white','white',3)
                range_panda('black','black',6)
                square_panda('dark green','dark green')
                range_panda('white','white',2)
                range_panda('black','black',3)
                tom.penup()
                tom.forward(6)
                tom.right(90)
                tom.forward(6)
                tom.left(90)
                tom.backward(6*18)
                tom.pendown()
                range_panda('black','black',4)
                range_panda('white','white',2)
                range_panda('black','black',5)
                range_panda('white','white',4)
                range_panda('black','black',4)
                tom.penup()
                tom.forward(6)
                tom.right(90)
                tom.forward(6)
                tom.left(90)
                tom.backward(6*21)
                tom.pendown()
                range_panda('black','black',6)
                range_panda('white','white',3)
                range_panda('dark green','dark green',2)
                range_panda('white','white',4)
                range_panda('black','black',6)
                tom.penup()
                tom.forward(6)
                tom.right(90)
                tom.forward(6)
                tom.left(90)
                tom.backward(6*22)
                tom.pendown()
                range_panda('black','black',7)
                range_panda('white','white',8)
                range_panda('black','black',6)
                tom.penup()
                tom.forward(6)
                tom.right(90)
                tom.forward(6)
                tom.left(90)
                tom.backward(6*22)
                tom.pendown()
                range_panda('black','black',7)
                range_panda('white','white',7)
                range_panda('black','black',7)
                tom.penup()
                tom.forward(6)
                tom.right(90)
                tom.forward(6)
                tom.left(90)
                tom.backward(6*21)
                tom.pendown()
                range_panda('black','black',6)
                range_panda('white','white',6)
                range_panda('black','black',7)
                tom.penup()
                tom.goto(60,180)
                tom.pendown()
            tom.penup()
            tom.goto(170,0)
            tom.pendown()
        tom.penup()
        tom.goto(10,-20)
        tom.pendown()
    tom.penup()
    tom.goto(-500,20)
    tom.pendown()






tom._update()
done()