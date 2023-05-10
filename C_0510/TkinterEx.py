from tkinter import *
root = Tk() 

root.title("Siso") # title 생성
# root.geometry("300x200") # 크기 조절
root.resizable(False, False) # 크기조절 가능여부 설정

def btncmd():
    print("버튼 눌렀다니까요?")

# 프레임 
main_Frame = Frame(root, width=200, height=200, bg='blue').grid(row=0, column=0, padx=10, pady=5)
main_Frame2 = Frame(root, width=200, height=200, bg='magenta').grid(row=0, column=1, padx=10, pady=5)

# 버튼
btn = Button(main_Frame, text="버튼이라지요", command=btncmd, width=20, height=10, fg='black', bg='yellow')
btn.grid(row=0,column=0)

# 텍스트
input_text = Text(main_Frame2, width=10, height=1)
input_text.grid(row=0, column=0)

root.mainloop()