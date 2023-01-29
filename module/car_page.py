import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
import os, sys

from Selenium_Porsche.module.my_gallery import MyGalleryOfCars
from Selenium_Porsche.module.send_message import ContactEmail
from Selenium_Porsche.module.small_gal_icons import Icons


class Page:
    def __init__(self, root, *args, **kwargs):
        self.root = root

        # Calling up methods
        self.get_set_window()
        self.get_background()
        self.get_selection_model()
        self.get_start_photo()

    def get_set_window(self):
        ''' Main window settings '''
        self.root.title('Porsche Cars, Program Created by Adrian Szklarski, 01.2023')
        self.root.wm_attributes('-zoomed', True)
        self.root.resizable(width=False, height=False)
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

    def get_background(self):
        self.back_canvas = tk.Canvas(self.root, width=(round(self.width / 2)), height=1050, bg='white')
        self.back_canvas.place(x=0, y=0)

        foto_logo = Image.open("/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/background/Porsche_background.jpg")
        image = foto_logo.resize((round(self.width / 2), 1050), Image.ANTIALIAS)
        image.save(fp="/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/background/Background.png")
        self.logo = tk.PhotoImage(
            file="/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/background/Background.png")

        self.back_canvas.create_image(0, 0, image=self.logo, anchor="nw")

    def get_start_photo(self):
        '''Main photo on page'''
        link = f'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/background/Porsche.jpg'
        image = Image.open(link).resize((600, 400), Image.ANTIALIAS)
        image.save(fp=f'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/background/Window.png')
        link = f'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/background/Window.png'
        load = Image.open(link)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self.root, image=render)
        img.image = render
        img.place(x=300, y=60)

    def get_selection_model(self):
        ''' Addition of car model selection buttons for analysis '''
        tk.Label(self.root, text="Select of model's Porsche: ").place(x=50, y=60)

        self.radioValue = tk.IntVar(self.root, 0)
        tk.Radiobutton(self.root, text="All", variable=self.radioValue, value=1, command=self.get_driver).place(x=50,
                                                                                                                y=100)
        tk.Radiobutton(self.root, text="Cayenne", variable=self.radioValue, value=2, command=self.get_driver).place(
            x=50, y=140)
        tk.Radiobutton(self.root, text="911", variable=self.radioValue, value=3, command=self.get_driver).place(x=50,
                                                                                                                y=180)
        tk.Radiobutton(self.root, text="Cayenne S", variable=self.radioValue, value=4, command=self.get_driver).place(
            x=50, y=220)
        tk.Radiobutton(self.root, text="Panamera", variable=self.radioValue, value=5, command=self.get_driver).place(
            x=50, y=260)
        tk.Radiobutton(self.root, text="Boxter", variable=self.radioValue, value=6, command=self.get_driver).place(x=50,
                                                                                                                   y=300)
        tk.Radiobutton(self.root, text="944", variable=self.radioValue, value=7, command=self.get_driver).place(x=50,
                                                                                                                y=340)
        tk.Radiobutton(self.root, text="Cayenne Turbo", variable=self.radioValue, value=8,
                       command=self.get_driver).place(x=50, y=380)
        tk.Radiobutton(self.root, text="More", variable=self.radioValue, value=9, command=self.get_driver).place(x=50,
                                                                                                                 y=420)

    def get_driver(self):
        pass


class Gallery(Page):
    '''Gallery window'''

    def __init__(self, root, *args, **kwargs):
        Page.__init__(self, root, *args, **kwargs)
        self.gallery = root
        # self.contact = root
        self.counterUp = 0
        self.counterDown = 0

        menu = tk.Menu(self.gallery)

        file_menu = tk.Menu(menu)
        self.gallery.config(menu=file_menu)
        empty = tk.Menu(file_menu, tearoff=0)  # empty dock
        file_menu.add_cascade(label='                       '
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
        file_menu.add_command(label="  ")
        file_menu.add_command(label="Contact", command=self.get_contact_form)

        # Help
        file_menu.add_cascade(label="  Help  ", menu=helpmenu)
        helpmenu.add_command(label="About program")
        helpmenu.add_command(label="About...")

        # GitHub & Linkedin
        file_menu.add_command(label=" GitHub  ", command=self.get_github)
        file_menu.add_command(label=" Linkedin", command=self.get_linkedin)

    def get_github(self):
        webbrowser.open_new(r"https://github.com/AdrianSzklarski")

    def get_linkedin(self):
        webbrowser.open_new(r"https://www.linkedin.com/in/szklarskiadrian/")

    def get_contact_form(self):
        self.new_icon = tk.PanedWindow(orient='vertical')
        ContactEmail(self.new_icon)
        self.new_icon.place(x=1000, y=60)

    def get_reset(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def get_next_photo(self):
        self.lenght = MyGalleryOfCars(self.root).get_read_photo()
        self.counterUp += 1
        if self.counterUp <= self.lenght:
            link = f'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/work_dir_scale/Porsche_{self.counterUp}.png'
            load = Image.open(link)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(self.root, image=render)
            img.image = render
            img.place(x=300, y=60)

            self.new_text = tk.PanedWindow(orient='vertical')
            self.new_text.place(x=300, y=560)
            # name_adv = self.driver.find_elements(By.XPATH, '//*[@id="root"]/div[1]/div[3]/div[3]/div[1]/div[2]/div[2]/h1')
            result = f'Test text{link}\n' \
                # f'Name of adv: {self.name_adv}'
            tb = tk.Text(self.new_text, height=11, width=75)
            tb.pack(expand=True)
            tb.insert('end', result)
            tb.config(state='disabled')

        elif self.get_prev_photo():
            self.counterDown = self.counterUp
        else:
            self.counter = 0

    def get_prev_photo(self):
        self.lenght = MyGalleryOfCars(self.root).get_read_photo()
        self.counterDown -= 1
        calc = self.lenght + self.counterDown + 1
        if calc >= 1:
            link = f'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/work_dir_scale/Porsche_{calc}.png'
            load = Image.open(link)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(self.root, image=render)
            img.image = render
            img.place(x=300, y=60)
        elif self.get_next_photo():
            self.counterUp = self.counterDown
        else:
            self.counter = 0

    def get_start_icons(self):
        '''Arranging backgrounds for multi gallery'''
        self.new_icons = tk.PanedWindow(orient='vertical')
        Icons(self.new_icons)
        self.new_icons.place(x=950, y=60)
