import tkinter as tk
from tkinter import messagebox
import numpy as np
from SudokuSolver import solve_sudoku , solve_sudoku_genetic
import time

class SudokuGUI:
     def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.cells = [[tk.Entry(root, width=3,bg="white", font=('Arial', 18),
        justify='center', bd=3, relief='raised')
        for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()
        self.timer_label = tk.Label(root, text="Time: 0 sec", font=('Arial', 12))
        self.timer_label.grid(row=20, column=0, columnspan=10)

     def create_grid(self):
        for i in range(9):
            for j in range(9):
                if (i // 3 + j // 3) %2 == 0:
                    bg_color = '#ffe7f9' 
                else:
                    bg_color = '#fff7f1' 

                self.cells[i][j].grid(row=i, column=j, padx=2, pady=2)
                self.cells[i][j].config( bg=bg_color, highlightthickness=0)
            

    
     def create_buttons(self):
        solve_button = tk.Button(self.root, text="Solve with CSP",command=self.solve_csp, width=25, height=2 , bg="#ffcfcf" )
        solve_button.grid(row=10, column=0, columnspan=5, padx=5, pady=5)

        solve_genetic_button = tk.Button(self.root, text="Solve with GA",command=self.solve_genetic, width=25, height=2 , bg="#ffcfcf")
        solve_genetic_button.grid(row=10, column=5, columnspan=5, padx=5, pady=5)

        clear_button = tk.Button(self.root, text="Clear", command=self.clear_grid, width=12, height=2 , bg="#ffcfcf")
        clear_button.grid(row=11, column=0, columnspan=10, padx=5, pady=5)


     def clear_grid(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
        self.timer_label.config(text="Time: 0 sec")



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
        start_time = time.time()
        grid = self.get_grid()
        if solve_sudoku(grid):
            self.set_grid(grid)
            end_time = time.time()
            solve_time = end_time - start_time
            self.show_solve_time(solve_time)
        else:
            messagebox.showerror("Error", "No solution exists")

     def solve_genetic(self):
        start_time = time.time()
        grid = self.get_grid()
        grid = np.array(grid)
        solution = solve_sudoku_genetic(grid)
        self.set_grid(solution)
        end_time = time.time()
        solve_time = end_time - start_time
        self.show_solve_time(solve_time)
        
     def show_solve_time(self, solve_time):
        self.timer_label.config(text=f"Time: {solve_time:.4f} sec")
    
    
if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()