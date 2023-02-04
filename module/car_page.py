import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import webbrowser
import os, glob, sys, time
import requests
from os.path import join


from Selenium_Porsche.module.about_program import AboutProgram
from Selenium_Porsche.module.about_us import AboutProgramUs
from Selenium_Porsche.module.create_dir import get_dir
from Selenium_Porsche.module.dirClear import get_clear_dir
from Selenium_Porsche.module.my_gallery import MyGalleryOfCars
from Selenium_Porsche.module.send_message import ContactEmail
from Selenium_Porsche.module.small_gal_icons import Icons
from tkinter.filedialog import asksaveasfile

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Page:
    def __init__(self, root, *args, **kwargs):
        self.root = root

        # Calling up methods
        self.get_set_window()
        self.get_background()
        self.get_selection_model()
        self.get_start_photo()

        # get_clear_dir()
        self.option = Options()
        self.option.add_argument("--headless")


        # # controll of interface of user
        self.option.headless = False

    def get_set_window(self):
        ''' Main window settings '''
        self.root.title('Porsche Cars, Program Created by Adrian Szklarski, 01.2023')
        self.root.wm_attributes('-zoomed', True)
        self.root.resizable(width=False, height=False)
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

    def get_background(self):
        self.back_canvas = tk.Canvas(self.root, width=1845, height=1050,
                                     bg='white')  # (round(self.width / 2)), 1845
        self.back_canvas.place(x=0, y=0)
        foto_logo = Image.open("/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/background/Porsche_background.jpg")
        image = foto_logo.resize((1845, 1050), Image.ANTIALIAS)  # (round(self.width / 2), 1845
        image.save(fp="/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/background/Background.png")
        self.logo = tk.PhotoImage(
            file="/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/background/Background.png")
        self.back_canvas.create_image(0, 0, image=self.logo, anchor="nw")

    def get_start_photo(self):
        '''Main photo on page'''
        # car
        link = f'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/background/Porsche.jpg'
        image = Image.open(link).resize((600, 400), Image.ANTIALIAS)
        image.save(fp=f'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/background/Window.png')
        link = f'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/background/Window.png'
        load = Image.open(link)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self.root, image=render)
        img.image = render
        img.place(x=300, y=60)

        # gallery
        link = f'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/background/start_win_gallery.png'
        load = Image.open(link)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self.root, image=render)
        img.image = render
        img.place(x=950, y=60)

        # chart
        link = f'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/background/start_win_chart.png'
        load = Image.open(link)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self.root, image=render)
        img.image = render
        img.place(x=1370, y=560)

        # reset dir
        get_clear_dir()

        # create dir
        get_dir()

    def get_selection_model(self):
        ''' Addition of car model selection buttons for analysis '''
        tk.Label(self.root, text="Select of model's Porsche: ").place(x=50, y=60)

        self.radioValue = tk.IntVar(self.root, 0)
        tk.Radiobutton(self.root, text="All                                 "
                       , variable=self.radioValue, value=1, command=self.get_scrapping).place(x=50, y=100)
        tk.Radiobutton(self.root, text="Cayenne                       "
                       , variable=self.radioValue, value=2, command=self.get_scrapping).place(x=50, y=140)
        tk.Radiobutton(self.root, text="911                               "
                       , variable=self.radioValue, value=3, command=self.get_scrapping).place(x=50, y=180)
        tk.Radiobutton(self.root, text="Cayenne S                    "
                       , variable=self.radioValue, value=4, command=self.get_scrapping).place(x=50, y=220)
        tk.Radiobutton(self.root, text="Panamera                     "
                       , variable=self.radioValue, value=5, command=self.get_scrapping).place(x=50, y=260)
        tk.Radiobutton(self.root, text="Boxter                          "
                       , variable=self.radioValue, value=6, command=self.get_scrapping).place(x=50, y=300)
        tk.Radiobutton(self.root, text="944                               "
                       , variable=self.radioValue, value=7, command=self.get_scrapping).place(x=50, y=340)
        tk.Radiobutton(self.root, text="Cayenne Turbo             "
                       , variable=self.radioValue, value=8, command=self.get_scrapping).place(x=50, y=380)
        tk.Radiobutton(self.root, text="More                             "
                       , variable=self.radioValue, value=9, command=self.get_scrapping).place(x=50, y=420)

    def get_scrapping(self):
        ''' Scrapping the olx page for Porsche '''
        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.option)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.option)
        driver.implicitly_wait(1)
        driver.get('https://www.olx.pl/d/motoryzacja/samochody/porsche/')
        driver.maximize_window()
        # driver.close()
        driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()  # Cookies
        driver.find_element(By.CLASS_NAME, 'css-fb37n3').click()  # css-fb37n3  css-mf5jvh Arrow down in models
        # driver.find_element(By.XPATH,
        #                     '//*[@id="root"]/div[1]/div[2]/form/div[3]/div[1]/div/div[3]/div/div/div/div/svg').click()

        driver.find_element(By.XPATH,
                            '//*[@id="root"]/div[1]/div[2]/form/div[3]/div[1]/div/div[3]/div/div/div[2]/div/div[' + str(
                                self.radioValue.get()) + ']/label/input').click()

        link = r'?search%5Bfilter_enum_model%5D%5B0%5D'
        if True:
            if self.radioValue.get() == 1:
                self.link = None
                self.name = 'All'
            elif self.radioValue.get() == 2:
                self.link = f'{link}=cayenne'
                self.name = 'Cayenne'
            elif self.radioValue.get() == 3:
                self.link = f'{link}=911'
                self.name = '911'
            elif self.radioValue.get() == 4:
                self.link = f'{link}=cayenne-s'
                self.name = 'Cayenne-S'
            elif self.radioValue.get() == 5:
                self.link = f'{link}=panamera'
                self.name = 'Panamera'
            elif self.radioValue.get() == 6:
                self.link = f'{link}=boxster'
                self.name = 'Boxter'
            elif self.radioValue.get() == 7:
                self.link = f'{link}=944'
                self.name = '944'
            elif self.radioValue.get() == 8:
                self.link = f'{link}=cayenne-turbo'
                self.name = 'Cayenne-Turbo'
            elif self.radioValue.get() == 9:
                self.link = f'{link}=inny'
                self.name = 'Another'
            else:
                pass

        #  Link-up for selected car model
        link = f'https://www.olx.pl/d/motoryzacja/samochody/porsche/{self.link}'
        dir_html = r'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/html/html.txt'
        driver.get(link)
        with open(dir_html, 'w') as f:
            f.write(link)

        #  Information on the number of cars found
        elements = driver.find_elements(By.XPATH,
                                        '//*[@id="root"]/div[1]/div[2]/form/div[4]/div[2]/h3/div')

        #  Unpacking the text and downloading the number
        for element in elements:
            number = element.text
            oneNumber = []
            for iterationNumber in number:
                try:
                    oneNumber.append(str(int(iterationNumber)))
                except ValueError:
                    pass

            self.total = ''
            for unpackList in range(0, len(oneNumber)):
                self.total = self.total + oneNumber[unpackList]

            answer = f'{self.total} Porsche {self.name} models found'
            tk.Label(self.root, text=answer).place(x=50, y=460)

        #  Downloading thumbnail images of cars
        counter = 1
        while True:
            try:
                div = driver.find_element(By.XPATH, f'//*[@id="root"]/div[1]/div[2]/form/div[5]/div/div[2]/div[{counter}]').text
                resultPath = join(r'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/work_dir', f'Porsche{counter}.png')
                # print(div)
                if div and counter != 9:
                    link = f'//*[@id="root"]/div[1]/div[2]/form/div[5]/div/div[2]/div[{counter}]/a/div/div/div[1]/div[1]/div'
                    with open(resultPath, 'ab') as file:
                        time.sleep(0.5)
                        file.write(driver.find_element(By.XPATH, link).screenshot_as_png)
                else:
                    pass
            except:
                break
            counter += 1

        for num, i in enumerate(range(1, int(self.total)+1)):
            path = join(r'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/text/' + f'text{i}.txt')
            self.decribe_car = driver.find_elements(By.XPATH,
                                                        f'//*[@id="root"]/div[1]/div[2]/form/div[5]/div/div[2]/div[{i}]')

            info = self.decribe_car[0].text
            with open(path, 'w') as f:
                f.write(info)

        self.get_small_icons()

    def get_small_icons(self):
        '''Arranging backgrounds for multi gallery'''
        self.new_icons = tk.PanedWindow(orient='vertical')
        Icons(self.new_icons)
        self.new_icons.place(x=950, y=60)

class Gallery(Page):
    '''Gallery window'''

    def __init__(self, root, *args, **kwargs):
        Page.__init__(self, root, *args, **kwargs)
        self.gallery = root
        self.get_text_field()
        self.get_input_text_field()
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
        file_menu.add_command(label="Start >", command=self.get_start_calc)
        file_menu.add_command(label="| << Prev", command=self.get_prev_photo)
        file_menu.add_command(label="Reset app", command=self.get_reset)
        file_menu.add_command(label="  ")
        file_menu.add_command(label="Contact", command=self.get_contact_form)

        # Help
        file_menu.add_cascade(label="  Help  ", menu=helpmenu)
        helpmenu.add_command(label="About program", command=self.get_about)
        helpmenu.add_command(label="About...", command=self.get_aboutUs)

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
        get_dir()

    def get_about(self):
        self.new_about = tk.PanedWindow(orient='vertical')
        AboutProgram(self.new_about)
        self.new_about.place(x=365, y=59.5)

    def get_aboutUs(self):
        self.new_aboutUs = tk.PanedWindow(orient='vertical')
        AboutProgramUs(self.new_aboutUs)
        self.new_aboutUs.place(x=365, y=59.5)

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
            result = f'Test text{link}\n' \
                     f'{self.decribe_car}'
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

            self.new_text = tk.PanedWindow(orient='vertical')
            self.new_text.place(x=300, y=560)
            result = f'Test text{link}\n' \
                     f'{self.decribe_car[0]}'
            tb = tk.Text(self.new_text, height=11, width=75)
            tb.pack(expand=True)
            tb.insert('end', result)
            tb.config(state='disabled')
        elif self.get_next_photo():
            self.counterUp = self.counterDown
        else:
            self.counter = 0

    def get_start_calc(self):
        self.get_hist()

    def get_hist(self):
        frame = tk.Frame()

        fig = Figure(figsize=(4.5, 3.83), dpi=100)

        linktext = r'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/text/*txt'

        # cheak empty file, true is empty
        self.y = []
        help_list = []
        for k in glob.glob(linktext):
            if os.path.getsize(k) > 0:
                with open(k, 'r') as f:
                    text = f.read()
                    self.Y = []
                    if 'zł' in text:
                        indeX = text.index('zł')
                        slicE = text[indeX-13:indeX]
                        indeX2 = slicE.index('\n')
                        slicE2 = slicE[indeX2:indeX]
                        indeX3 = slicE2.index(' ')
                        sliceE3 = slicE2[:indeX3]
                        sliceE4 = slicE2[indeX3+1:]
                        price = int(sliceE3+sliceE4)
                        self.y.append(price)
                        help_list.append(price)
                    else:
                        self.y.append((max(help_list)+min(help_list))/len(self.y))
            else:
                self.y.append((max(help_list)+min(help_list))/len(self.y))

        plot = fig.add_subplot(111)
        plot.plot(self.y)

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()

        toolbar = NavigationToolbar2Tk(canvas, frame)
        toolbar.update()

        frame.place(x=1370, y=500)
        canvas.get_tk_widget().place(x=1370, y=560)

    def get_text_field(self):
        self.new_text = tk.PanedWindow(orient='vertical')
        self.new_text.place(x=300, y=560)
        result = f'Information about the selected car:\n'
        tb = tk.Text(self.new_text, height=22, width=75)
        tb.pack(expand=True)
        tb.insert('end', result)
        tb.config(state='disabled')

    def get_input_text_field(self):
        self.tb = tk.Text(self.root, height=22, width=45)
        self.tb.place(x=950, y=560)

        result = f'My notes: \n'
        self.tb.insert('end', result)

        open_btn = tk.Button(self.root, text="Open File", command=self.get_open_file)
        open_btn.place(x=950, y=500)
        open_btn = tk.Button(self.root, text="Open Last", command=self.get_open_last)
        open_btn.place(x=1053, y=500)
        save_btn = tk.Button(self.root, text="Save File", command=self.save_text)
        save_btn.place(x=1157, y=500)
        save_btn = tk.Button(self.root, text="Clear", command=self.get_clear)
        save_btn.place(x=1255, y=500)

    def get_open_file(self):
        self.file_photo = filedialog.askopenfilename(initialdir=os.getcwd(), filetypes=[("text", ".txt")])
        pathh = tk.Entry(self.root)
        pathh.insert(tk.END, self.file_photo)
        tf = open(self.file_photo)
        data = tf.read()
        self.tb.insert(tk.END, data)
        tf.close()

    def get_open_last(self):
        self.link = r'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/save_txt/file.txt'
        text_file = open(self.link, "r")
        content = text_file.read()
        self.tb.insert(tk.END, content[9:])
        text_file.close()

    def save_text(self):
        self.link = r'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/save_txt/file.txt'
        f = asksaveasfile(initialfile='TXT Files',
                          defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
                          parent=self.root)
        f.write(self.tb.get(1.0, tk.END))

        text_file = open(self.link, "w")
        text_file.write(self.tb.get(1.0, tk.END))
        text_file.close()

    def get_clear(self):
        self.tb.delete(1.0, tk.END)
        self.get_input_text_field()

        dir_main = '/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/save_txt'
        filelistMain = glob.glob(os.path.join(dir_main, "*"))
        for files in filelistMain:
            os.remove(files)
