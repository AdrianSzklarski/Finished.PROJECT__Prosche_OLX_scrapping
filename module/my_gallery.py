import tkinter as tk
from PIL import Image, ImageTk
import glob


class MyGalleryOfCars:
    def __init__(self, root):
        self.root = root
        self.root.config(width=300, height=200)
        self.root.title("Secondary Window")
        self.root.focus()

    def get_read_photo(self):
        '''Created a "work_dir_scale" directory'''
        sickPaths = glob.glob(
            r'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/work_dir/*.png')
        self.tableCars = []
        [self.tableCars.append(cars) for cars in sickPaths]

        # This is numeration only, save cars to dir
        for i in range(0, len(self.tableCars)):
            load = Image.open(sickPaths[i])
            image = load.resize((600, 400), Image.ANTIALIAS)
            image.save(fp=f'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/work_dir_scale/Porsche_{i+1}.png')

        return len(self.tableCars)
