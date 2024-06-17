import tkinter as tk
from tkinter import messagebox
import numpy as np
from SudokuSolver import solve_sudoku , solve_sudoku_genetic

class SudokuGUI:
     def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.cells = [[tk.Entry(root, width=3,bg="#ffcc99", font=('Arial', 18),
        justify='center', bd=3, relief='raised')
        for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()

     def create_grid(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].grid(row=i, column=j, padx=3, pady=3)
                self.cells[i][j].config(highlightthickness=1.5, highlightbackground='gray')
    
     def create_buttons(self):
        solve_button = tk.Button(self.root, text="Solve with CSP",command=self.solve_csp, width=25, height=2 , bg="#ff9966" )
        solve_button.grid(row=10, column=0, columnspan=5, padx=5, pady=5)

        solve_genetic_button = tk.Button(self.root, text="Solve with GA",command=self.solve_genetic, width=25, height=2 , bg="#ff9966")
        solve_genetic_button.grid(row=10, column=5, columnspan=5, padx=5, pady=5)

        clear_button = tk.Button(self.root, text="Clear", command=self.clear_grid, width=12, height=2 , bg="#ffcc99")
        clear_button.grid(row=11, column=0, columnspan=10, padx=5, pady=5)


     def clear_grid(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)


     def get_grid(self):
        grid = []
        for row in range(9):
            current_row = []
            for col in range(9):
                value = self.cells[row][col].get()
                if value == '':
                    current_row.append(0)
                else:
                    current_row.append(int(value))
            grid.append(current_row)
        return grid   
     
     def set_grid(self, grid):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
                if grid[row][col] != 0:
                    self.cells[row][col].insert(0, grid[row][col])
    
     def solve_csp(self):
        grid = self.get_grid()
        if solve_sudoku(grid):
            self.set_grid(grid)
        else:
            messagebox.showerror("Error", "No solution exists")

     def solve_genetic(self):
        grid = self.get_grid()
        grid = np.array(grid)
        solution = solve_sudoku_genetic(grid)
        self.set_grid(solution)
        
    
if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()