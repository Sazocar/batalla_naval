import time
import random 
import serial

arduino = serial.Serial(port='COM3', baudrate=9600, bytesize=serial.EIGHTBITS)

# def getRandomNumber():
#     random_number = random.randint(0, 10)
#     return random_number


# def run():
#     while(arduino.isOpen()):
#         number = getRandomNumber()
#         print(f'El numero random fue {number}')
#         arduino.write()


# Importing Libraries
# arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


def run():
    while True:
        num = input("Enter a number: ")  # Taking input from user
        value = write_read(num)
        print(value)  # printing the value



if __name__ == '__main__':
    run()
