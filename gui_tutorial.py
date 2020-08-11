import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="my first window in chromeos")
label.pack()

mybutton = tk.Button(root, text="button", command=print("this is a test"))
mybutton.pack()


root.mainloop()