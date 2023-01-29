import tkinter as tk
from PIL import Image, ImageTk
import glob

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
        vertibar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        vertibar.pack(side=tk.RIGHT, fill=tk.Y)
        vertibar.config(command=self.my_canvas.yview)

        self.my_canvas.config(yscrollcommand=vertibar.set)
        self.my_canvas.pack(expand=True, side=tk.LEFT, fill=tk.BOTH)

        self.get_icons()

    def get_icons(self):
        '''Method to add a mini gallery'''
        pass

if __name__ == '__main__':
    root = tk.Tk()
    Icons(root)
    root.mainloop()
