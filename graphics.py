from tkinter import Tk, BOTH, Canvas

class Window():
        def __init__(self, width, height) -> None:
            self.__root = Tk()
            self.__root.title = ("Maze solver")
            self.__root.protocol("WM_DELETE_WINDOW", self.close)
            self.canvas = Canvas(self.__root,bg="white", height=height, width=width)
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
            
        def draw_line(self, line: object, fill_color="black") ->None:
            line.draw(self.canvas, fill_color)
  
class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
            
class Line():
    def __init__(self, pointA: object, pointB: object) -> None:
        self.pointA = pointA
        self.pointB = pointB
        
    def draw(self, canvas, fill_color="black") -> None:
        canvas.create_line(
            self.pointA.x, self.pointA.y, self.pointB.x, self.pointB.y, fill=fill_color, width=2
        )   
            