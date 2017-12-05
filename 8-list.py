from Tkinter import *

class Janela:
    def __init__(self, instancia_de_Tk):
        frame1 = Frame(instancia_de_Tk)
        frame1.pack()
        
        lb = Listbox()
        lb.pack(side=LEFT,expand=True,fill="both")
        
        sb = Scrollbar()
        sb.pack(side=RIGHT,fill="y")
        sb.configure(command=lb.yview)
        
        lb.configure(yscrollcommand=sb.set)
        
        for i in range(100):
            lb.insert(END,i)        

raiz = Tk()
Janela(raiz)
raiz.mainloop()