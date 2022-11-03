from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
COUNTER = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    window.after_cancel(COUNTER)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    check_mark.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        timer.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif REPS % 2 == 0:
        timer.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    # Counts the number of minutes
    count_min = math.floor(count / 60)
    # Counts the number or seconds
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global COUNTER
        # It counts the time in milliseconds so (1000ms = 1 second)
        COUNTER = window.after(62, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✓"
            check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
# Setting the Canvas image to half the width and height to keep ip center
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)
"""Labels"""
timer = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_mark.config(pady=30)
check_mark.grid(column=1, row=4,)
"""Buttons"""
start = Button(text="Start", width=5, highlightthickness=0, command=start_timer)
start.grid(column=0, row=3)
reset = Button(text="Reset", width=5, highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=3)


window.mainloop()
