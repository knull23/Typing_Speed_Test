import tkinter as tk
from tkinter import ttk, messagebox
import time
import random

SAMPLE_TEXTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a versatile programming language loved by developers worldwide.",
    "Speed and accuracy are essential skills for efficient typing.",
    "Consistency and practice can greatly improve your typing speed."
]

start_time = None
sample_text = random.choice(SAMPLE_TEXTS)


def start_typing(event):
    global start_time
    if start_time is None:
        start_time = time.time()


def calculate_results():
    global start_time

    if start_time is None:
        messagebox.showerror('Error', 'You need to start typing first!')
        return

    end_time = time.time()
    elapsed_time = end_time - start_time

    user_text = typing_textbox.get('1.0', tk.END).strip()
    user_words = user_text.split()
    sample_words = sample_text.split()

    word_count = len(user_words)
    wpm = (word_count / elapsed_time) * 60 if elapsed_time > 0 else 0

    correct_words = sum(1 for user_word, sample_word in zip(user_words, sample_words) if user_word == sample_word)
    accuracy = (correct_words / len(sample_words)) * 100 if len(sample_words) > 0 else 0

    result_message = f"Time: {elapsed_time:.2f} seconds\nWords Per Minute: {wpm:.2f}\nAccuracy: {accuracy:.2f}%"
    messagebox.showinfo('Typing Test Results', result_message)

    reset_test()


def reset_test():
    global start_time, sample_text

    start_time = None
    sample_text = random.choice(SAMPLE_TEXTS)
    sample_label.config(text=sample_text)
    typing_textbox.delete('1.0', tk.END)


root = tk.Tk()
root.geometry('600x400')
root.title('Typing Speed Test')
root.resizable(False, False)

title_label = ttk.Label(root, text='Typing Speed Test', font=('Arial', 18, 'bold'))
title_label.pack(pady=10)

sample_label = ttk.Label(root, text=sample_text, wraplength=500, font=('Arial',12), justify='center')
sample_label.pack(pady=10)

typing_textbox = tk.Text(root, height=5, wrap='word', font=('Arial', 12), bg='lightyellow')
typing_textbox.pack(pady=10, padx=20)
typing_textbox.bind('<Key>', start_typing)

button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

calculate_button = ttk.Button(button_frame, text='Calculate Results', command=calculate_results)
calculate_button.grid(row=0, column=0, padx=5)

reset_button = ttk.Button(button_frame, text="Reset Test", command=reset_test)
reset_button.grid(row=0, column=1, padx=5)

root.mainloop()