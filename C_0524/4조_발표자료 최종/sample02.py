from tkinter import *

win = Tk()
win.title('여러 위젯 구성')

lb1 = Label(win, text="레이블(Lable)")

# 레이블을 윈도우에 맞게 적절하게 배치
lb1.pack()

txt = Entry(win)
txt.insert(0, '엔트리(Entry)')
txt.pack()

btn = Button(win, text = "OK")
btn.pack()

win.mainloop()
