#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this script, we lay out images
using absolute positioning.

Author: Jan Bodnar
Last modified: July 2017
Website: www.zetcode.com
"""

from PIL import Image, ImageTk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style


class Example(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame", background="#333")

        bard = Image.open("photo/1.jpg")
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=20, y=20)

        rot = Image.open("photo/1.jpg")
        rotunda = ImageTk.PhotoImage(rot)
        label2 = Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=40, y=160)

        minc = Image.open("photo/1.jpg")
        mincol = ImageTk.PhotoImage(minc)
        label3 = Label(self, image=mincol)
        label3.image = mincol
        label3.place(x=170, y=50)


def main():
    root = Tk()
    root.geometry("300x280+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()  