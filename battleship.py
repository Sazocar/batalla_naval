from faulthandler import disable
from unittest import case
import customtkinter
from tkinter import *
from PIL import ImageTk, Image, ImageOps
import serial, time


arduino = serial.Serial(port='/dev/cu.usbmodem14201', baudrate=9600, bytesize=serial.EIGHTBITS)

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green



class Frame:
    def __init__(self, master): 

        self.ships_coors = []
        self.ships_count = 0

        self.misiles_coors = []
        self.misiles_count = 0

        self.didPlayerAWon = FALSE
        self.didPlayerBWon = FALSE

        self.scorePlayerA = 110
        self.scorePlayerB = 250

        self.PlayerA = 0
        self.PlayerB = 0

        self.batalla_count = 0

        self.buttons_pressed = []

        # super().__init__()
        self.master = master
        root.geometry('1000x600')
        master.title("Batalla Naval")
        root.minsize(1000, 600)
        root.maxsize(1000, 600)
        root.resizable(0, 0)
        root.eval('tk::PlaceWindow . center')


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

        self.matrizBarcosLabel = Label(
            master, text="Barcos Jugador A", font=("Arial", 20))
        self.matrizBarcosLabel.config(bg="white")
        self.matrizBarcosLabel.place(x=80, y=135)

        self.matrizMisilesLabel = Label(
            master, text="Misiles Jugador A", font=("Arial", 20))
        self.matrizMisilesLabel.config(bg="white")
        self.matrizMisilesLabel.place(x=220, y=456)

        self.PlayButton = Button(master, text="Jugar", font=(
            "Arial", 20), pady=10, command=lambda: showShipsAndMisiles(), state='disabled')
        self.PlayButton.place(x=800, y=116)

        self.verResultadosBtn = Button(root, text= "Ver Resultados", font=("Arial", 20), pady=10, command=lambda: showResults(), state='disabled')
        self.verResultadosBtn.place(x=800, y=155)

        self.resetButton = Button(root, text= "Limpiar Posiciones", font=("Arial", 20), pady=10, command=lambda: resetGame())
        self.resetButton.place(x=800, y=195)


        def readFromArduino():
            char = ''
            score = 0
            char = arduino.readline()
            score = int(char)
            if (score < 10):
                self.scorePlayerA = 0 
                self.scorePlayerB = score * 100
            else:
                char = str(score)
                print(char)
                self.scorePlayerA = int(char[0]) * 100
                self.scorePlayerB = int(char[1]) * 100

            print(f' Score Jugador A {self.scorePlayerA}')
            print(f' Score Jugador B {self.scorePlayerB}')


        def incMisilesCount():
            self.misiles_count += 1

        def incShipCount():
            # global ships_count
            self.ships_count += 1


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
            self.ships_coors.append({"x": x, "y": y})
            print(f'BARCO posicionado en ({x},{y})')

        def addMisilesCoordenates(x, y):
            self.misiles_coors.append({"x": x, "y": y})
            print(f'MISIL posicionado en ({x},{y})')

        def incBattleCount():
            self.batalla_count += 1

        def disableButton(boton):
            boton['state'] = DISABLED


        def enableButton(button):
            button['state'] = NORMAL


        def isPlayButtonEnable():
            if ((self.ships_count == 10) and (self.misiles_count == 10)):
                return TRUE
            else:
                return FALSE

        def saveShip(boton, x, y):
            if (self.ships_count < 10): 
                disableButton(boton)
                addShipsCoordenates(x, y)
                sendCoordenates(x,y)
                incShipCount()
                self.buttons_pressed.append(boton)
                print(f'Cantidad de BARCOS  restantes {10-self.ships_count}\n')
                # print(f'Array de botones: {self.buttons_pressed}')
            else:
                print('Error, no se puede agregar mas BARCOS.\n')
            if (isPlayButtonEnable()):
                enableButton(self.PlayButton)


        def saveMisiles(boton, x, y):
            if (self.misiles_count < 10):
                  disableButton(boton)
                  addMisilesCoordenates(x, y)
                  sendCoordenates(x, y)
                  incMisilesCount()
                  self.buttons_pressed.append(boton)
                  print(f'Cantidad de MISILES restantes {10-self.misiles_count}\n')
                #   print(f'Array de botones: {self.buttons_pressed}')
            else:
                print('Error, no se puede agregar mas MISILES.\n')
            if (isPlayButtonEnable()):
                enableButton(self.PlayButton)


        def showShipsAndMisiles():
            if (len(self.ships_coors) <= 0):
                print('\n')
                print('No hay barcos en posicion\n')
            else:
              print('BARCOS\n')
              for ship in self.ships_coors:
                  print(f' ({ship["x"]},{ship["y"]})')
            if (len(self.misiles_coors) <= 0):
                print('\n')
                print('No hay misiles en posicion\n')
            else:
              print('\n')
              print('MISILES\n')
              for misil in self.misiles_coors:
                  print(f' ({misil["x"]},{misil["y"]})')
            incBattleCount()
            print(f' \n Batalla numero {self.batalla_count} realizada')
            enableButton(self.verResultadosBtn)
            battleStarted()
            readFromArduino() 


        def sendCoordenates(x,y):
            pos_x = bytes(str(x-1), 'utf-8')      # Si quiero que sean numeros, le quito str
            pos_y = bytes(str(y-1), 'utf-8')      # pero me va a dar error de encode.
            arduino.write(pos_x)
            arduino.write(pos_y)
            print(f'Posicion ({pos_x},{pos_y}) ENVIADA al Arduino')
            

        def showDraw():
            top = customtkinter.CTk()  # create CTk window like you do with the Tk window
            top.resizable(0, 0)
            top.geometry("330x150")
            top.title("Resultados de la Batalla")
            label = customtkinter.CTkLabel(
                top, text=(f' Empate\n Jugador A: {self.scorePlayerA}\n Jugador B: {self.scorePlayerB}'))
            label.place(relx=0.5, rely=0.5, anchor=CENTER)

            button = customtkinter.CTkButton(
                top, text="Ok", command=lambda: exitTop(top))
            button.pack(padx=20, pady=10)

        def exitGame(top):
            root.destroy()
            top.destroy()


        def exitTop(top):
            top.destroy()

        def showWinner(player, own_score, rival_score):
            top = customtkinter.CTk()  # create CTk window like you do with the Tk window
            top.resizable(0, 0)
            top.geometry("330x150")
            top.title("????Ganador!!")
            label = customtkinter.CTkLabel(
                top, text=(f' {player} Gan?? la Batalla {own_score} - {rival_score}'))
            label.place(relx=0.5, rely=0.5, anchor=CENTER)

            button = customtkinter.CTkButton(top, text="Finalizar Juego", command=lambda: exitGame(top))
            button.pack(padx=20, pady=10)



        def open_popup(player, score):

            top = customtkinter.CTk()  # create CTk window like you do with the Tk window
            top.resizable(0,0)
            top.geometry("330x150")
            top.title("Resultados de la Batalla")
            label = customtkinter.CTkLabel(top, text=(f'{player} Gan??\n Score: {score}'))
            label.place(relx=0.5, rely=0.5, anchor=CENTER)

            button = customtkinter.CTkButton(
                top, text="Ok", command=lambda: exitTop(top))
            button.pack(padx=20, pady=10)


        def battleStarted():
            top = customtkinter.CTk()  # create CTk window like you do with the Tk window
            top.resizable(0, 0)
            top.geometry("230x150")
            top.title("????Batalla!!")
            label = customtkinter.CTkLabel(top, text=(f'??Batalla #{self.batalla_count} empez??!'))
            label.place(relx=0.5, rely=0.5, anchor=CENTER)

            button = customtkinter.CTkButton(top, text="Ok", command=lambda: exitTop(top))
            button.pack(padx=20, pady=10)


        def resetCounts():
            self.batalla_count = 0
            self.PlayerA = 0
            self.PlayerB = 0


        def showResults():
            if (self.scorePlayerA > self.scorePlayerB):
                open_popup('Jugador A', self.scorePlayerA)
                self.PlayerA += 1
                print(f' Jugador A {self.PlayerA} - Jugador B {self.PlayerB}')
            elif (self.scorePlayerA < self.scorePlayerB):
                open_popup('Jugador B', self.scorePlayerB)
                self.PlayerB += 1
                print(f' Jugador A {self.PlayerA} - Jugador B {self.PlayerB}')
            elif (self.scorePlayerA == self.scorePlayerB):
                showDraw()
                print(f' Jugador A {self.PlayerA} - Jugador B {self.PlayerB}')
            disableButton(self.PlayButton)
            disableButton(self.verResultadosBtn)
            if (self.PlayerA == 2):
                print(f' Jugador A Gan?? la partida')
                showWinner('Jugador A', self.PlayerA, self.PlayerB)
                resetGame()
                resetCounts()
            elif (self.PlayerB == 2):
                print(f' Jugador B Gan?? la partida')
                showWinner('Jugador B', self.PlayerB, self.PlayerA)
                resetGame()
                resetCounts()


      # Matriz de barcos

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


        # Fila D

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


        # Matriz de misiles

        # Primera Fila

        self.E1 = Button(master, text="(1,1)", command=lambda: saveMisiles(self.E1, 1, 1))
        self.E1.place(x=160, y=350)
        self.E2 = Button(master, text="(2,1)", command=lambda: saveMisiles(self.E2, 2, 1))
        self.E2.place(x=200, y=350)
        self.E3 = Button(master, text="(3,1)", command=lambda: saveMisiles(self.E3, 3, 1))
        self.E3.place(x=240, y=350)
        self.E4 = Button(master, text="(4,1)", command=lambda: saveMisiles(self.E4, 4, 1))
        self.E4.place(x=280, y=350)
        self.E5 = Button(master, text="(5,1)", command=lambda: saveMisiles(self.E5, 5, 1))
        self.E5.place(x=320, y=350)
        self.E6 = Button(master, text="(6,1)", command=lambda: saveMisiles(self.E6, 6, 1))
        self.E6.place(x=360, y=350)
        self.E7 = Button(master, text="(7,1)", command=lambda: saveMisiles(self.E7, 7, 1))
        self.E7.place(x=400, y=350)
        self.E8 = Button(master, text="(8,1)", command=lambda: saveMisiles(self.E8, 8, 1))
        self.E8.place(x=440, y=350)
        self.E9 = Button(master, text="(9,1)", command=lambda: saveMisiles(self.E9, 9, 1))
        self.E9.place(x=480, y=350)
        self.E10 = Button(master, text="(10,1)", command=lambda: saveMisiles(self.E10, 10, 1))
        self.E10.place(x=520, y=350)
        

        # Segunda Fila

        self.F1 = Button(master, text="(1,2)", command=lambda: saveMisiles(self.F1, 1, 2))
        self.F1.place(x=160, y=372)
        self.F2 = Button(master, text="(2,2)", command=lambda: saveMisiles(self.F2, 2, 2))
        self.F2.place(x=200, y=372)
        self.F3 = Button(master, text="(3,2)", command=lambda: saveMisiles(self.F3, 3, 2))
        self.F3.place(x=240, y=372)
        self.F4 = Button(master, text="(4,2)", command=lambda: saveMisiles(self.F4, 4, 2))
        self.F4.place(x=280, y=372)
        self.F5 = Button(master, text="(5,2)", command=lambda: saveMisiles(self.F5, 5, 2))
        self.F5.place(x=320, y=372)
        self.F6 = Button(master, text="(6,2)", command=lambda: saveMisiles(self.F6, 6, 2))
        self.F6.place(x=360, y=372)
        self.F7 = Button(master, text="(7,2)", command=lambda: saveMisiles(self.F7, 7, 2))
        self.F7.place(x=400, y=372)
        self.F8 = Button(master, text="(8,2)", command=lambda: saveMisiles(self.F8, 8, 2))
        self.F8.place(x=440, y=372)
        self.F9 = Button(master, text="(9,2)", command=lambda: saveMisiles(self.F9, 9, 2))
        self.F9.place(x=480, y=372)
        self.F10 = Button(master, text="(10,2)", command=lambda: saveMisiles(self.F10, 10, 2))
        self.F10.place(x=520, y=372)
        
        # Tercera Fila

        self.G1 = Button(master, text="(1,3)", command=lambda: saveMisiles(self.G1, 1, 3))
        self.G1.place(x=160, y=394)
        self.G2 = Button(master, text="(2,3)", command=lambda: saveMisiles(self.G2, 2, 3))
        self.G2.place(x=200, y=394)
        self.G3 = Button(master, text="(3,3)", command=lambda: saveMisiles(self.G3, 3, 3))
        self.G3.place(x=240, y=394)
        self.G4 = Button(master, text="(4,3)", command=lambda: saveMisiles(self.G4, 4, 3))
        self.G4.place(x=280, y=394)
        self.G5 = Button(master, text="(5,3)", command=lambda: saveMisiles(self.G5, 5, 3))
        self.G5.place(x=320, y=394)
        self.G6 = Button(master, text="(6,3)", command=lambda: saveMisiles(self.G6, 6, 3))
        self.G6.place(x=360, y=394)
        self.G7 = Button(master, text="(7,3)", command=lambda: saveMisiles(self.G7, 7, 3))
        self.G7.place(x=400, y=394)
        self.G8 = Button(master, text="(8,3)", command=lambda: saveMisiles(self.G8, 8, 3))
        self.G8.place(x=440, y=394)
        self.G9 = Button(master, text="(9,3)", command=lambda: saveMisiles(self.G9, 9, 3))
        self.G9.place(x=480, y=394)
        self.G10 = Button(master, text="(10,3)", command=lambda: saveMisiles(self.G10, 10, 3))
        self.G10.place(x=520, y=394)

        # Cuarta Fila

        self.H1 = Button(master, text="(1,4)", command=lambda: saveMisiles(self.H1, 1, 4))
        self.H1.place(x=160, y=416)
        self.H2 = Button(master, text="(2,4)", command=lambda: saveMisiles(self.H2, 2, 4))
        self.H2.place(x=200, y=416)
        self.H3 = Button(master, text="(3,4)", command=lambda: saveMisiles(self.H3, 3, 4))
        self.H3.place(x=240, y=416)
        self.H4 = Button(master, text="(4,4)", command=lambda: saveMisiles(self.H4, 4, 4))
        self.H4.place(x=280, y=416)
        self.H5 = Button(master, text="(5,4)", command=lambda: saveMisiles(self.H5, 5, 4))
        self.H5.place(x=320, y=416)
        self.H6 = Button(master, text="(6,4)", command=lambda: saveMisiles(self.H6, 6, 4))
        self.H6.place(x=360, y=416)
        self.H7 = Button(master, text="(7,4)", command=lambda: saveMisiles(self.H7, 7, 4))
        self.H7.place(x=400, y=416)
        self.H8 = Button(master, text="(8,4)", command=lambda: saveMisiles(self.H8, 8, 4))
        self.H8.place(x=440, y=416)
        self.H9 = Button(master, text="(9,4)", command=lambda: saveMisiles(self.H9, 9, 4))
        self.H9.place(x=480, y=416)
        self.H10 = Button(master, text="(10,4)", command=lambda: saveMisiles(self.H10, 10, 4))
        self.H10.place(x=520, y=416)

        self.UnoLabel = Label(master, text="1",)
        self.UnoLabel.config(bg="white")
        self.UnoLabel.place(x=170, y=325)
        
        self.DosLabel = Label(master, text="2",)
        self.DosLabel.config(bg="white")
        self.DosLabel.place(x=210, y=325)
              
          
        self.TresLabel = Label(master, text="3",)
        self.TresLabel.config(bg="white")
        self.TresLabel.place(x=250, y=325)
              
        self.CuatroLabel = Label(master, text="4",)
        self.CuatroLabel.config(bg="white")
        self.CuatroLabel.place(x=290, y=325)

        self.CincoLabel = Label(master, text="5",)
        self.CincoLabel.config(bg="white")
        self.CincoLabel.place(x=330, y=325)
              
        self.SeisLabel = Label(master, text="6",)
        self.SeisLabel.config(bg="white")
        self.SeisLabel.place(x=370, y=325)
              
        self.SieteLabel = Label(master, text="7",)
        self.SieteLabel.config(bg="white")
        self.SieteLabel.place(x=410, y=325)

        self.OchoLabel = Label(master, text="8",)
        self.OchoLabel.config(bg="white")
        self.OchoLabel.place(x=450, y=325)

        self.NueveLabel = Label(master, text="9",)
        self.NueveLabel.config(bg="white")
        self.NueveLabel.place(x=490, y=325)
              
        self.DiezLabel = Label(master, text="10",)
        self.DiezLabel.config(bg="white")
        self.DiezLabel.place(x=530, y=325)

        self.ALabel = Label(master, text="A",)
        self.ALabel.config(bg="white")
        self.ALabel.place(x=140, y=349)
              
        self.BLabel = Label(master, text="B",)
        self.BLabel.config(bg="white")
        self.BLabel.place(x=140, y=371)

        self.CLabel = Label(master, text="C",)
        self.CLabel.config(bg="white")
        self.CLabel.place(x=140, y=395)
              
        self.DLabel = Label(master, text="D",)
        self.DLabel.config(bg="white")
        self.DLabel.place(x=140, y=417)


        def resetGame():
            for button in self.buttons_pressed:
                button['state'] = NORMAL
            del self.buttons_pressed[:]
            del self.ships_coors[:]
            del self.misiles_coors[:]
            self.ships_count = 0
            self.misiles_count = 0
            disableButton(self.PlayButton)
            disableButton(self.verResultadosBtn)

              
            



root = Tk()
MainFrame = Frame(root)
root.mainloop()
