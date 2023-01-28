class Page:
    def __init__(self, root):
        self.root = root

        # Calling up methods
        self.get_set_window()

    def get_set_window(self):
        ''' Main window settings '''
        self.root.title('Porsche Cars, Program Created by Adrian Szklarski, 01.2023')
        self.root.wm_attributes('-zoomed', True)
        self.root.resizable(width=False, height=False)
