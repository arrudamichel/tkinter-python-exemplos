from Tkinter import *

class Janela:
    def __init__(self, instancia_de_Tk):
        label1 = Label(instancia_de_Tk, text="Hello World!")
        label1.pack ()
        pass

raiz = Tk()
Janela(raiz)
raiz.mainloop()