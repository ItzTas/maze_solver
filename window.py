from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        
        self.__root = Tk()
        self.__root.title = ("Maze solver")
        self.__root.geometry(f"{width}x{height}")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
        self.canvas = Canvas(self.__root)
        self.canvas.pack(fill=BOTH, expand=True)
        self.isrunning = False
    
    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self) -> None:
        self.isrunning = True
        while self.isrunning:
            self.redraw()
    
    def close(self) -> None:
        self.isrunning = False
        