#! python3

import tkinter as tk
from tkinter import ttk

from application import Application
from weather import Weather

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__': main()