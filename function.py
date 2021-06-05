import turtle
from tkinter import *


def window():
    window = Tk()
    window.title("Ovaligue V1.0.0")
    window.mainloop()


def chargement_turtle():
    try:
        t = turtle.Turtle()
        for i in range(0, 200):
            t.forward(i+10)
            i = i+10
            t.left(90)
            t.speed(500)
        try:
            turtle.bye()
            turtle.done()
        except:
            print("")
    except:
        print("")
    

def token():
    token = ""
    token = str(input("Entrez le token de votre bot : "))

