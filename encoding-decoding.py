# import from tkinter all the packages
from tkinter import *
# import base64
import base64

# Intializing tkinter to build the window
root = Tk()
# Initializing the size of the window
root.geometry('500x300')
# Adjusting the size of the window
root.resizable(0,0)
# Adding the title to the window
root.title("Encoding and Decoding Messages")

# The program name
Label(root, text = 'ENCODE DECODE', font = 'arial 20 bold').pack()

# Initializing variables
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

# Encode
''' The Encode function is to convert a code to coded form. '''
def Encode(key,message):
    enc = []

    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Decode
''' The Decode function is to reconvert the code back to its original form '''
def Decode(key,message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(message)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)