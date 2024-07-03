import turtle as tosba
import random as rd

pencere = tosba.Screen()
pencere.setup(width=500, height=500)
pencere.title("Sanat Eseri")

tosbik = tosba.Turtle()
tosbik.shape("turtle")
tosbik.speed(15)

renkler=["red", "yellow","blue","violet", "purple", "green"]
pencere.bgcolor("black")

for i in range(50):
    tosbik.forward(100)
    tosbik.color(renkler[rd.randint(0,5)])
    tosbik.left(90+i)

pencere.mainloop()