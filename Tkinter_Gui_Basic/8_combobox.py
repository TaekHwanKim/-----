import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Basic GUI") 
root.geometry("640x480")    #창의 크기 설정 ( 가로 x 세로 + x좌표 + y좌표 )

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5 , values=values, state="readonly")
combobox.pack()
#combobox.set("카드 결제일") 최초 목록의 제목 설정
combobox.current(0) # 0번째 인덱스값 선택


def btncmd():
    print(combobox.get())
    
btn = Button(root, text = "선택", command = btncmd)
btn.pack()

root.mainloop()