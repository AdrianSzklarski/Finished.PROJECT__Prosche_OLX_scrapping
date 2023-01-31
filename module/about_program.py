import tkinter as tk

class AboutProgram:

    def __init__(self, root):
        self.root = root

        self.get_form()

    def get_exit(self):
        self.root.destroy()

    def get_form(self):
        '''Application window settings'''

        describe = """... """


        self.message = tk.Label(self.root, text="About Program")
        self.mess_box_entry = tk.Text(self.root, width=50, height=18.49, wrap=tk.WORD)
        self.mess_box_entry.insert(tk.END, describe)
        self.mess_box_entry.config(state=tk.DISABLED)

        self.button_exit = tk.Button(self.root, text="Exit", command=self.get_exit)

        self.message.grid(row=3, column=0, columnspan=2, pady=(12, 0))
        self.mess_box_entry.grid(row=4, column=0, columnspan=2, padx=30)
        self.button_exit.grid(row=5, column=0, padx=(150, 50), pady=(10, 10))



