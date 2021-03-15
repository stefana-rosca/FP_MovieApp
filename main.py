import tkinter as tk
import benutzer_func as b
import filme_func as f
import gemeinsam_func as g


def ord_func():
    u = g.comanda1(1, 1, 'a')
    film = f.film("a", 1, 1, "a", 1)

    r1 = tk.Tk()
    r1.title("Bestellungen Filme")
    r1.geometry("350x350")
    def back():
        r1.destroy()
        menu()
    def addtolist():
        Lista1 = []
        for item in varList1:
            if item.get() != "":
                Lista1.append(item.get())
        u.preluare_comanda(entry1.get(),Lista1)
        back()

    label1 = tk.Label(r1, text='ID')
    label1.config(font=('times', 10, 'bold'), pady=0)
    label1.place(x=130, y=0)
    entry1 = tk.Entry(r1)
    entry1.place(x=0, y=0)

    l1 = []
    l1 = film.extragere_filme(l1)  # lista cu filmele existente
    varList1 = []

    class Check:
        x = 30

        def __init__(self, lbl):
            self.var = tk.StringVar()
            self.cb = tk.Checkbutton(r1, text=lbl, variable=self.var, onvalue=lbl, offvalue="")
            self.cb.place(x = 0, y = Check.x)
            Check.x += 30
            varList1.append(self.var)

    for el in l1:
        Check(el)

    b1 = tk.Button(r1, text="Submit order", command=addtolist)
    b1.place(x=100, y = 30)
    r1.mainloop()


def menu():
    WIDTH = 800
    HEIGHT = 700

    root = tk.Tk()

    def menu_benutzer():
        root.destroy()
        def back():
            window.destroy()
            menu()
        def add_benutzer():
            def validare():
                om=b.benutzer("r", "h", 1)
                om.adaugare(nume.get(), prenume.get(),id.get())
                om.adaugare_in_fisier()
                s.destroy()
            s = tk.Tk()
            s.geometry("1000x700")
            button = tk.Button(s, text="Enter", command=validare)
            button.pack()

            nume=tk.Entry(s)
            label1=tk.Label(s, text="nume")
            label1.pack()
            nume.pack()
            prenume=tk.Entry(s)
            label2 = tk.Label(s, text="prenume")
            label2.pack()
            prenume.pack()
            id = tk.Entry(s)
            label3 = tk.Label(s, text="id")
            label3.pack()
            id.pack()
            s.mainloop()

        def stergere():
            def validare():
                om = b.benutzer("r", "h", 1)
                om.stergere_user(id.get())
                s.destroy()

            s = tk.Tk()
            s.geometry("1000x700")
            button = tk.Button(s, text="Enter", command=validare)
            button.pack()

            id = tk.Entry(s)
            id.pack()
            s.mainloop()

        def edit():
            def validare():
                om = b.benutzer("r", "h", 1)
                om.edit_prenume(id.get(), prenume.get())
                s.destroy()

            s = tk.Tk()
            s.geometry("1000x700")
            button = tk.Button(s, text="Enter", command=validare)
            button.pack()

            prenume = tk.Entry(s)
            prenume.pack()
            id = tk.Entry(s)
            id.pack()
            s.mainloop()

        def afisare():
            om=b.benutzer("r", "h", 1)
            l=[]
            l=om.afisare_useri(l)
            r=tk.Tk()
            text=tk.Text(r)
            for el in l:
                text.insert(tk.END, el+"\n")
            text.pack()
            r.mainloop()


        window = tk.Tk()
        window.geometry("1000x700")
        button = tk.Button(window, text="adaugare", bg="pink", fg="red", command=add_benutzer)
        button.pack()

        button1 = tk.Button(window, text="actualizare", bg="pink", fg="red", command=edit)
        button1.pack()

        button2 = tk.Button(window, text="stergere", bg="pink", fg="red", command=stergere)
        button2.pack()

        button3 = tk.Button(window, text="afisare", bg="pink", fg="red", command=afisare)
        button3.pack()

        button4 = tk.Button(window, text="back", bg="pink", fg="red", command=back)
        button4.pack()

    def menu_filme():
        root.destroy()

        def back():
            window.destroy()
            menu()

        def add_film():
            def validare():
                film = f.film("r",1, 1, "h", 1)
                film.adaugare_film(titlu.get(), an.get(),nota.get(), pret.get(), actor.get())
                film.adaugare_in_fisier()
                s.destroy()

            s = tk.Tk()
            s.geometry("1000x700")
            button = tk.Button(s, text="Enter", command=validare)
            button.pack()

            titlu = tk.Entry(s)
            label1 = tk.Label(s, text="titlu")
            label1.pack()
            titlu.pack()

            an = tk.Entry(s)
            label2 = tk.Label(s, text="an")
            label2.pack()
            an.pack()

            nota = tk.Entry(s)
            label3 = tk.Label(s, text="nota")
            label3.pack()
            nota.pack()

            pret = tk.Entry(s)
            label5 = tk.Label(s, text="actor")
            label5.pack()
            pret.pack()

            actor = tk.Entry(s)
            label4 = tk.Label(s, text="pret")
            label4.pack()
            actor.pack()
            s.mainloop()


        def edit():
            def validare():
                film = f.film("r", 1, 1, "h", 1)
                film.modificare_pret(titlu.get(), pret.get())
                s.destroy()

            s = tk.Tk()
            s.geometry("1000x700")
            button = tk.Button(s, text="Enter", command=validare)
            button.pack()

            titlu = tk.Entry(s)
            titlu.pack()
            pret = tk.Entry(s)
            pret.pack()
            s.mainloop()

        def afisare():
            film = f.film("r", 1, 1, "h", 1)
            l = []
            l = film.afisare_filme(l)
            r = tk.Tk()
            text = tk.Text(r)
            for el in l:
                text.insert(tk.END, el + "\n")
            text.pack()
            r.mainloop()

        window = tk.Tk()
        window.geometry("1000x700")
        button = tk.Button(window, text="adaugare", bg="pink", fg="red", command=add_film)
        button.pack()

        button1 = tk.Button(window, text="actualizare", bg="pink", fg="red", command=edit)
        button1.pack()

        button2 = tk.Button(window, text="afisare", bg="pink", fg="red", command=afisare)
        button2.pack()

        button3 = tk.Button(window, text="back", bg="pink", fg="red", command=back)
        button3.pack()

    def menu_gemeinsam():
        root.destroy()

        def back():
            window.destroy()
            menu()

        def comandare():
            window.destroy()
            ord_func()

        def afisare():
            com = g.comanda1(1, 1, "a")
            l = []
            l = com.afisare_comenzi(l)
            r = tk.Tk()
            text = tk.Text(r)
            for el in l:
                text.insert(tk.END, el + "\n")
            text.pack()
            r.mainloop()

        def cautare_actori():
            def validate():
                com = g.comanda1(1, 1, "a")
                l = []
                l = com.cautare_actori(l, actor.get())
                r = tk.Tk()
                text = tk.Text(r)
                for el in l:
                    text.insert(tk.END, el + "\n")
                text.pack()
                r.mainloop()
            s=tk.Tk()
            button=tk.Button(s, text="enter", command=validate)
            button.pack()
            actor=tk.Entry(s)
            actor.pack()

        def cautare_nota():
            def validate():
                com = g.comanda1(1, 1, "a")
                l = []
                l = com.cautare_nota(l, nota.get())
                r = tk.Tk()
                text = tk.Text(r)
                for el in l:
                    text.insert(tk.END, el + "\n")
                text.pack()
                r.mainloop()

            s = tk.Tk()
            button = tk.Button(s, text="enter", command=validate)
            button.pack()
            nota = tk.Entry(s)
            nota.pack()


        window = tk.Tk()
        window.geometry("1000x700")
        button = tk.Button(window, text="comanda", bg="pink", fg="red", command = comandare)
        button.pack()

        button1 = tk.Button(window, text="lista comenzi", bg="pink", fg="red", command=afisare)
        button1.pack()

        button2 = tk.Button(window, text="cautare nota", bg="pink", fg="red", command=cautare_nota)
        button2.pack()

        button3 = tk.Button(window, text="cautare actor", bg="pink", fg="red", command=cautare_actori)
        button3.pack()

        button4 = tk.Button(window, text="back", bg="pink", fg="red", command=back)
        button4.pack()


    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame = tk.Frame(root, bg="grey")
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    button = tk.Button(frame, text="Benutzer", bg="pink", fg="red", command=menu_benutzer)
    button.pack()

    button1 = tk.Button(frame, text="Filme", bg="pink", fg="red", command=menu_filme)
    button1.pack()

    button2 = tk.Button(frame, text="Gemeinsam", bg="pink", fg="red", command=menu_gemeinsam)
    button2.pack()

    button3 = tk.Button(frame, text="Exit", bg="pink", fg="red", command=quit)
    button3.pack()

    root.mainloop()
menu()
