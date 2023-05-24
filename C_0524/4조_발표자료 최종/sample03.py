import tkinter as tk
from tkinter import *
win = tk.Tk()
win.title("체크박스 예제")
win.geometry("600x400")

#버튼 클릭하면 선택한 체크버튼을 선택하였다는 문구 출력하는 함수 설정
def sub_chk():
    if ChkVar1.get() == 1:
        lb2.configure(text = "파이썬을 선택하였습니다.")
    elif ChkVar2.get() == 1:
        lb2.configure(text = "자바를 선택하였습니다.")
    elif ChkVar3.get() == 1:
        lb2.configure(text = "알고리즘을 선택하였습니다.")
        
#"과목을 선택하세요" 라벨 생성
lb1 = tk.Label(win, text="과목을 선택하세요.", bg = "yellow")
lb1.grid(row = 0, column = 0, columnspan = 3)

#"파이썬", "자바", "알고리즘" 체크버튼 생성
ChkVar1 = tk.IntVar()
chk1 = tk.Checkbutton(win, text = "파이썬", variable = ChkVar1)
chk1.grid(row = 1, column = 0, sticky = "w")
ChkVar2 = tk.IntVar()
chk2 = tk.Checkbutton(win, text = "자바", variable = ChkVar2)
chk2.grid(row = 1, column = 1, sticky = "w")
ChkVar3 = tk.IntVar()
chk3 = tk.Checkbutton(win, text = "알고리즘", variable = ChkVar3)
chk3.grid(row = 1, column = 2, sticky = "w")

#결과물 출력되는 라벨 생성
lb2 = tk.Label(win)
lb2.grid(row = 2, column = 0, sticky = "w", columnspan = 3)

#체크버튼을 선택 후 클릭 시 함수 실행
btn1 = tk.Button(win, text = "선택", command = sub_chk)
btn1.grid(row = 1, column = 3, sticky = "w")
win.mainloop()



