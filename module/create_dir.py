import os, shutil

def get_clear_dir():
    path = r'/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/work_one_car_scale'
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        raise ValueError("file {} is not a file or dir.".format(path))


def get_dir():
    path = '/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/work_one_car_scale'
    isExist = os.path.exists(path)

    if isExist:
        pass
    else:
        directory = "work_one_car_scale"
        parent_dir = "/home/adrian/Pulpit/GitHub_Public/Selenium_Porsche/"
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        print("Directory '% s' created" % directory)

get_clear_dir()
get_dir()