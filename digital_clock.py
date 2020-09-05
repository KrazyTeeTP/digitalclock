from tkinter import *
import time
import sys

root = Tk()
root.title('Digital : : Clock')


def print_time():
	time_var = time.strftime("%H:%M:%S")
	test.config(text=time_var)
	test.after(200, print_time)


test = Label(root, font=('segeo', 90), fg='white', bg='grey')
test.pack()

print_time()


root.mainloop()