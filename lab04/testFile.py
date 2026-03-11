from Stack import Stack
from lab04 import solveMaze

def test_example():
	maze = [
    ['+','+','+','+','G','+'],
    ['+',' ','+',' ',' ','+'],
    ['+',' ',' ',' ','+','+'],
    ['+',' ','+','+',' ','+'],
    ['+',' ',' ',' ',' ','+'],
    ['+','+','+','+','+','+'] ]
	assert solveMaze(maze, 4, 4) == True
	assert maze == [
    ['+', '+', '+', '+', 'G', '+'],
    ['+', 8, '+', 11, 12, '+'],
    ['+', 7, 9, 10, '+', '+'],
    ['+', 6, '+', '+', 2, '+'],
    ['+', 5, 4, 3, 1, '+'],
    ['+', '+', '+', '+', '+', '+'] ]
	
def test_noSolution():
	maze = [
    ['+','+','+','+','+','+','+','+','+','+'],
    ['+',' ',' ',' ','+',' ',' ',' ',' ','+'],
    ['+',' ','+',' ','+',' ','+','+','+','+'],
    ['+',' ','+',' ',' ',' ',' ',' ',' ','+'],
    ['+',' ','+','+','+','+','+','+',' ','+'],
    ['+',' ',' ',' ',' ','+',' ',' ',' ','+'],
    ['+','+','+','+',' ','+',' ','+',' ','+'],
    ['+',' ',' ',' ',' ','+',' ','+',' ','+'],
    ['+',' ','+','+',' ',' ',' ','+',' ','+'],
    ['+','+','+','+','+','+','+','+','+','+'] ]
	assert solveMaze(maze, 1, 1) == False
	
def test_straightPath():
	maze = [
    ["+", "+", "+"],
    ["+", " ", "+"],
    ["+", " ", "+"],
    ["+", " ", "+"],
    ["+", " ", "+"],
    ["+", "G", "+"],
    ["+", "+", "+"]]
	assert solveMaze(maze, 1, 1) == True
	assert maze == [
    ["+", "+", "+"],
    ["+", 1, "+"],
    ["+", 2, "+"],
    ["+", 3, "+"],
    ["+", 4, "+"],
    ["+", "G", "+"],
    ["+", "+", "+"]]
	
def test_openSpace_noSoln():
	maze = [
    ['+', '+', '+', '+', '+'],
    ['+', ' ', ' ', ' ', '+'],
    ['+', ' ', ' ', ' ', '+'],
    ['+', ' ', ' ', ' ', '+'],
    ['+', '+', '+', '+', '+']]
	assert solveMaze(maze, 1, 1) == False
	
def test_openSpace():
	maze = [
    ['+', '+', '+', '+', '+'],
    ['+', ' ', ' ', ' ', '+'],
    ['+', 'G', ' ', ' ', '+'],
    ['+', ' ', ' ', ' ', '+'],
    ['+', '+', '+', '+', '+']]	
	assert solveMaze(maze, 1, 1) == True
	



def test_insertIntoStack():
    s = Stack()
    s.push("There")
    s.push("Hi")
    assert s.size() == 2
    assert s.peek() == "Hi"
    assert s.isEmpty() == False

def test_deleteFromStack():
    s = Stack()
    s.push("There")
    s.push("Hi")
    x = s.pop()
    assert x == "Hi"
    assert s.peek() == "There"
    assert s.size() == 1
    assert s.isEmpty() == False
    y = s.pop()
    assert y == "There"
    assert s.size() == 0
    assert s.isEmpty() == True