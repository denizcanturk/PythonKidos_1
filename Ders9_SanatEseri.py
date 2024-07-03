import turtle as tosba
import random as rd

pencere = tosba.Screen()
pencere.setup(width=500, height=500)
pencere.title("Sanat Eseri")

tosbik = tosba.Turtle()
tosbik.shape("turtle")
tosbik.speed(15)

for i in range(2000):
    adim= rd.randint(0,10)
    aci = rd.randint(1,360)
    tosbik.forward(adim)
    tosbik.right(aci)

pencere.mainloop()