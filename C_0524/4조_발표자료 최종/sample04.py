# tkinter 모듈을 tk로 불러옴
import tkinter as tk
# tkinter.messagebox 모듈을 mb로 불러옴
import tkinter.messagebox as mb
# matplotlib.pyplot 모듈을 plt로 불러옴
import matplotlib.pyplot as plt

# BarChartApp 클래스 정의
class BarChartApp(tk.Frame):
    # 생성자 함수
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Bar Chart App")

        self.create_widgets()

    # 위젯을 생성하는 함수
    def create_widgets(self):
        # 데이터 입력을 위한 라벨과 엔트리 위젯 생성
        tk.Label(self.master, text="apple").grid(row=0, column=0, padx=10, pady=10)
        self.apple_entry = tk.Entry(self.master)
        self.apple_entry.grid(row=0, column=1)

        tk.Label(self.master, text="banana").grid(row=1, column=0, padx=10, pady=10)
        self.banana_entry = tk.Entry(self.master)
        self.banana_entry.grid(row=1, column=1)

        tk.Label(self.master, text="pear").grid(row=2, column=0, padx=10, pady=10)
        self.pear_entry = tk.Entry(self.master)
        self.pear_entry.grid(row=2, column=1)

        # 막대그래프를 출력하는 버튼 생성
        tk.Button(self.master, text="막대 그래프 보기",
                  command=self.show_bar_chart).grid(row=3, column=0,
                                                    columnspan=2, padx=10, pady=10)
  # 막대그래프 출력 함수
    def show_bar_chart(self):
        # 엔트리 위젯에서 입력받은 값을 변수에 저장
        try:
            apple_value = float(self.apple_entry.get())
            banana_value = float(self.banana_entry.get())
            pear_value = float(self.pear_entry.get())
        # 숫자가 아닌 값을 입력한 경우 오류창을 띄움
        except ValueError:
            mb.showerror("Error", "숫자를 입력해주세요.")
            return

        # 막대그래프 생성
        labels = ["apple", "banana", "pear"]
        values = [apple_value, banana_value, pear_value]

        plt.bar(labels, values)
        plt.show()

if __name__ == "__main__":
    # tkinter 루트 윈도우 생성
    root = tk.Tk()
    # BarChartApp 클래스의 인스턴스 생성
    app = BarChartApp(master=root)
    # 이벤트 루프 실행
    app.mainloop()



