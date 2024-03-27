import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter StringVar")
        self.geometry("300x80")
        self.name_var = tk.StringVar()

        # Create widgets
        name_entry = ttk.Entry(self, textvariable=self.name_var)
        name_entry.grid(column=1, row=0)
        name_entry.focus()

        submit_button = ttk.Button(self, text="Submit", command=self.submit)
        submit_button.grid(column=2, row=0)

        self.output_label = ttk.Label(self)
        self.output_label.grid(column=0, row=1, columnspan=3)

    def submit(self):
        self.output_label.config(text=self.name_var.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()
