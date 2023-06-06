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
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def time_reset():
     window.after_cancel(timer)    ## it will cancel time execution
     canvas.itemconfig(timer_text, text="00:00")
     time_label.config(text="Timer")
     check_label.config(text="")
     global reps
     reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps % 8==0:
        count_down(long_break_sec)
        time_label.config(text="Break",fg=RED)
    elif reps %2==0:
        count_down(short_break_sec)
        time_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        time_label.config(text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000, count_down, count - 1)      ## it will refresh the screen every time
    else:
        start_count()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pamodora")
# window.minsize(200,224)
window.config(padx=100, pady=50,bg=YELLOW)

canvas=Canvas(width=200, height=224, bg=YELLOW , highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)

timer_text=canvas.create_text(100,130,text="00:00", fill="White",font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

time_label=Label(text="Timer",bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "normal"))
time_label.grid(column=1, row=0)

start_button=Button(text="Start",width=15,command=start_count)
start_button.grid(column=0, row=2)

reset_button=Button(text="Reset", width=15, command=time_reset)
reset_button.grid(column=2, row=2)

check_label=Label(text="" ,bg=YELLOW, fg=GREEN, width=10)
check_label.grid(column=1, row=3)

window.mainloop()

