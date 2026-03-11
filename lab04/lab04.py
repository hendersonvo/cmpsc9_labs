from Stack import Stack

# def printMaze(maze):
# 	for row in range(len(maze)):
# 		for col in range(len(maze[0])):
# 			print("|{:<2}".format(maze[row][col]), sep='',end='')
# 		print("|")
# 	return

def solveMaze(maze, startX, startY):
    visits = Stack()
    visits.push([startX, startY])
    steps = 0
    pos = visits.peek() 
    
    while maze[visits.peek()[0]][visits.peek()[1]] != "G":
        
        if maze[visits.peek()[0]][visits.peek()[1]] == " ":
            steps += 1
            maze[visits.peek()[0]][visits.peek()[1]] = steps

        if maze[visits.peek()[0]-1][visits.peek()[1]] == " " or maze[visits.peek()[0]-1][visits.peek()[1]] == "G":
            pos = [visits.peek()[0]-1, visits.peek()[1]]
            visits.push(pos)

        elif maze[visits.peek()[0]][visits.peek()[1] - 1] == " " or maze[visits.peek()[0]][visits.peek()[1] - 1] == "G":
            pos = [visits.peek()[0], visits.peek()[1] - 1]
            visits.push(pos)

        elif maze[visits.peek()[0] + 1][visits.peek()[1]] == " " or maze[visits.peek()[0] + 1][visits.peek()[1]] == "G":
            pos = [visits.peek()[0] + 1, visits.peek()[1]]
            visits.push(pos)

        elif maze[visits.peek()[0]][visits.peek()[1] + 1] == " " or maze[visits.peek()[0]][visits.peek()[1] + 1] == "G":
            pos = [visits.peek()[0], visits.peek()[1] + 1]
            visits.push(pos)

        else: 
            visits.pop()

        if visits.size() == 0:
            # printMaze(maze)
            return False
    # printMaze(maze)
    return True


# maze = [['G'], [' '], [' '], [' ']]

# maze = [
#     ["+", "+", "+"],
#     ["+", " ", "+"],
#     ["+", " ", "+"],
#     ["+", " ", "+"],
#     ["+", " ", "+"],
#     ["+", "G", "+"],
#     ["+", "+", "+"]
# ]

# maze = [
# ['+','+','+','+','G','+'],
# ['+',' ','+',' ',' ','+'],
# ['+',' ',' ',' ','+','+'],
# ['+',' ','+','+',' ','+'],
# ['+',' ',' ',' ',' ','+'],
# ['+','+','+','+','+','+'] ]

# maze = [
#     ['+','+','+','+','+','+','+','+','+','+'],
#     ['+',' ',' ',' ','+',' ',' ',' ',' ','+'],
#     ['+',' ','+',' ','+',' ','+','+','+','+'],
#     ['+',' ','+',' ',' ',' ',' ',' ',' ','+'],
#     ['+',' ','+','+','+','+','+','+',' ','+'],
#     ['+',' ',' ',' ',' ','+',' ',' ',' ','+'],
#     ['+','+','+','+',' ','+',' ','+',' ','+'],
#     ['+',' ',' ',' ',' ','+',' ','+',' ','+'],
#     ['+',' ','+','+',' ',' ',' ','+','G','+'],
#     ['+','+','+','+','+','+','+','+','+','+']
# ]

# maze = [
#     ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+'],
#     ['+', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '+'],
#     ['+', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '+'],
#     ['+', ' ', ' ', ' ', ' ', ' ', 'G', ' ', ' ', '+'],
#     ['+', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '+'],
#     ['+', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '+'],
#     ['+', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '+'],
#     ['+', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '+'],
#     ['+', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '+'],
#     ['+', '+', '+', '+', '+', '+', '+', '+', '+', '+']
# ]

# print(solveMaze(maze, 1, 1))

    




    