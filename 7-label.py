from Tkinter import *

class Janela:
    def __init__(self, instancia_de_Tk):
        frame1 = Frame(instancia_de_Tk)
        frame1.pack()
        
        l = Label(frame1, text="Label")        
        l.pack()        

raiz = Tk()
Janela(raiz)
raiz.mainloop()