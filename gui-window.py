import tkinter as tk

def say_hello():
    print("Hello from Anatolia GUI!")

root = tk.Tk()
root.title("Anatolia Sample GUI")

button = tk.Button(root, text="Click Me", command=say_hello)
button.pack()

root.mainloop()
