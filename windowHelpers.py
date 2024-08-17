import tkinter as tk

def SetWindowCenterOfScreen(root: tk.Tk, width: int = 400, height: int = 200):
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    x = (screenWidth / 2) - (width / 2)
    y = (screenHeight / 2) - (height / 2)

    root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    pass