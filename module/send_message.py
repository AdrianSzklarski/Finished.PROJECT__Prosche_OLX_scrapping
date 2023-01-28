import smtplib
import tkinter as tk
from tkinter import ttk


class Contact:

    def __init__(self, root):
        self.root = root

        self.sender_box = tk.StringVar()
        self.name_sender = tk.StringVar()

        self.get_form()

    def get_contact(self):
        '''Server settings'''
        sender = self.sender_box_entry.get()  # who sends an e-mail
        message = self.mess_box_entry.get('1.0', 'end')
        receiver = "address@gmail.com"
        login = "Adrian"
        password = "***"

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(login, password)
            server.sendmail(sender, receiver, message)
            server.quit()
            statement_1 = "Success, your e-mail was send!"
            return statement_1
        except:
            statement_2 = "Warning! Message don't send!"
            return statement_2

    def get_info(self, get_contact):
        self.display['text'] = get_contact()

    def get_exit(self):
        self.root.destroy()

    def get_form(self):
        '''Application window settings'''
        self.sender_label = tk.Label(self.root, text="Sender Email")
        self.name_sender_label = tk.Label(self.root, text="Name")
        self.message = tk.Label(self.root, text="Write your message below")
        self.display = tk.Label(self.root)
        self.sender_box_entry = ttk.Entry(self.root, textvariable=self.sender_box)
        self.name_box_entry = tk.Entry(self.root, textvariable=self.name_sender)
        self.mess_box_entry = tk.Text(self.root, width=50, height=10, wrap=tk.WORD)
        self.button_send = tk.Button(self.root, text="Send Message", command=lambda: self.get_info(self.get_contact))
        self.button_exit = tk.Button(self.root, text="Exit", command=self.get_exit)

        self.sender_label.grid(row=0, column=0, padx=(40, 5), pady=(20, 5))
        self.sender_box_entry.grid(row=0, column=1, padx=(40, 0), pady=(20, 5))
        self.name_sender_label.grid(row=1, column=0, padx=(40, 5), pady=(20, 20))
        self.name_box_entry.grid(row=1, column=1, padx=(40, 0), pady=(20, 20))
        self.display.grid(row=2, column=0, columnspan=2, pady=(12, 0))
        self.message.grid(row=3, column=0, columnspan=2, pady=(12, 0))
        self.mess_box_entry.grid(row=4, column=0, columnspan=2, padx=30)
        self.button_send.grid(row=5, column=1, padx=(0, 190), pady=(10, 10))
        self.button_exit.grid(row=5, column=1, padx=(10, 20), pady=(10, 10))

