import pyttsx3
import time
import serial
import msvcrt
from elevenlabs import clone, generate, play, set_api_key
from elevenlabs.api import History

set_api_key("c7f8ff1ea7527c73e4015f9f9e1917ff")

def speak(str):
    audio = generate(
        text=str,
        voice="Daniel",
        model="eleven_multilingual_v2"
    )

    play(audio)

def walkFront():

    serial_port = 'COM3'  # Change this to your actual Bluetooth serial port
    baud_rate = 9600

    ser = serial.Serial(serial_port, baud_rate, timeout=1)

    def send_command(command):
        ser.write(command.encode())
        time.sleep(0.3)  # Add a delay after sending each command

    key_last_sent_time = 0  # Initialize variable to track the last time a key was sent
    key_delay = 0.5  # Set the time delay in seconds between sending keys

    send_command('F')
    time.sleep(3.5)
    send_command('L')
    time.sleep(0.15)
    send_command('F')
    time.sleep(4)
    send_command('S')
    time.sleep(1)
    ser.close()
    time.sleep(3)

def turnaround():

    serial_port = 'COM3'  # Change this to your actual Bluetooth serial port
    baud_rate = 9600

    ser = serial.Serial(serial_port, baud_rate, timeout=1)

    def send_command(command):
        ser.write(command.encode())
        time.sleep(0.3)  # Add a delay after sending each command

    key_last_sent_time = 0  # Initialize variable to track the last time a key was sent
    key_delay = 0.5  # Set the time delay in seconds between sending keys

    send_command('L')
    time.sleep(1.72)
    send_command('S')




    ser.close()
    time.sleep(3)
