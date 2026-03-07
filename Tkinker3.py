import tkinter as tk
def add_task():
    task = entry.get()
    listbox.insert(tk.END,task)
    entry.delete(0,tk.END)
window = tk.Tk()
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="Add Task",command=add_task)
button.pack()
listbox = tk.Listbox(window)
listbox.pack()
window.mainloop()