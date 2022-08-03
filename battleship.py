from tkinter import *
from PIL import ImageTk, Image, ImageOps

ships_coors = []
ships_count = 0

misiles_coors = []
misiles_count = 0

class Frame:
    def __init__(self, master): 
        # super().__init__()
        self.master = master
        root.geometry('1000x600')
        master.title("Batalla Naval")
        root.minsize(1000, 600)
        root.maxsize(1000, 600)
        root.resizable(0, 0)


        # Putting background image
        image = Image.open("battleship.jpg")
        image = ImageOps.fit(image, [1000, 600], Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.__background = Label(root,
                                  image=photo)
        self.__background.image = photo
        self.__background.place(relx=0,
                                rely=0,
                                relwidth=1,
                                relheight=1)

        self.etiqueta = Label(
            master, text="Matriz de Barcos Jugador A", font=("Arial", 20))
        self.etiqueta.config(bg="white")
        self.etiqueta.place(x=80, y=135)


        def incMisilesCount():
            global misiles_count
            misiles_count += 1

        def incShipCount():
            global ships_count
            ships_count += 1


        def make_labels():
          letter_coordinates = "ABCD"
          for y in range(1, 5):

              for numbers in range(1, 5):
                  Label(root,
                        text=str(letter_coordinates[numbers-1])).grid(row=numbers, column=0)

              for x in range(1, 11):
                  Label(root,
                        text=str(x)).grid(row=0, column=x)


        def addShipsCoordenates(x, y):
            ships_coors.append({"x": x, "y": y})
            print(f'Barco posicionado en ({x},{y})')

        def addMisilesCoordenates(x, y):
            misiles_coors.append({"x": x, "y": y})
            print(f'Misil posicionado en ({x},{y})')


        def disableButton(boton):
            boton['state'] = DISABLED


        def saveShip(boton, x, y):
            if (ships_count < 10): 
                disableButton(boton)
                addShipsCoordenates(x, y)
                incShipCount()
                print(f'Cantidad de barcos restantes {10-ships_count}')
            else:
                print('Error, no se puede agregar mas barcos.')


        def saveMisiles(boton, x, y):
            if (misiles_count < 10):
                  disableButton(boton)
                  addMisilesCoordenates(x, y)
                  incMisilesCount()
                  print(f'Cantidad de misiles restantes {10-misiles_count}')
            else:
                print('Error, no se puede agregar mas misiles.')

        make_labels()

        self.A1 = Button(master, text="(1,1)", command=lambda: saveShip(self.A1, 1, 1))
        self.A1.grid(row=1, column=1)
        self.A2 = Button(master, text="(2,1)", command=lambda: saveShip(self.A2, 2, 1))
        self.A2.grid(row=1, column=2)
        self.A3 = Button(master, text="(3,1)", command=lambda: saveShip(self.A3, 3, 1))
        self.A3.grid(row=1, column=3)
        self.A4 = Button(master, text="(4,1)", command=lambda: saveShip(self.A4, 4, 1))
        self.A4.grid(row=1, column=4)
        self.A5 = Button(master, text="(5,1)", command=lambda: saveShip(self.A5, 5, 1))
        self.A5.grid(row=1, column=5)
        self.A6 = Button(master, text="(6,1)", command=lambda: saveShip(self.A6, 6, 1))
        self.A6.grid(row=1, column=6)
        self.A7 = Button(master, text="(7,1)", command=lambda: saveShip(self.A7, 7, 1))
        self.A7.grid(row=1, column=7)
        self.A8 = Button(master, text="(8,1)", command=lambda: saveShip(self.A8, 8, 1))
        self.A8.grid(row=1, column=8)
        self.A9 = Button(master, text="(9,1)", command=lambda: saveShip(self.A9, 9, 1))
        self.A9.grid(row=1, column=9)
        self.A10 = Button(master, text="(10,1)", command=lambda: saveShip(self.A10, 10, 1))
        self.A10.grid(row=1, column=10)

        # Fila B

        self.B1 = Button(master, text="(1,2)", command=lambda: saveShip(self.B1, 1, 2))
        self.B1.grid(row=2, column=1)
        self.B2 = Button(master, text="(2,2)", command=lambda: saveShip(self.B2, 2, 2))
        self.B2.grid(row=2, column=2)
        self.B3 = Button(master, text="(3,2)", command=lambda: saveShip(self.B3, 3, 2))
        self.B3.grid(row=2, column=3)
        self.B4 = Button(master, text="(4,2)", command=lambda: saveShip(self.B4, 4, 2))
        self.B4.grid(row=2, column=4)
        self.B5 = Button(master, text="(5,2)", command=lambda: saveShip(self.B5, 5, 2))
        self.B5.grid(row=2, column=5)
        self.B6 = Button(master, text="(6,2)", command=lambda: saveShip(self.B6, 6, 2))
        self.B6.grid(row=2, column=6)
        self.B7 = Button(master, text="(7,2)", command=lambda: saveShip(self.B7, 7, 2))
        self.B7.grid(row=2, column=7)
        self.B8 = Button(master, text="(8,2)", command=lambda: saveShip(self.B8, 8, 2))
        self.B8.grid(row=2, column=8)
        self.B9 = Button(master, text="(9,2)", command=lambda: saveShip(self.B9, 9, 2))
        self.B9.grid(row=2, column=9)
        self.B10 = Button(master, text="(10,2)", command=lambda: saveShip(self.B10, 10, 2))
        self.B10.grid(row=2, column=10)


        # Fila C

        self.C1 = Button(master, text="(1,3)", command=lambda: saveShip(self.C1, 1, 3))
        self.C1.grid(row=3, column=1)
        self.C2 = Button(master, text="(2,3)", command=lambda: saveShip(self.C2, 2, 3))
        self.C2.grid(row=3, column=2)
        self.C3 = Button(master, text="(3,3)", command=lambda: saveShip(self.C3, 3, 3))
        self.C3.grid(row=3, column=3)
        self.C4 = Button(master, text="(4,3)", command=lambda: saveShip(self.C4, 4, 3))
        self.C4.grid(row=3, column=4)
        self.C5 = Button(master, text="(5,3)", command=lambda: saveShip(self.C5, 5, 3))
        self.C5.grid(row=3, column=5)
        self.C6 = Button(master, text="(6,3)", command=lambda: saveShip(self.C6, 6, 3))
        self.C6.grid(row=3, column=6)
        self.C7 = Button(master, text="(7,3)", command=lambda: saveShip(self.C7, 7, 3))
        self.C7.grid(row=3, column=7)
        self.C8 = Button(master, text="(8,3)", command=lambda: saveShip(self.C8, 8, 3))
        self.C8.grid(row=3, column=8)
        self.C9 = Button(master, text="(9,3)", command=lambda: saveShip(self.C9, 9, 3))
        self.C9.grid(row=3, column=9)
        self.C10 = Button(master, text="(10,3)", command=lambda: saveShip(self.C10, 10, 3))
        self.C10.grid(row=3, column=10)


        # Fila C

        self.D1 = Button(master, text="(1,4)", command=lambda: saveShip(self.D1, 1, 4))
        self.D1.grid(row=4, column=1)
        self.D2 = Button(master, text="(2,4)", command=lambda: saveShip(self.D2, 2, 4))
        self.D2.grid(row=4, column=2)
        self.D3 = Button(master, text="(3,4)", command=lambda: saveShip(self.D3, 3, 4))
        self.D3.grid(row=4, column=3)
        self.D4 = Button(master, text="(4,4)", command=lambda: saveShip(self.D4, 4, 4))
        self.D4.grid(row=4, column=4)
        self.D5 = Button(master, text="(5,4)", command=lambda: saveShip(self.D5, 5, 4))
        self.D5.grid(row=4, column=5)
        self.D6 = Button(master, text="(6,4)", command=lambda: saveShip(self.D6, 6, 4))
        self.D6.grid(row=4, column=6)
        self.D7 = Button(master, text="(7,4)", command=lambda: saveShip(self.D7, 7, 4))
        self.D7.grid(row=4, column=7)
        self.D8 = Button(master, text="(8,4)", command=lambda: saveShip(self.D8, 8, 4))
        self.D8.grid(row=4, column=8)
        self.D9 = Button(master, text="(9,4)", command=lambda: saveShip(self.D9, 9, 4))
        self.D9.grid(row=4, column=9)
        self.D10 = Button(master, text="(10,4)", command=lambda: saveShip(self.D10, 10, 4))
        self.D10.grid(row=4, column=10)


        self.E1 = Button(master, text="(1,1)", command=lambda: saveMisiles(self.E1, 1, 1))
        self.E1.place(x=160, y=350)
        self.E2 = Button(master, text="(1,2)", command=lambda: saveMisiles(self.E2, 1, 2))
        self.E2.place(x=200, y=350)
        self.E3 = Button(master, text="(1,3)", command=lambda: saveMisiles(self.E3, 1, 3))
        self.E3.place(x=240, y=350)
        self.E4 = Button(master, text="(1,4)", command=lambda: saveMisiles(self.E4, 1, 4))
        self.E4.place(x=280, y=350)
        self.E5 = Button(master, text="(1,5)", command=lambda: saveMisiles(self.E5, 1, 5))
        self.E5.place(x=320, y=350)
        self.E6 = Button(master, text="(1,6)", command=lambda: saveMisiles(self.E6, 1, 6))
        self.E6.place(x=360, y=350)
        self.E7 = Button(master, text="(1,7)", command=lambda: saveMisiles(self.E7, 1, 7))
        self.E7.place(x=400, y=350)
        self.E8 = Button(master, text="(1,8)", command=lambda: saveMisiles(self.E8, 1, 8))
        self.E8.place(x=440, y=350)
        self.E9 = Button(master, text="(1,9)", command=lambda: saveMisiles(self.E9, 1, 9))
        self.E9.place(x=480, y=350)
        self.E10 = Button(master, text="(1,10)", command=lambda: saveMisiles(self.E10, 1, 10))
        self.E10.place(x=520, y=350)
        



root = Tk()
MainFrame = Frame(root)
root.mainloop()

# #Button 1: not clickable
# btn1 = Button(root, text="Button 1", command= lambda: disableButton(btn1))
# btn1.pack(side=LEFT)

# #Button 2 : clickable
# btn = Button(root, text="Hola", command= lambda: disableButton(btn))
# btn.pack(side=RIGHT)

# # print(btn.configure().keys())

# root.mainloop()
