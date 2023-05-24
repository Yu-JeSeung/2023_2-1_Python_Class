from tkinter import *
from tkinter import ttk

# Tkinter 인스턴스 생성
win = Tk()

# Window 사이즈 지정
win.geometry("300x200+100+100")
win.resizable(False, False)

# get() : entry에 텍스트를 문자열로 반환
def Cal():
    label.configure(text="결과 값 = " + str(eval(entry.get())))

entry = Entry(win)
entry.pack()

button = Button(win, text="계산", command=Cal)
button.pack()

label = Label(win)
label.pack()

win.mainloop()
