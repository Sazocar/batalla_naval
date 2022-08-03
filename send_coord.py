import serial

ser = serial.Serial(
    port='COM17', baudrate=9600, bytesize=serial.EIGHTBITS)

ships_coors = [{"x": 1, "y": 2}, {"x": 5, "y": 3}]


def run():
  sendCoors()



def sendCoors():
  for coordenate in ships_coors:
    print(f' Enviando coordenada x: {coordenate["x"]}')
    # ser.print(coordenate["x"])
    input('Press enter to continue...')
    
    print(f' Enviando coordenada y: {coordenate["y"]}')
    # ser.print(coordenate["y"])
    input('Press enter to continue...')


if __name__ == '__main__':
  run()
