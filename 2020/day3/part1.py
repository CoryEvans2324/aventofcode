

class Map:
    def __init__(self, raw_map: str) -> None:

        self.grid = raw_map.strip().splitlines()
        self.row_width = len(self.grid[0])

        self.num_of_rows = len(self.grid)


    def is_tree_at_pos(self, row, col):
        return self.grid[row][col % self.row_width] == '#'


def main():
    with open('input.txt') as f:
        grid = Map(f.read())

    row_counter = 0
    col_counter = 0

    tree_counter = 0

    while row_counter < grid.num_of_rows - 1:
        row_counter += 1
        col_counter += 3

        if grid.is_tree_at_pos(row_counter, col_counter):
            tree_counter += 1

    print(tree_counter)

if __name__ == "__main__":
    main()
