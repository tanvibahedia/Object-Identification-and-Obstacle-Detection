
import serial
import time
import pyttsx3

# initialisation
engine = pyttsx3.init()

language = 'en'
ser = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)

for i in range(100):
    line = ser.readline()
    if line:
        string = line.decode()
        engine.say(string)
        engine.runAndWait()
        print(string)
ser.close()