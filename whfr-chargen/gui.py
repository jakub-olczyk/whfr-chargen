#!/usr/bin/python

from tkinter import *

from generator import Generator
from utils import print_character

class WarhammerChargenGUI(Frame):
    def createWidgets(self):
        self.char_text = StringVar()
        self.char_text.set('Press generate button')
        self.text = Label(self, textvariable = self.char_text, justify=LEFT)
        self.text['width'] = 120
        self.text.pack()


        self.QUIT = Button(self)
        self.QUIT['text'] = 'Exit'
        self.QUIT['command'] = self.quit

        self.QUIT.pack({'side': 'left'})

        self.character = Generator()

        self.generate = Button(self)
        self.generate['text'] = 'Generate!'
        self.generate['command'] = self.new_character
        self.generate.pack({'side': 'right'})

    def new_character(self):
        self.char_text.set(print_character(self.character.result(), is_printing=False))
        self.character = Generator()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.master.title('Warhammer Character Generator')

root = Tk()
wcg = WarhammerChargenGUI(master=root)
wcg.mainloop()
root.destroy()
