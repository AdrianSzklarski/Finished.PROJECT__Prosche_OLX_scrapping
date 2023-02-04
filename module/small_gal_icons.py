import tkinter as tk
from PIL import Image, ImageTk
import glob, pyautogui
import pyautogui as py #Import pyautogui
import time



# Photo sizes
SIZE_X = 150

SIZE_Y = 100


class Icons:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.grid()

        sickPaths = glob.glob(
            r'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/work_dir/*.png')
        self.tableCars = []
        [self.tableCars.append(cars) for cars in sickPaths]
        self.number = len(self.tableCars)

        # Dimensions of the window
        self.my_canvas = tk.Canvas(self.frame, width=850, height=400, bg='#d8d8d9',
                                   scrollregion=(0, 0, 1000, SIZE_Y * round(self.number / 5)))

        self.my_canvas.configure(scrollregion=(0, 0, 850, (self.number/5)*160))
        vertibar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        vertibar.pack(side=tk.RIGHT, fill=tk.Y)
        vertibar.config(command=self.my_canvas.yview)

        self.my_canvas.config(yscrollcommand=vertibar.set)
        self.my_canvas.pack(expand=True, side=tk.LEFT, fill=tk.BOTH)
        # self.get_mouse()
        self.get_icons()



    def get_icons(self):
        '''Method to add a mini gallery'''

        # Scale images and download them for display
        link = r'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/work_dir/*png'
        number_of_photos = len(glob.glob(link))
        photos = glob.glob(link)
        if number_of_photos != 0:
            for no, n in enumerate(photos):
                image = Image.open(n).resize((SIZE_X, SIZE_Y), Image.ANTIALIAS)
                image.save(fp=f'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/work_one_car_scale/One_Car{no}.png')
        else:
            tk.Label(self.root, text='I am sorry, this directory is empty!').place(x=1000, y=156)

        # scale photo
        link = r'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/work_one_car_scale/*png'
        cars = glob.glob(link)

        self.tab_render = []
        for car in cars:
            load = Image.open(car)
            self.render = ImageTk.PhotoImage(load)
            img = tk.Label(self.root, image=self.render)
            img.image = self.render
            self.tab_render.append(self.render)

            self.counter = -1

        if self.number <= 5:  # below 5 photos
            for i in range(1, self.number + 1):
                self.my_canvas.create_image(-165 + i * 170, 10, image=self.tab_render[i], anchor="nw")
        elif self.number > 5:  # over 5 photos
            k = int()
            y = []
            for i in range(0, self.number + 1):
                if i % 5 == 0:  # switch to a new line
                    k = i
                y.append(k)

            for j in range(0, self.number):
                self.counter += 1  # to count 5 elements in a row
                if (15 + self.counter * 180) <= 735:
                    # "y[j] * 25" move to a new row
                    self.my_canvas.create_image(15 + self.counter * 170, 10 + y[j] * 25,
                                                image=self.tab_render[j],
                                                anchor="nw")
                    # print(self.tab_render[j])
                else:
                    self.counter = 0
                    self.my_canvas.create_image(15 + self.counter * 170, 10 + y[j] * 25,
                                                image=self.tab_render[j],
                                                anchor="nw")

            else:
                tk.Label(self.root, text='Wrong Value').place(x=1000, y=156)

    # def get_mouse(self):
    #     # current mouse x and y
    #     print(pyautogui.position())
    #     # current screen resolution width and height
    #     print(pyautogui.size())

        # print('Press Ctrl-C to quit.')
        # try:
        #     while True:
        #         print(py.position())
        #         time.sleep(5)
        # except KeyboardInterrupt:
        #     print('\n')


if __name__ == '__main__':
    root = tk.Tk()
    Icons(root)
    root.mainloop()
