from tkinter import *
from main import Contador

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Ventana")
        self.geometry("800x600")

        for c in range(2):
            for f in range(2):
                self.contador=Contador(self, height=300, width=400)
                self.contador.place(x=400*c,y=300*f)

    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app=MainApp()
    app.start()