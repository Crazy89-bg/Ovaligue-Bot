import turtle
from tkinter import *
import webbrowser


def dipsun_discord():
    webbrowser.open_new("https://discord.gg/pBHJ4vKnKZ")


def continue_to_page2():
    second = Tk()
    second.title("Ovaligue V1.0.0")
    second.iconbitmap("Ovaligue.ico")
    second.geometry("1080x720")
    second.maxsize(1080, 720)
    second.minsize(1080, 720)
    second.config(background='#f8b84d')
    second.mainloop()


def window():
    window = Tk()
    window.title("Ovaligue V1.0.0")
    window.iconbitmap("Ovaligue.ico")
    window.geometry("1080x720")
    window.maxsize(1080, 720)
    window.minsize(1080, 720)

    window.config(background='#f8b84d')

    frame = Frame(window, bg='#f8b84d')

    label_title = Label(frame, text="Bienvenue sur le pannel Ovaligue", font=("Courrier", 40), bg="#f8b84d", fg="#8a102d")
    label_title.pack()

    label_subtitle = Label(frame, text="Développé par Cwazy", font=("Arial", 20), bg="#f8b84d", fg="#8a102d")
    label_subtitle.pack()

    dipsun_button = Button(frame, text="Dipsun discord", font=("Arial", 20), bg="#8a102d", fg="#f8b84d", command=dipsun_discord)
    dipsun_button.pack(pady=25, fill=X)
    frame.pack(expand="YES")

    continue_button = Button(frame, text="Continue", font=("Courrier", 17), bg="#8a102d", fg="#f8b84d",command=continue_to_page2)
    continue_button.pack()
    frame.pack(expand="YES")
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


