from Tkinter import *

class Janela:
    def __init__(self, instancia_de_Tk):
        frame1 = Frame(instancia_de_Tk)
        frame1.configure(border=5, relief="groove"); frame1.pack()
        
        c1 = Checkbutton(text="Checkbox 1", var=1)
        c1.pack()
        c2 = Checkbutton(text="Checkbox 2", var=2)
        c2.pack()

raiz = Tk()
Janela(raiz)
raiz.mainloop()