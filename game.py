
board = ["   " for x in range(9)]

def print_board():
	for i in range(3):
		#print(i)
		print("|{}|{}|{}|".format(board[(i+1)*3-3],board[(i+1)*3-2],board[(i+1)*3-1])) 	

def modify_board(symbol):
	user = 0	
	if symbol == 'X':
		user = 1
	elif symbol == 'O':
		user = 2
	pos = int(input("At which position you would like to entre :- player{}?:".format(user)).strip())	
	
	while board[pos-1] != "   ":
		print()
		print("You can't enter in that position!")
		print()
		pos = int(input("At which position you would like to entre :- player{}?:".format(user)).strip())
	else:		
		board[pos-1] = " " + symbol + " "

def is_draw(symbol):
	if not "   " in board:
		print("It's draw!")
		return True
	else: 
		return False
def is_win(sym):
	symbol = " " + sym + " " 
	user = 0	
	if symbol == ' X ':
		user = 1
	elif symbol == ' O ':
		user = 2
	if  (board[0] == symbol and board[1] == symbol and board[2] == symbol) or \
		(board[3] == symbol and board[4] == symbol and board[5] == symbol) or \
		(board[6] == symbol and board[7] == symbol and board[8] == symbol) or \
		(board[0] == symbol and board[3] == symbol and board[6] == symbol) or \
		(board[1] == symbol and board[4] == symbol and board[7] == symbol) or \
		(board[2] == symbol and board[5] == symbol and board[8] == symbol) or \
		(board[0] == symbol and board[4] == symbol and board[8] == symbol) or \
		(board[2] == symbol and board[4] == symbol and board[6] == symbol):
			print("Player {} wins!".format(user));
			return True
	else:
		return False
				
while True:	
	print_board()
	modify_board('X')
	if is_win('X'):
		con = input("Do you want to play again?(Y/n):").lower().strip()
		if con == 'y':
			for i in range(9):
				board[i] = "   "
			continue
		else:
			break
	if is_draw('X'):
		con = input("Do you want to play again?(Y/n):").lower().strip()
		if con == 'y':
			for i in range(9):
				board[i] = "   "
			continue
		else:
			break
	print_board()
	modify_board('O')
	if is_win('O'):
		con = input("Do you want to play again?(Y/n):").lower().strip()
		if con == 'y':
			for i in range(9):
				board[i] = "   "
			continue
		else:
			break
	if is_draw('O'):
		con = input("Do you want to play again?(Y/n):").lower().strip()
		if con == 'y':
			continue
		else:
			break
	
