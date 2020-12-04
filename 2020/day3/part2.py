

class Map:
    def __init__(self, raw_map: str) -> None:

        self.grid = raw_map.strip().splitlines()
        self.row_width = len(self.grid[0])

        self.num_of_rows = len(self.grid)


    def is_tree_at_pos(self, row, col):
        return self.grid[row][col % self.row_width] == '#'

    def count(self, row_step, col_step) -> int:
        row_counter = 0
        col_counter = 0

        tree_counter = 0

        while row_counter < self.num_of_rows - 1:
            row_counter += row_step
            col_counter += col_step

            if self.is_tree_at_pos(row_counter, col_counter):
                tree_counter += 1

        return tree_counter


def main():
    with open('input.txt') as f:
        grid = Map(f.read())

    total = 1

    total *= grid.count(1, 1)
    total *= grid.count(1, 3)
    total *= grid.count(1, 5)
    total *= grid.count(1, 7)
    total *= grid.count(2, 1)

    print(total)

if __name__ == "__main__":
    main()
