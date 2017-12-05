from Tkinter import *

class Janela:
    def __init__(self, instancia_de_Tk):                
        
        for txt in ("preto", "vermelho","azul","verde"):
            Radiobutton(text=txt,value=txt).pack(anchor=W)
raiz = Tk()
Janela(raiz)
raiz.mainloop()