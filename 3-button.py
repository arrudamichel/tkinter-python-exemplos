from Tkinter import *

class Janela:
    def __init__(self, instancia_de_Tk):
        frame1 = Frame(instancia_de_Tk)
        frame1.configure(border=5, relief="groove"); frame1.pack()
        
        button1 = Button(frame1, text="OK")
        button1.pack()

raiz = Tk()
Janela(raiz)
raiz.mainloop()