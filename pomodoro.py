import tkinter as tk
from tkinter import ttk
import time
import threading
from plyer import notification

# Durations in seconds
WORK_DURATION = 25 * 60
BREAK_DURATION = 5 * 60

# Notifications
def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )

# Timer logic
def start_timer(duration, label_text):
    def run():
        remaining = duration
        while remaining >= 0:
            mins, secs = divmod(remaining, 60)
            timer_var.set(f"{label_text} - {mins:02}:{secs:02}")
            time.sleep(1)
            remaining -= 1

        if label_text == "Work":
            send_notification("Pomodoro", "Work session done! 🧘 Time for a break.")
            timer_var.set("Break Time ⏸️")
            start_timer(BREAK_DURATION, "Break")
        else:
            send_notification("Pomodoro", "Break over! 💪 Back to grind.")
            timer_var.set("Session Complete ✔️")

    threading.Thread(target=run).start()

# === GUI Setup ===

app = tk.Tk()
app.title("🧘 Lo-Fi Pomodoro")
app.geometry("400x300")
app.configure(bg="#1e1e1e")

# Styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Helvetica", 12), padding=10, foreground="white", background="#333")

# Timer label
timer_var = tk.StringVar(value="Ready to focus?")
timer_label = tk.Label(app, textvariable=timer_var, font=("Helvetica", 24), fg="#FCE38A", bg="#1e1e1e")
timer_label.pack(pady=40)

# Start button
def start_pomodoro():
    timer_var.set("Starting...")
    start_timer(WORK_DURATION, "Work")

start_btn = ttk.Button(app, text="Start Pomodoro 🔥", command=start_pomodoro)
start_btn.pack(pady=20)

# Run the GUI loop
app.mainloop()
# Ensure the script runs only if executed directly