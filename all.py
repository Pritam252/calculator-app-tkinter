print("Calculator App for Group Project")

import tkinter as tk

from math import log as log

def basebtn(root, pColor, pTxt, pX, pY, pCmd):
    thisbtn = tk.Button(root, bg = pColor, text = pTxt, command = pCmd)
    thisbtn.config(font=("Segoe UI", 26))
    thisbtn.grid(row = pY, column = pX, sticky = 'news')
    return thisbtn

def calcbtn(root, pTxt, pX, pY, pCmd):
    calcbtn = basebtn(root, "#34AEEB", pTxt, pX, pY, pCmd)
    return calcbtn

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

def delHndlr():
    clearResBox()
    delLastCmdChar()

def pwrbtn(root, pTxt, pX, pY, pCmd):
    pwrbtn = basebtn(root, "red", pTxt, pX, pY, pCmd)
    return pwrbtn

def opbtn(root, pTxt, pX, pY, pCmd):
    opbtn = basebtn(root, "white", pTxt, pX, pY, pCmd)
    return opbtn

def opbtn_hndlr(pCmdBox, pStr):
    pCmdBox.configure(text = pCmdBox.cget("text") + str(pStr))

def opbtn_reg(root, pX, pY, pStr, pCmdBox):
    opbtn(root, str(pStr), pX, pY, pCmd=lambda: opbtn_hndlr(pCmdBox, pStr))

def window(root):
    
    # 2 Boxes on the top for the command to be calculated and the result.
    mCmdBox = calcbox(root, 0, 0)
    mCmdBox.config(background="#03e8fc") #(text = "Use the keypad to enter a command here.")
    mResBox = calcbox(root, 0, 1)
    mResBox.config(background="#03fc90") #(text = "The result of the command will be displayed here.")
    initBoxes(mCmdBox, mResBox)

    # Code for Clearing/Deleting
    pwrbtn(root, " CE", 0, 2, clearBoxes)
    pwrbtn(root, " C ", 1, 2, clearResBox)
    pwrbtn(root, "DEL", 2, 2, delHndlr)

    # Code for Basic Operations
    # Optimization nightmare
    #opbtn_reg(root, 3, 2, '/', cmdbox)
    #opbtn_reg(root, 3, 3, '*', cmdbox)
    #opbtn_reg(root, 3, 4, '-', cmdbox)
    #opbtn_reg(root, 3, 5, '+', cmdbox)
    calc_ops = ['/', '*', '-', '+', '', 'log']
    for i, operator in enumerate(calc_ops, start=2):
        opbtn_reg(root, 3, i, operator, mCmdBox)

    # Code for Number Keys
    numpad = [
        (7, 0, 3), (8, 1, 3), (9, 2, 3),
        (4, 0, 4), (5, 1, 4), (6, 2, 4),
        (1, 0, 5), (2, 1, 5), (3, 2, 5),
        ('-', 0, 6), (0, 1, 6), ('.', 2, 6),
        ('(', 0, 7), (')', 1, 7), (',', 2, 7)
    ]
    for num, row, col in numpad:
        opbtn_reg(root, row, col, num, mCmdBox)
    
    calcbtn(root, '=', 3, 6, evaluatebox)

    return

wnd = tk.Tk()

wnd.title("Calculator app group project v1.2")
wnd.geometry("320x560")

window(wnd)

wnd.mainloop()
