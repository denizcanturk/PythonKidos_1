import turtle as tosba
import random as rd

renkler = ["blue", "red", "yellow", "purple", "violet","green"]
pencere = tosba.Screen()
pencere.setup(width = 500, height = 500)
pencere.bgcolor("black")
pencere.title("Daireler")
tosbik = tosba.Turtle()
tosbik.shape("turtle")
tosbik.speed(50)
tosbik.color("white")

for i in range(150):
    tosbik.circle(10+i)
    tosbik.right(10)
    tosbik.color(renkler[rd.randint(0,5)])

pencere.mainloop()