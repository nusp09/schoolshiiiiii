grid = [
    ["","",""],
    ["","",""],
    ["","",""]
]
def display_grid(grid):
    print("",grid[0][0],"|",grid[0][1],"|",grid[0][2],"\n","---------","\n",grid[1][0],"|",grid[1][1],"|",grid[1][2],"\n","---------","\n",grid[2][0],"|",grid[2][1],"|",grid[2][2])
    return
def check_winner(grid):
    if grid[0][0] == grid[0][1] == grid[0][2] and grid[0][0] != "":
        return grid[0][0]
    if grid[1][0] == grid[1][1] == grid[1][2] and grid[1][0] != "":
        return grid[1][0]
    if grid[2][0] == grid[2][1] == grid[2][2] and grid[2][0] != "":
        return grid[2][0]
    if grid[0][0] == grid[1][0] == grid[2][0] and grid[0][0] != "":
        return grid[0][0]
    if grid[0][1] == grid[1][1] == grid[2][1] and grid[0][1] != "":
        return grid[0][1]
    if grid[0][2] == grid[1][2] == grid[2][2] and grid[0][2] != "":
        return grid[0][2]
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != "":
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != "":
        return grid[0][2]
    return False

print("Welcome to Tic Tac Toe")
while check_winner(grid) == False:
    print("x's turn")
    while True:
        row = int(input("Enter the row number you want to enter into: ")) - 1
        col = int(input("Enter the column number you want to enter into: ")) -1
        if grid[row][col] != "":
            print("That spot is already taken")
            continue
        else:
            grid[row][col] = "x"
            break
    display_grid(grid)
    if check_winner(grid) == "x":
        print("x wins")
        break
    print("o's turn")
    while True:
        row = int(input("Enter the row number you want to enter into: ")) - 1
        col = int(input("Enter the column number you want to enter into: ")) - 1
        if grid[row][col] != "":
            print("That spot is already taken")
            continue
        else:
            grid[row][col] = "o"
            break
    display_grid(grid)
    if check_winner(grid) == "o":
        print("o wins")
        break
print("game over")
