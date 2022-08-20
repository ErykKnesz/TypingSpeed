import tkinter as tk
from faker import Faker

TIMER_START = 60
SCORE_START = 0

root = tk.Tk()
root.title("Typing Pace")
current_word = tk.StringVar()
user_word = tk.StringVar()
score = tk.IntVar(root, SCORE_START)
timer = tk.IntVar(root, TIMER_START)

fake = Faker()
words = iter(fake.words(200))


def start():
    current_word.trace('w', validate)
    user_word.trace('w', validate)
    timer.set(TIMER_START)
    score.set(SCORE_START)
    root.after(1000, countdown)
    next_word()
    user_word.set("")


def end():
    current_word.set(f"Time's up! you typed {score.get()} words.")
    root.after_cancel(countdown)


def countdown():
    global timer
    if timer.get() > 0:
        timer.set(timer.get() - 1)
        root.after(1000, countdown)
    else:
        end()


def validate(*args):
    global score
    if user_word.get() == current_word.get():
        score.set(score.get() + 1)
        if timer.get() > 0:
            next_word()
        user_word.set("")


def next_word():
    global current_word
    try:
        current_word.set(next(words))
    except StopIteration:
        pass


# Entry
word_input = tk.Entry(root, textvariable=user_word)
word_input.grid(column=1, row=2, padx=5, pady=5)
word_input.focus()

# Labels
word_label = tk.Label(textvariable=current_word, font=("TkDefaultFont", 15))
word_label.grid(column=1, row=1, padx=5, pady=5)
score_label = tk.Label(textvariable=str(score))
score_label.grid(column=1, row=3, padx=5, pady=5)
timer_label = tk.Label(textvariable=str(timer))
timer_label.grid(column=2, row=1, padx=5, pady=5)

# Button
start_button = tk.Button(root, text="Start", command=start)
start_button.grid(column=2, row=2, padx=5, pady=5)

root.mainloop()
