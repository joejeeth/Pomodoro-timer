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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    label.config(text="TIMER", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
    canvas.itemconfig(time_c, text="00:00")
    tick_label.config(text="0")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    print(reps)

    if reps % 8 == 0:
        label.config(text="REST", fg=RED, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        label.config(text="REST", fg=PINK, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        label.config(text="WORK", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = int(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_c, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            tick_label.config(text=int(reps/2))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# label
label = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
label.grid(column=3, row=0)

tick_label = Label(text="0", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
tick_label.grid(column=3, row=4)

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_c = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=3, row=3)

# Buttons
start_button = Button(text="Start", fg="black", font=(FONT_NAME, 13), highlightthickness=0, command=start_timer)
start_button.grid(column=2, row=4)

reset_button = Button(text="Reset", fg="black", font=(FONT_NAME, 13), highlightthickness=0, command=reset_timer)
reset_button.grid(column=4, row=4)

window.mainloop()
