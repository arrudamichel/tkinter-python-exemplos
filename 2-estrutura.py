from Tkinter import *

class Janela:
    def __init__(self, instancia_de_Tk):
        frame1 = Frame(instancia_de_Tk)
        frame1.configure(border=5, relief="groove"); frame1.pack()
        
        frame2 = Frame(instancia_de_Tk)
        frame2.configure(border=5, relief="groove"); frame2.pack()

        label1 = Label(frame1, text="widget 1"); label1.pack()
        label2 = Label(frame2, text="widget 2"); label2.pack()
        label3 = Label(frame2, text="widget 3"); label3.pack()

raiz = Tk()
Janela(raiz)
raiz.mainloop()