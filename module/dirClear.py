# clear "work_dir"
import os, glob


def get_clear_dir():
    dir_main = '/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/work_dir'
    dir_copy = '/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/work_dir_scale'
    dir_text = '/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/text'

    filelistMain = glob.glob(os.path.join(dir_main, "*"))
    filelistCopy = glob.glob(os.path.join(dir_copy, "*"))
    filelistText= glob.glob(os.path.join(dir_text, "*"))


    for files in filelistMain:
        os.remove(files)

    for files in filelistCopy:
        os.remove(files)

    for files in filelistText:
        os.remove(files)

get_clear_dir()
