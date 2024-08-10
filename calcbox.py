import tkinter as tk

# The 2 Boxes variable (for convenience)
mCmdBox: tk.Label = None
mResBox: tk.Label = None

def clearBoxes():
    global mCmdBox
    global mResBox
    mCmdBox.config(text='')
    mResBox.config(text='')

def initBoxes(pCmdBox, pResBox):
    global mCmdBox
    global mResBox
    mCmdBox = pCmdBox
    mResBox = pResBox

def clearResBox():
    global mResBox
    mResBox.config(text='')

def delLastCmdChar():
    global mCmdBox
    mCmdBox.config(text=mCmdBox.cget('text')[:-1])

def txtbox(root):
    txtBox = tk.Label(root, font = ("Segoe UI", 15), height = 1, width = 50, justify="left", anchor="w")
    return txtBox

def calcbox(root, pX, pY):
    box = txtbox(root)
    box.grid(row=pY, column=pX, sticky='n', columnspan=1000) # LOL, 1000 columnspan. IDK how to make buttons together?
    return box

def evaluatebox():
    global mCmdBox
    global mResBox
    mResBox.config(text=eval(mCmdBox.cget('text')))