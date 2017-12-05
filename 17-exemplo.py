from Tkinter import *
class Janela:
    def calcula_imc(self):          
        peso = float(self.spin_peso.get()) * 100
        altura = float(self.spin_altura.get())
        imc = (peso / (altura * altura)) * 100

        if self.rb_value.get() == 1: #masculino     
            if imc < 20.7:                       
                self.v.set("abaixo do peso")
            elif 20.7 < imc < 26.4:
                self.v.set("no peso normal")
            elif 26.4 < imc < 27.8:
                self.v.set("marginalmente acima do peso")
            elif 27.8 < imc < 31.1:
                self.v.set("acima do peso ideal")
            elif imc > 31.1:
                self.v.set("obeso")

        elif self.rb_value.get() == 2: #feminino
            if imc < 19.1:                       
                self.v.set("abaixo do peso")
            elif 19.1 < imc < 25.8:
                self.v.set("no peso normal")
            elif 25.8 < imc < 27.3:
                self.v.set("marginalmente acima do peso")
            elif 27.3 < imc < 32.3:
                self.v.set("acima do peso ideal")
            elif imc > 32.3:
                self.v.set("obeso")
    
    def __init__(self, instancia_de_Tk):              
        frame1 = Frame(instancia_de_Tk)
        frame1.configure(border=5); frame1.pack()
        frame2 = Frame(instancia_de_Tk)
        frame2.configure(border=5); frame2.pack()
        frame3 = Frame(instancia_de_Tk)
        frame3.configure(border=5); frame3.pack()
        frame4 = Frame(instancia_de_Tk)
        frame4.configure(border=5); frame4.pack()

        label1 = Label(frame1, text="Nome:"); label1.pack()
        entry1 = Entry(frame1); entry1.pack()
        label2 = Label(frame2, text="Sexo:"); label2.pack()
        
        self.rb_value = IntVar()
        self.rb1 = Radiobutton(frame2,text="Masculino",value=1, variable=self.rb_value).pack(anchor=W)
        self.rb1 = Radiobutton(frame2, text="Feminino",value=2, variable=self.rb_value).pack(anchor=W)

        self.altura = DoubleVar()
        label3 = Label(frame3, text="Altura(cm):"); label3.pack()
        self.spin_altura = Spinbox(frame3, from_=0, to=150); self.spin_altura.pack()

        self.peso = IntVar()
        label3 = Label(frame3, text="Peso(kg):"); label3.pack()
        self.spin_peso = Spinbox(frame3, from_=0, to=150); self.spin_peso.pack()

        label4 = Label(frame4, text="Resultado:"); label4.pack()
                
        self.v = StringVar()
        label5 = Label(frame4, text="", textvariable=self.v); label5.pack()
        
        button1 = Button(instancia_de_Tk, text="OK", command=self.calcula_imc); button1.pack()

raiz = Tk()
Janela(raiz)
raiz.title("Calculadora IMC")
raiz.mainloop()