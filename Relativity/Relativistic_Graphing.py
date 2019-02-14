from tkinter import *

master = Tk()

canvas_width  = 640
canvas_height = 400

w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#000000")

master.mainloop()