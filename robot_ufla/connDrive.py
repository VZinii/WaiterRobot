import serial
import time
import msvcrt
import pyttsx3


# Initialize the text-to-speech engine
engine = pyttsx3.init()

# # Set properties (optional)
# # engine.setProperty("rate", 150)  # Speed of speech
# # engine.setProperty("volume", 1.0)  # Volume level (0.0 to 1.0)

# # Speak the provided text
# engine.say("Ai minha nossa, em plena segunda feira você me enchendo...")
# time.sleep(3)
# engine.say("Ops, esqueci que estamos em São João k k k ")
# time.sleep(1)
# engine.say("tudo bem. Vou andar para frente e dar um giro")
# time.sleep(2)
# engine.say("luz na passarela que lá vem ela")

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
# send_command('B')
# time.sleep(3)
send_command('L')
time.sleep(0.15)
send_command('F')
time.sleep(4)
send_command('S')


# send_command('L')
# send_command('L')
# send_command('L')
# send_command('L')
# send_command('L')
# send_command('L')


time.sleep(3)

# # Wait for the speech to finish
engine.runAndWait()

# Wait for the speech to finish
# engine.runAndWait()


# while True:
#     send_command('S')
#     if msvcrt.kbhit():
#         user_input = msvcrt.getch().decode().upper()
#         print(user_input, end='', flush=True)

#         if user_input in ['F', 'B', 'L', 'R', 'S', 'V']:
#             current_time = time.time()
#             if current_time - key_last_sent_time >= key_delay:
#                 send_command(user_input)
#                 key_last_sent_time = current_time
#         else:
#             print("\nInvalid command. Please enter 'F', 'B', 'L', 'R', 'S', or 'V'.")
