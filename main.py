#!/usr/bin/env python3

from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#346751"
YELLOW = "#F3C583"
FONT_NAME = "Courier"
CHECKMARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    screen.after_cancel(timer)
    canvas.itemconfig(counter_text, text="0:00")
    label1.config(text='Timer')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def mechanism():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_br_sec = SHORT_BREAK_MIN * 60
    long_br_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_br_sec)
        label1.config(fg=RED, text='Break')
        # checkmarks.config(text="")
    elif reps % 2 == 0:
        count_down(short_br_sec)
        label1.config(fg=PINK, text="Break")
    else:
        count_down(work_sec)
        label1.config(fg=GREEN, text='Work')

    if reps % 9 == 0 or reps == 0:
        checkmarks.config(text="")
    elif reps % 2 == 0:
        checkmarks.config(text=(checkmarks['text'] + CHECKMARK))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minutes = floor(count / 60)
    seconds = count % 60

    if seconds >= 10:
        timer_running = f"{minutes}:{seconds}"

    else:
        timer_running = f"{minutes}:0{seconds}"

    canvas.itemconfig(counter_text, text=timer_running)
    if count > 0:
        timer = screen.after(1000, count_down, (count - 1))
    elif count == 0:
        mechanism()


def start_count_down():
    count = WORK_MIN * 60
    mechanism()


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomodoro Counter")
screen.minsize(width=400, height=300)
screen.config(padx=100, pady=50, bg=YELLOW)

label1 = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
label1.grid(column=2, row=1)

start_button = Button(text="Start", width=5)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", width=5)
reset_button.grid(column=3, row=3)

checkmarks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmarks.grid(column=2, row=4)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
counter_text = canvas.create_text(100, 140, text="0:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=2, row=2)
start_button.config(command=start_count_down)
reset_button.config(command=reset_timer)

screen.mainloop()