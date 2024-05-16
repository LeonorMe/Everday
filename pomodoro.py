import tkinter as tk 
from tkinter import messagebox
from ttkbootstrap import ttk, Style
"""
SEC = 60
WORK_TIME = 40 * SEC
SHORT_BREAK = 10 * SEC
LONG_BREAK = 15 * SEC
SHORT_LAPS = 2
LAPS = 6
"""

SEC = 15
WORK_TIME = 1 * SEC
SHORT_BREAK = 1 * SEC
LONG_BREAK = 1 * SEC
SHORT_LAPS = 2
LAPS = 6

class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x200")
        self.root.title("Everday")
        self.style = Style(theme="simplex")
        self.style.theme_use()
        
        self.timer_label = tk.Label(self.root, text="", font=("TkDefault", 40))
        self.timer_label.pack(pady=20)
        
        self.start_button = ttk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)
        
        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=5)
        
        self.work_time, self.break_time = WORK_TIME, SHORT_BREAK
        self.is_work_time, self.pomodoros_completed, self.is_running = True, 0, False
        
        self.root.mainloop()
        
    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        self.update_timer()
        
    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False
    
    def update_timer(self):
        if self.is_running:
            if self.is_work_time:
                self.work_time -= 1
                if self.work_time == 0:
                    self.is_work_time = False
                    self.pomodoros_completed += 1
                    self.break_time = LONG_BREAK if self.pomodoros_completed % SHORT_LAPS == 0 else SHORT_BREAK
                    messagebox.showinfo("Great" if self.pomodoros_completed % SHORT_LAPS == 0 
                                        else "Good", "Long break"
                                        if self.pomodoros_completed % SHORT_LAPS == 0
                                        else "Short break")
            else:
                self.break_time -= 1
                if self.break_time == 0:
                    self.is_work_time, self.work_time = True, WORK_TIME
                    messagebox.showinfo("Work time", "Back to work")
            minutes, seconds = divmod(self.work_time if self.is_work_time else self.break_time, SEC)
            self.timer_label.config(text="{:02d}:{:2d}".format(minutes, seconds))
            self.root.after(1000, self.update_timer)
            
PomodoroTimer()