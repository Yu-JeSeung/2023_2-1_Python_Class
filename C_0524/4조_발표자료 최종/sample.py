from tkinter import*

win = Tk()
win.title('pack 예제')

label = Label(win, width=50, height=5)
label.pack()

btn1 = Button(label, text="top")
btn1.pack(side = "top")

btn2 = Button(label, text="left")
btn2.pack(side = "left")

btn3 = Button(label, text="right")
btn3.pack(side = "right")

btn4 = Button(label, text="bottom")
btn4.pack(side = "bottom")

win.geometry("300x300")
win.mainloop()
