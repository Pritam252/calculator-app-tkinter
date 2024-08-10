import tkinter as tk

def basebtn(root, pColor, pTxt, pX, pY, pCmd):
    thisbtn = tk.Button(root, bg = pColor, text = pTxt, command = pCmd)
    thisbtn.config(font=("Segoe UI", 26))
    thisbtn.grid(row = pY, column = pX, sticky = 'news')
    return thisbtn