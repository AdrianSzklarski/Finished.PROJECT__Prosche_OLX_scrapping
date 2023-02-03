# clear "work_dir"
import os, glob


def get_clear_dir():
    dir_main = '/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/work_dir'
    dir_copy = '/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/work_dir_scale'

    filelistMain = glob.glob(os.path.join(dir_main, "*"))
    filelistCopy = glob.glob(os.path.join(dir_copy, "*"))


    for files in filelistMain:
        os.remove(files)

    for files in filelistCopy:
        os.remove(files)


get_clear_dir()
