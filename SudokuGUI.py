import tkinter as tk
class SudokuGUI:
     def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.cells = [[tk.Entry(root, width=3,bg="#ffcc99", font=('Arial', 18),
        justify='center', bd=3, relief='raised')
        for _ in range(9)] for _ in range(9)]
        


if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()