import tkinter as tk

def say_hello():
    print("Hello this is simple GUI!")

root = tk.Tk()
root.title("Tkinter GUI Python")

button = tk.Button(root, text="Click Me", command=say_hello)
button.pack()

root.mainloop()
