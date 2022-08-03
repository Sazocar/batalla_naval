from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageOps

ships_coors = []
ships_count = 0


class Frame:
    def __init__(self, master):
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

        def incShipCount():
            global ships_count
            ships_count = ships_count + 1


        def make_labels():
          letter_coordinates = "ABCD"
          for y in range(1, 5):

              for numbers in range(1, 5):
                  Label(root,
                        text=str(letter_coordinates[numbers-1])).grid(row=numbers, column=0)

              for x in range(1, 11):
                  Label(root,
                        text=str(x)).grid(row=0, column=x)


        def addCoordenate(x, y):
            ships_coors.append({"x": x, "y": y})
            print(ships_coors)


        def disableButton(boton):
            boton['state'] = DISABLED


        def saveAndDisableButton(boton, x, y):
            if (ships_count < 10): 
                disableButton(boton)
                addCoordenate(x, y)
                incShipCount()
                print(ships_count)
            else:
                print('Error, no se puede agregar mas barcos.')


        make_labels()
        
        # Fila A

        self.A1 = Button(master, text="(1,1)", command=lambda: saveAndDisableButton(self.A1, 1, 1))
        self.A1.grid(row=1, column=1)
        self.A2 = Button(master, text="(2,1)", command=lambda: saveAndDisableButton(self.A2, 2, 1))
        self.A2.grid(row=1, column=2)
        self.A3 = Button(master, text="(3,1)", command=lambda: saveAndDisableButton(self.A3, 3, 1))
        self.A3.grid(row=1, column=3)
        self.A4 = Button(master, text="(4,1)", command=lambda: saveAndDisableButton(self.A4, 4, 1))
        self.A4.grid(row=1, column=4)
        self.A5 = Button(master, text="(5,1)", command=lambda: saveAndDisableButton(self.A5, 5, 1))
        self.A5.grid(row=1, column=5)
        self.A6 = Button(master, text="(6,1)", command=lambda: saveAndDisableButton(self.A6, 6, 1))
        self.A6.grid(row=1, column=6)
        self.A7 = Button(master, text="(7,1)", command=lambda: saveAndDisableButton(self.A7, 7, 1))
        self.A7.grid(row=1, column=7)
        self.A8 = Button(master, text="(8,1)", command=lambda: saveAndDisableButton(self.A8, 8, 1))
        self.A8.grid(row=1, column=8)
        self.A9 = Button(master, text="(9,1)", command=lambda: saveAndDisableButton(self.A9, 9, 1))
        self.A9.grid(row=1, column=9)
        self.A10 = Button(master, text="(10,1)", command=lambda: saveAndDisableButton(self.A10, 10, 1))
        self.A10.grid(row=1, column=10)

        # Fila B

        self.B1 = Button(master, text="(1,2)", command=lambda: saveAndDisableButton(self.B1, 1, 2))
        self.B1.grid(row=2, column=1)
        self.B2 = Button(master, text="(2,2)", command=lambda: saveAndDisableButton(self.B2, 2, 2))
        self.B2.grid(row=2, column=2)
        self.B3 = Button(master, text="(3,2)", command=lambda: saveAndDisableButton(self.B3, 3, 2))
        self.B3.grid(row=2, column=3)
        self.B4 = Button(master, text="(4,2)", command=lambda: saveAndDisableButton(self.B4, 4, 2))
        self.B4.grid(row=2, column=4)
        self.B5 = Button(master, text="(5,2)", command=lambda: saveAndDisableButton(self.B5, 5, 2))
        self.B5.grid(row=2, column=5)
        self.B6 = Button(master, text="(6,2)", command=lambda: saveAndDisableButton(self.B6, 6, 2))
        self.B6.grid(row=2, column=6)
        self.B7 = Button(master, text="(7,2)", command=lambda: saveAndDisableButton(self.B7, 7, 2))
        self.B7.grid(row=2, column=7)
        self.B8 = Button(master, text="(8,2)", command=lambda: saveAndDisableButton(self.B8, 8, 2))
        self.B8.grid(row=2, column=8)
        self.B9 = Button(master, text="(9,2)", command=lambda: saveAndDisableButton(self.B9, 9, 2))
        self.B9.grid(row=2, column=9)
        self.B10 = Button(master, text="(10,2)", command=lambda: saveAndDisableButton(self.B10, 10, 2))
        self.B10.grid(row=2, column=10)


        # Fila C

        self.C1 = Button(master, text="(1,3)", command=lambda: saveAndDisableButton(self.C1, 1, 3))
        self.C1.grid(row=3, column=1)
        self.C2 = Button(master, text="(2,3)", command=lambda: saveAndDisableButton(self.C2, 2, 3))
        self.C2.grid(row=3, column=2)
        self.C3 = Button(master, text="(3,3)", command=lambda: saveAndDisableButton(self.C3, 3, 3))
        self.C3.grid(row=3, column=3)
        self.C4 = Button(master, text="(4,3)", command=lambda: saveAndDisableButton(self.C4, 4, 3))
        self.C4.grid(row=3, column=4)
        self.C5 = Button(master, text="(5,3)", command=lambda: saveAndDisableButton(self.C5, 5, 3))
        self.C5.grid(row=3, column=5)
        self.C6 = Button(master, text="(6,3)", command=lambda: saveAndDisableButton(self.C6, 6, 3))
        self.C6.grid(row=3, column=6)
        self.C7 = Button(master, text="(7,3)", command=lambda: saveAndDisableButton(self.C7, 7, 3))
        self.C7.grid(row=3, column=7)
        self.C8 = Button(master, text="(8,3)", command=lambda: saveAndDisableButton(self.C8, 8, 3))
        self.C8.grid(row=3, column=8)
        self.C9 = Button(master, text="(9,3)", command=lambda: saveAndDisableButton(self.C9, 9, 3))
        self.C9.grid(row=3, column=9)
        self.C10 = Button(master, text="(10,3)", command=lambda: saveAndDisableButton(self.C10, 10, 3))
        self.C10.grid(row=3, column=10)




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
