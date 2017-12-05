from Tkinter import *
class Janela:
    def __init__(self, instancia_de_Tk):                
        top = Frame() ; top.pack()
        l1 = Label (top, text="Exemplo", foreground="blue"); l1.pack ()
        l1.configure(relief="ridge", font="Arial 24 bold", border=5, background="yellow")

raiz = Tk()
Janela(raiz)
raiz.mainloop()