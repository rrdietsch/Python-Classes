import tkinter as tk

HEIGHT = 700
WIDTH = 800

root= tk.Tk()
canva = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canva.pack()

#create and show frames
frame_io = tk.Frame(root, bg="white")
frame_list = tk.Frame(root, bg="white")
frame_list.place(relx=0.05, rely=0.05, relwidth=0.20, relheight=.8)
frame_io.place(relx=0.3, rely=0.05, relwidth=0.6, relheight=.8)

#what's inside of frame_list
contact_list = tk.Listbox(frame_list, height="500")
contact_list.pack()

#inside the frame.io

full_name_l= tk.Label(frame_io, text="Full Name")
full_name_l.grid(row=0, column=0, padx=5, pady=10)
full_name_io = tk.Entry(frame_io)
full_name_io.grid(row=0, column=1)

number_l= tk.Label(frame_io, text="Phone Number")
number_l.grid(row=1, column=0, padx=5, pady=10)
number_io = tk.Entry(frame_io)
number_io.grid(row=1, column=1)

address_l= tk.Label(frame_io, text="Address")
address_l.grid(row=2, column=0, padx=5, pady=10)
address_io = tk.Entry(frame_io)
address_io.grid(row=2, column=1)


root.mainloop()