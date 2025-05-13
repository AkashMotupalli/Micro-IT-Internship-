import tkinter as tk
from datetime import datetime
import time
import threading

class StopwatchClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch & Clock")
        self.running = False
        self.start_time = None
        self.elapsed_time = 0

        self.clock_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.clock_label.pack()

        self.stopwatch_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.stopwatch_label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side="left")

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side="left")

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side="left")

        self.update_clock()

    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=now)
        self.root.after(1000, self.update_clock)

    def update_stopwatch(self):
        while self.running:
            time.sleep(1)
            self.elapsed_time = time.time() - self.start_time
            mins, secs = divmod(int(self.elapsed_time), 60)
            hours, mins = divmod(mins, 60)
            self.stopwatch_label.config(text=f"{hours:02}:{mins:02}:{secs:02}")

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            threading.Thread(target=self.update_stopwatch, daemon=True).start()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.stopwatch_label.config(text="00:00:00")

root = tk.Tk()
app = StopwatchClockApp(root)
root.mainloop()