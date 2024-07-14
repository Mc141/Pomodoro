import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)






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
check_text = ""
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_seconds)
        title.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_seconds)
        title.config(text="Break", fg=PINK)
    else:
        countdown(work_seconds)
        title.config(text="Work", fg=GREEN)






# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(time):
    minutes = math.floor(time / 60)
    seconds = time % 60

    if minutes < 10:
        minutes = f"0{minutes}"

    if seconds == 0 or seconds < 10:
        seconds = f"0{seconds}"



    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if time > 0:
        time -= 1
        global timer
        timer = window.after(20, countdown, time)
    else:
        start_timer()
        if reps % 2 == 0:
            global check_text
            check_text += "✓"
            check_mark.config(text=check_text)
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.resizable(0, 0)
window.config(padx=100, pady=50, bg=YELLOW)

window.wm_iconphoto(False, PhotoImage(file=resource_path("tomato.png")))


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file=resource_path("tomato.png"))
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))



title = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 40, "bold"), fg=GREEN)


start_button = Button(text="Start", bd=0, command=start_timer)


reset_button = Button(text="Reset", bd=0, command=reset_timer)


check_mark = Label(text="", fg=GREEN, font=("Couries", 15, "bold"), bg=YELLOW)



canvas.grid(row=1, column=1)
title.grid(row=0, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
check_mark.grid(row=3, column=1)








window.mainloop()