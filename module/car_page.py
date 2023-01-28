import tkinter as tk
from PIL import Image


class Page:
    def __init__(self, root, *args, **kwargs):
        self.root = root

        # Calling up methods
        self.get_set_window()
        self.get_background()

    def get_set_window(self):
        ''' Main window settings '''
        self.root.title('Porsche Cars, Program Created by Adrian Szklarski, 01.2023')
        self.root.wm_attributes('-zoomed', True)
        self.root.resizable(width=False, height=False)
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

    def get_background(self):
        self.back_canvas = tk.Canvas(self.root, width=(round(self.width/2)), height=1050, bg='white')
        self.back_canvas.place(x=0, y=0)

        foto_logo = Image.open("/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/background/Background.jpg")
        image = foto_logo.resize((round(self.width/2), 1050), Image.ANTIALIAS)
        image.save(fp="/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/background/Background_copy.png")
        self.logo = tk.PhotoImage(
            file="/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/background/Background_copy.png")

        self.back_canvas.create_image(0, 0, image=self.logo, anchor="nw")


class Gallery(Page):
    '''Gallery window'''

    def __init__(self, root, *args, **kwargs):
        Page.__init__(self, root, *args, **kwargs)
        self.gallery = root
        self.counterUp = 0
        self.counterDown = 0

        menu = tk.Menu(self.gallery)
        file_menu = tk.Menu(menu)
        self.gallery.config(menu=file_menu)
        empty = tk.Menu(file_menu, tearoff=0)  # empty dock
        file_menu.add_cascade(label='                       '
                                    '                       '
                                    '                       '
                                    '                       ', menu=empty)

        filemenu = tk.Menu(file_menu, tearoff=0)
        helpmenu = tk.Menu(file_menu, tearoff=0)

        file_menu.add_cascade(label="File", menu=filemenu)

        # File
        filemenu.add_command(label="New")
        filemenu.add_command(label="Save")
        filemenu.add_command(label="Save as...")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)

        # Next & prev
        file_menu.add_command(label="Next >> |", command=self.get_next_photo)
        file_menu.add_command(label="Start >", command=self.get_start_icons)
        file_menu.add_command(label="| << Prev", command=self.get_prev_photo)
        file_menu.add_command(label="Reset app", command=self.get_reset)
        file_menu.add_command(label="    ")
        file_menu.add_command(label="Contact", command=self.get_contact_form)

        # Help
        file_menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About program")
        helpmenu.add_command(label="About...")

    def get_next_photo(self):
        pass

    def get_start_icons(self):
        pass

    def get_prev_photo(self):
        pass

    def get_reset(self):
        pass

    def get_contact_form(self):
        pass
