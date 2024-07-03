import turtle as tosba

pencere=tosba.Screen()
pencere.setup(width=500, height=500)
pencere.title("Canım Tosbam")

tosbik = tosba.Turtle()
tosbik.shape("turtle")

tosbik.speed(1)
for i in range(5):
    tosbik.forward(100)
    tosbik.right(90)

tosbik.circle(10)

pencere.mainloop()


#------------------------------

