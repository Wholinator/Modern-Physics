import numpy as np
from tkinter import *

canvas_width = 640
canvas_height = 400
master = Tk()

px_per_m = 1
mass_scaling = 1
w = Canvas()


def __init__():

    w = Canvas(master, width=canvas_width, height=canvas_height)
    w.create_rectangle((0, 0, canvas_width, canvas_height), fill="Black")
    w.pack()


def paint(obs_list):
    # clear all canvas items and refill background
    w.delete("all")
    w.create_rectangle((0, 0, canvas_width, canvas_height), fill="Black")

    coords = [convert_coordinates(obs) for obs in obs_list]

    for n in coords:
        w.create_oval(n, fill="White")

    w.pack()

    master.update()


def convert_coordinates(obs):
    x = obs.x * px_per_m
    y = obs.y * px_per_m

    size = obs.r * mass_scaling

    return x, y, x+size, y+size

# converts between window event coords and canvas coords
# def callback(event):
#    canvas = event.widget
#    x = canvas.canvasx(event.x)
#    y = canvas.canvasy(event.y)
#    print(canvas.find_closest(x, y))
