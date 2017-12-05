from Tkinter import *

class Janela:
    def __init__(self, instancia_de_Tk):
        frame1 = Frame(instancia_de_Tk)
        frame1.configure(border=5, relief="groove"); frame1.pack()
        
        canvas1 = Canvas(frame1)
        canvas1.pack()
        
        o = canvas1.create_oval(50, 50, 100, 100, width=3, fill="blue")

raiz = Tk()
Janela(raiz)
raiz.mainloop()