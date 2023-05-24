import tkinter as tk
def calculate():
    try:
        result = int(data1_entry.get()) + int(data2_entry.get())
        result_label.config(text="결과: " + str(result))
    except ValueError:
        result_label.config(text="숫자를 입력해주세요.")
root = tk.Tk()
root.title("간단한 계산기")

data1_label = tk.Label(root, text="Data1:")
data1_label.pack()

data1_entry = tk.Entry(root)
data1_entry.pack()
data2_label = tk.Label(root, text="Data2:")
data2_label.pack()
data2_entry = tk.Entry(root)
data2_entry.pack()
calculate_button = tk.Button(root, text="계산", command=calculate)
calculate_button.pack()

result_label = tk.Label(root)
result_label.pack()
root.mainloop()
