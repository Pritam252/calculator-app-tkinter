import tkinter as tk
import basebtn

def opbtn(root, pTxt, pX, pY, pCmd):
    opbtn = basebtn.basebtn(root, "white", pTxt, pX, pY, pCmd)
    return opbtn

def opbtn_hndlr(pCmdBox, pStr):
    pCmdBox.configure(text = pCmdBox.cget("text") + str(pStr))

def opbtn_reg(root, pX, pY, pStr, pCmdBox):
    opbtn(root, str(pStr), pX, pY, pCmd=lambda: opbtn_hndlr(pCmdBox, pStr))