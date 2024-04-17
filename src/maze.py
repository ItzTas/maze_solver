from cell import Cell

import time

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
        ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
    
    def _create_cells(self) -> None:
        self.cells = []
        for c in range(self.num_rows):
            row = []
            for i in range(self.num_cols):
                row.append(Cell(self.win))
            self.cells.append(row)
        
        for i in range(len(self.cells)):
            row = self.cells[i]
            for j in range(len(row)):
                self._draw_cell(i, j)   
    
    def _draw_cell(self, i, j) -> None:
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
        
    def _animate(self) -> None:
        if self.win is None:
            return  
        self.win.redraw()
        time.sleep(0.05)