import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Basic GUI") 
root.geometry("640x480")    #창의 크기 설정 ( 가로 x 세로 + x좌표 + y좌표 )
'''
progressbar = ttk.Progressbar(root, maximum = 100, mode="determinate")
progressbar.start(10)

progressbar.pack()

def btncmd():
    progressbar.stop()
    
btn = Button(root, text = "선택", command = btncmd)
btn.pack()
'''

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) # pbar의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())

btn = Button(root, text = "시작", command = btncmd2)
btn.pack()


root.mainloop()