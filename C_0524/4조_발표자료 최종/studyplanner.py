import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

event_counter = 1

def add_event():
    global event_counter
    event = event_entry.get()
    start_time = start_time_entry.get()
    end_time = end_time_entry.get()

    if event and start_time and end_time:
        if start_am_pm.get() == "PM":
            start_time = add_hours(start_time, 12)
        if end_am_pm.get() == "PM":
            end_time = add_hours(end_time, 12)
        
        study_time = calculate_study_time(start_time, end_time)
        event_info = f"{event} (시작시각: {start_time}, 종료시각: {end_time}, 공부시간: {study_time})"
        event_listbox.insert(tk.END, f"{event_counter}. {event_info}")
        event_counter += 1
        clear_entries()
    else:
        messagebox.showwarning("경고", "공부, 시작시각, 종료시각을 모두 입력해주세요.")

def add_hours(time_str, hours):
    hour, minute = map(int, time_str.split(":"))
    total_minutes = hour * 60 + minute + (hours * 60)
    new_hour = total_minutes // 60
    new_minute = total_minutes % 60
    return f"{new_hour:02d}:{new_minute:02d}"

def calculate_study_time(start_time, end_time):
    start_hour, start_minute = map(int, start_time.split(":"))
    end_hour, end_minute = map(int, end_time.split(":"))

    total_minutes = (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)
    hours = total_minutes // 60
    minutes = total_minutes % 60
    study_time = f"{hours}.{minutes // 10} 시간"

    return study_time

def clear_entries():
    event_entry.delete(0, tk.END)
    start_time_entry.delete(0, tk.END)
    end_time_entry.delete(0, tk.END)

def delete_event():
    selected_index = event_listbox.curselection()
    if selected_index:
        event_listbox.delete(selected_index)

        global event_counter
        event_counter = 1
        events = event_listbox.get(0, tk.END)
        event_listbox.delete(0, tk.END)
        for event in events:
            event_listbox.insert(tk.END, f"{event_counter}. {event}")
            event_counter += 1

def clear_all():
    event_listbox.delete(0, tk.END)
    global event_counter
    event_counter = 1

def show_bar_chart():
    study_times = []
    events = event_listbox.get(0, tk.END)
    for event in events:
        study_time = float(event.split("공부시간: ")[-1].split(" 시간")[0])
        study_times.append(study_time)

    labels = [event.split(". ")[1].split(" (")[0] for event in events]
    plt.bar(labels, study_times)
    plt.xlabel('subject')
    plt.ylabel('studytime(hour)')
    plt.title('studytime for each subject')
    plt.show()

root = tk.Tk()

event_frame = tk.Frame(root)
event_frame.pack(pady=10)

event_label = tk.Label(event_frame, text="공부 할 과목:")
event_label.grid(row=0, column=0)

event_entry = tk.Entry(event_frame)
event_entry.grid(row=0, column=1)

start_time_label = tk.Label(event_frame, text="시작시각:")
start_time_label.grid(row=1, column=0)

start_time_entry = tk.Entry(event_frame)
start_time_entry.grid(row=1, column=1)

start_am_pm = tk.StringVar(value="AM")
start_am_radio = tk.Radiobutton(event_frame, text="AM", variable=start_am_pm, value="AM")
start_am_radio.grid(row=1, column=2)
start_pm_radio = tk.Radiobutton(event_frame, text="PM", variable=start_am_pm, value="PM")
start_pm_radio.grid(row=1, column=3)

end_time_label = tk.Label(event_frame, text="종료시각:")
end_time_label.grid(row=2, column=0)

end_time_entry = tk.Entry(event_frame)
end_time_entry.grid(row=2, column=1)

end_am_pm = tk.StringVar(value="AM")
end_am_radio = tk.Radiobutton(event_frame, text="AM", variable=end_am_pm, value="AM")
end_am_radio.grid(row=2, column=2)
end_pm_radio = tk.Radiobutton(event_frame, text="PM", variable=end_am_pm, value="PM")
end_pm_radio.grid(row=2, column=3)

add_button = tk.Button(event_frame, text="추가", command=add_event)
add_button.grid(row=0, column=4, padx=10)

event_listbox = tk.Listbox(root, width=50)
event_listbox.pack(pady=10)

delete_button = tk.Button(root, text="삭제", command=delete_event)
delete_button.pack()

clear_button = tk.Button(root, text="전체 삭제", command=clear_all)
clear_button.pack(pady=10)

show_chart_button = tk.Button(root, text="그래프로 보기", command=show_bar_chart)
show_chart_button.pack(pady=10)

root.mainloop()
