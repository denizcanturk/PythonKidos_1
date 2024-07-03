import turtle as tosba

pencere=tosba.Screen()
pencere.setup(width=500,height=500)
pencere.title("Canım Toosbik")

pencere.bgcolor("red")

tosbik = tosba.Turtle()
tosbik.speed(1)

tosbik.pencolor("yellow")
tosbik.forward(100)
tosbik.right(90)
tosbik.forward(100)
tosbik.penup()
tosbik.right(90)
tosbik.forward(100)
tosbik.pendown()
tosbik.forward(50)

pencere.mainloop()
