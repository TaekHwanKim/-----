from tkinter import *

root = Tk()
root.title("Basic GUI") 
root.geometry("640x480")    #창의 크기 설정 ( 가로 x 세로 + x좌표 + y좌표 )

txt = Text(root, width=30, height=5)    #여러줄 입력용
txt.pack()
txt.insert(END, "글자를 입력하세요")


e = Entry(root, width = 30)    #한줄 입력용
e.pack()
e.insert(0, "한줄만 입력")

def btncmd():
    #내용 출력
    print(txt.get("1.0", END)) #1: 첫번째 라인 , 0: 0번째 column
    print(e.get())

    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text = "클릭", command = btncmd)
btn.pack()

root.mainloop()