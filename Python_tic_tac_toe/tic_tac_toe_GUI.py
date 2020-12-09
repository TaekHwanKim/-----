from tkinter import *
from functools import partial

root = Tk()
root.title("TicTacToe GUI") 
root.geometry("300x300")    #창의 크기 설정 ( 가로 x 세로 + x좌표 + y좌표 )
root.resizable(False, False)    #임의 크기조절 ( 너비, 높이 ) 기본값: True

checkimg = PhotoImage(file="tic_tac_toe/check.png")
def click_b():
    this.Button["image"]=checkimg

b1 = Button(root,text = "1", width="100", height="100", command=click_b)
b2 = Button(root,text = "2", width="100", height="100", command=click_b)
b3 = Button(root,text = "3", width="100", height="100", command=click_b)
b4 = Button(root,text = "4", width="100", height="100", command=click_b)
b5 = Button(root,text = "5", width="100", height="100", command=click_b)
b6 = Button(root,text = "6", width="100", height="100", command=click_b)
b7 = Button(root,text = "7", width="100", height="100", command=click_b)
b8 = Button(root,text = "8", width="100", height="100", command=click_b)
b9 = Button(root,text = "9", width="100", height="100", command=click_b)

b1.place(x=0,y=0)
b2.place(x=100,y=0)
b3.place(x=200,y=0)
b4.place(x=0,y=100)
b5.place(x=100,y=100)
b6.place(x=200,y=100)
b7.place(x=0,y=200)
b8.place(x=100,y=200)
b9.place(x=200,y=200)




root.mainloop()