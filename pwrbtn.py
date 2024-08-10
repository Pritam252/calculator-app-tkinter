import tkinter as tk
import basebtn

def pwrbtn(root, pTxt, pX, pY, pCmd):
    pwrbtn = basebtn.basebtn(root, "red", pTxt, pX, pY, pCmd)
    return pwrbtn