from tkinter import *
entry = ""


def annouce():
    def return_annoucement():
        entry = annoucement.get()
        annoucement.delete(0, END)
        print(entry)
        return entry
    window = Tk()
    window.title("Ovaligue Annoucemment")
    window.geometry("720x350")
    window.maxsize(720, 350)
    window.minsize(720, 350)

    window.iconbitmap("Ovaligue.ico")
    window.config(background='#f8b84d')

    frame = Frame(window, bg="#f8b84d")
    width = 300
    height = 300
    image = PhotoImage(file="Ova.png").zoom(4).subsample(32)
    canvas = Canvas(frame, width=width, height=height, bg="#f8b84d", bd=0, highlightthickness=0)
    canvas.create_image(width/2,height/2, image=image)
    canvas.grid(row=0, column=0, sticky=W)

    right_frame = Frame(frame, bg="#f8b84d")

    label_title = Label(right_frame, text="Faire une annonce", font=("Helvetica", 30), bg="#f8b84d", fg="#8a102d")
    label_title.pack()
    annoucement = Entry(right_frame, font=("Helvetica", 20), bg="white", fg="black")
    annoucement.pack()

    envoyer_infos = Button(right_frame, text="Envoyer", font=("Helvetica", 10), bg="#f8b84d", fg="#8a102d", command=return_annoucement)
    envoyer_infos.pack()

    right_frame.grid(row=0, column=1, sticky=W)

    frame.pack(expand=YES)

    window.mainloop()
    pass
