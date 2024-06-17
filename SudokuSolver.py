def find_empty_location(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None


def is_safe(grid, row, col, num):
    if num in grid[row]:
        return False

    if num in [grid[i][col] for i in range(9)]:
        return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(grid):
    empty_loc = find_empty_location(grid)
    if not empty_loc:
        return True
    row, col = empty_loc

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True
            grid[row][col] = 0

    return False

class SudokuGA:
    def __init__(self, grid, population_size=100, generations=5000, mutation_rate=0.01):
        self.grid = grid
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.population = self.initialize_population()
    
    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            individual = self.create_individual()
            population.append(individual)
        return population
    


    def create_individual(self):
        individual = self.grid.copy()
        for row in range(9):
            available_numbers = set(range(1, 10)) - set(individual[row])
            for col in range(9):
                if individual[row][col] == 0:
                    individual[row][col] = random.choice(list(available_numbers))
                    available_numbers.remove(individual[row][col])
        return individual 
    
    def  fitness(self, individual):
        row_count = sum([len(set(row)) for row in individual])
        col_count = sum([len(set(col)) for col in np.transpose(individual)])
        subgrid_count = sum([len(set(individual[r:r+3, c:c+3].flatten())) for r in range(0, 9, 3) for c in range(0, 9, 3)])
        return row_count + col_count + subgrid_count

    def selection(self):
        weights = [self.fitness(ind) for ind in self.population]
        return random.choices(self.population, weights=weights, k=self.population_size)
          