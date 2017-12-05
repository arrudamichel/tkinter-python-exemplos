from Tkinter import *

class Janela:
    def __init__(self, instancia_de_Tk):
        frame1 = Frame(instancia_de_Tk)
        frame1.pack()
        
        e1 = Entry()
        e1.insert(END, 'Digite um valor')
        e1.pack()        

raiz = Tk()
Janela(raiz)
raiz.mainloop()