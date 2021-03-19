from tkinter import *
import base64

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("DataFair = Message Encode and Decode")

Label(root, text = 'ENCODE DECODE', font = 'arial 20 bold').pack()
Label(root, text = 'DataFlair', font = 'arial 20 bold').pack(side = BOTTOM)

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()