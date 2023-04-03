import random


class Maze:

    def __init__(self, row: int, col: int, numOfTreasureBox: int):

        self.row = row  # to define border of maze
        self.col = col  # to define border of maze
        self.numOfTreasureBox = numOfTreasureBox  # nember of treasure boxes we are looking for
        self.grid = [[0 for x in range(col)] for y in
                     range(row)]  # maze consist of grids so each grid is created as number 0 in here
        self.treasure_boxes = []  # to store position of treasure boxes
        self.generate_walls_and_deadends()
        self.place_treasure_boxes()

    def generate_walls_and_deadends(self):
        for i in range(self.row):
            for j in range(self.col):
                # define a random number between 0-1 t generate walls and dead ends randomly
                if i == 0 and j == 0:
                    continue
                if random.random() < 0.2:
                    self.grid[i][j] = 1  # Walls are indicated with 1 in grid array
                elif random.random() < 0.1:
                    self.grid[i][j] = 2  # Dead ends are indicated with 2 in grid array

    def place_treasure_boxes(self):
        for i in range(self.numOfTreasureBox):
            x = random.randint(0, self.row - 1)
            y = random.randint(0, self.col - 1)
            if self.grid[x][y] == 0:
                self.grid[x][
                    y] = 3  # Treasure box are indicated with 3 in the grid array, position of them is randomly choosen
                self.treasure_boxes.append((x, y))  # to see the coordinates of boxes

 
    def collect_treasure(self):
        visited = [[False for _ in range(self.col)] for _ in range(self.row)] #to keep track grids that dfs visited already 
        
        def dfs(i, j, path):
            if i < 0 or i >= self.row or j < 0 or j >= self.col:
                return False  # Out of bounds
            if visited[i][j]:
                return False  # already visited so the function does not pass 2nd time on there
            if self.grid[i][j] == 1 or self.grid[i][j] == 2:
                return False  # Wall or dead end so the function does not go the grid that have those things
            if self.grid[i][j] == 3:
                path.append((i, j))  # append the position of treasure box to "path"
                return True
            visited[i][j] = True
            if dfs(i + 1, j, path) or dfs(i - 1, j, path) or dfs(i, j + 1, path) or dfs(i, j - 1, path):
                path.append((i, j))
                return True
        paths = []
        path = []
        while len(paths) < self.numOfTreasureBox and dfs(0, 0, path):
            paths.append(path)
            path = []
        return paths

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.grid])


maze = Maze(64,64,5)

print(maze)
print(maze.treasure_boxes)
print(maze.collect_treasure())
