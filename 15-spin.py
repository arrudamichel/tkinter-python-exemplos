from Tkinter import *

class Janela:
    def __init__(self, instancia_de_Tk):                
        w = Spinbox(instancia_de_Tk, from_=0, to=10)
        w.pack()

raiz = Tk()
Janela(raiz)
raiz.mainloop()