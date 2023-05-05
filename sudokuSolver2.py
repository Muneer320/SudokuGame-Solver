M = 9

def puzzle(a):
	for i in range(M):
		for j in range(M):
			print(a[i][j],end = " ")
		print()
        
def solve(grid, row, col, num):
	for x in range(9):
		if grid[row][x] == num:
			return False
		    
	for x in range(9):
		if grid[x][col] == num:
			return False


	startRow = row - row % 3
	startCol = col - col % 3
	for i in range(3):
		for j in range(3):
			if grid[i + startRow][j + startCol] == num:
				return False
	return True

def Suduko(grid, row, col):

	if (row == M - 1 and col == M):
		return True
	if col == M:
		row += 1
		col = 0
	if grid[row][col] > 0:
		return Suduko(grid, row, col + 1)
	for num in range(1, M + 1, 1): 
	
		if solve(grid, row, col, num):
		
			grid[row][col] = num
			if Suduko(grid, row, col + 1):
				return True
		grid[row][col] = 0
	return False

def fillGrid():
    '''0 means the cells where no value is assigned'''
    # grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
    # 		[5, 2, 0, 0, 0, 0, 0, 0, 0],
    # 		[0, 8, 7, 0, 0, 0, 0, 3, 1],
    # 		[0, 0, 3, 0, 1, 0, 0, 8, 0],
    # 		[9, 0, 0, 8, 6, 3, 0, 0, 5],
    # 		[0, 5, 0, 0, 9, 0, 6, 0, 0],
    # 		[1, 3, 0, 0, 0, 0, 2, 5, 0],
    # 		[0, 0, 0, 0, 0, 0, 0, 7, 4],
    # 		[0, 0, 5, 2, 0, 6, 3, 0, 0]]

    grid = []

    for x in range(1, 10):
        ''' Alternate way to fill grid but if you use this then after every entry you need a space. Ex. 1 0 0 0 2 0 0 0 4
        grid.append(list(map(int, input(
            f"Enter the values of your row {x} (write 0 for empty cells) >>> ").split())))
        '''
        val = input(f"Enter the values of your row {x} (write 0 for empty cells) >>> ")
        gridX = []
        for v in val:
            gridX.append(int(v))
        grid.append(gridX)

    for x in range(9):
        print()
        for y in grid[x]:
            print(y, end=' ')

    again = input("\nIs it correct? (Y/N) >>> ").capitalize()
    if 'N' in again:
        fillGrid()

    return grid

def main():
	grid = fillGrid()


	if (Suduko(grid, 0, 0)):
		print('\n', '*'*5, 'SOLUTION', '*'*5)
		puzzle(grid)
	else:
		print("No Solution exist:(")

	again = input("\nDo you want to try again (Y/N): ").lower()

	if again == 'y':
		main()


if __name__=="__main__":
	main()