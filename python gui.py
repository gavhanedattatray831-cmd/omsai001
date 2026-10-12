import tkinter as tk
def hello():
    label.config(text="Hello!")

    window=tk.Tk()
    window.title("My App")

    button=tk.Button(window,text="Click",command=hello)
    button.pack(pady=20)

    label=tk.Label(window,text="")
    label.pack()

    window.mainloop()
    