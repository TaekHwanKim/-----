from tkinter import *

root = Tk()
root.title("Basic GUI") 
root.geometry("640x480")    #창의 크기 설정 ( 가로 x 세로 + x좌표 + y좌표 )
root.resizable(False, False)    #임의 크기조절 ( 너비, 높이 ) 기본값: True

root.mainloop()