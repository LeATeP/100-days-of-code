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
reps = -1


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(long_break_sec)
        name_label.config(text="Break", fg=RED)
    elif reps % 2 == 1:
        count_down(short_break_sec)
        name_label.config(text="Break", fg=PINK)
    elif reps % 2 == 0:
        count_down(work_sec)
        name_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    print(count)

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    elif count == 0:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

# TODO: 1. Label
name_label = Label(font=(FONT_NAME, 35, "bold"))
name_label.place(x=20, y=-40)


# TODO: 2. 2 Buttons
def reset1():
    pass


button_Start = Button(text="Start", command=start_timer())
button_Start.place(x=-50, y=230)

button_Reset = Button(text="Reset", command=reset_timer())
button_Reset.place(x=200, y=230)

# TODO 3. Check by completion button  (fg=GREEN) as label = text

if reps == 1:
    check_label = Label(text="#", font=(FONT_NAME, 20))
    check_label.place(x=65, y=230)
    check_label.config(fg=GREEN, bg=GREEN)
elif reps == 3:
    check_label2 = Label(text="#", font=(FONT_NAME, 20))
    check_label2.place(x=90, y=230)
    check_label2.config(fg=GREEN, bg=GREEN)
elif reps == 5:
    check_label3 = Label(text="#", font=(FONT_NAME, 20))
    check_label3.place(x=115, y=230)
    check_label3.config(fg=GREEN, bg=GREEN)

window.mainloop()
