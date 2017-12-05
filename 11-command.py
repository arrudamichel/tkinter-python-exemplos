from Tkinter import *

class Janela:
    def __init__(self, instancia_de_Tk):                
        def incrementar():
            n = int(rotulo.configure("text")[4]) + 1
            rotulo.configure(text=str(n))
        
        b = Button(instancia_de_Tk, text="Soma 1",command=incrementar)
        b.pack()
        rotulo = Label(instancia_de_Tk, text="0")
        rotulo.pack()      

raiz = Tk()
Janela(raiz)
raiz.mainloop()