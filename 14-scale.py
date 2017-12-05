from Tkinter import *

class Janela:
    def __init__(self, instancia_de_Tk):                
        scale = Scale(instancia_de_Tk)
        scale.pack(anchor=CENTER)

raiz = Tk()
Janela(raiz)
raiz.mainloop()