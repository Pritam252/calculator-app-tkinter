import tkinter as tk
import basebtn

def calcbtn(root, pTxt, pX, pY, pCmd):
    calcbtn = basebtn.basebtn(root, "blue", pTxt, pX, pY, pCmd)
    return calcbtn