from pwrbtn import pwrbtn 
from opbtn import opbtn, opbtn_reg
from calcbtn import calcbtn
from calcbox import calcbox, clearBoxes, initBoxes, clearResBox, delLastCmdChar, evaluatebox

def delHndlr():
    clearResBox()
    delLastCmdChar()

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
    calc_ops = ['/', '*', '-', '+']
    for i, operator in enumerate(calc_ops, start=2):
        opbtn_reg(root, 3, i, operator, mCmdBox)

    # Code for Number Keys
    numpad = [
        (7, 0, 3), (8, 1, 3), (9, 2, 3),
        (4, 0, 4), (5, 1, 4), (6, 2, 4),
        (1, 0, 5), (2, 1, 5), (3, 2, 5),
        ('-', 0, 6), (0, 1, 6), ('.', 2, 6)
    ]
    for num, row, col in numpad:
        opbtn_reg(root, row, col, num, mCmdBox)
    
    calcbtn(root, '=', 3, 6, evaluatebox)

    return