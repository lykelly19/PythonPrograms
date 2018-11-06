# In progress creating a 5 x 4 Tic Tac Toe Game

game = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]];

def game_board(game_map, player=0, row=0, column=0, just_display=False):
  try:
    if not just_display:
      game_map[row][column] = player;
    print("   a  b  c  d  e")
    for count, row in enumerate(game_map):
      print(count, row)
    return game_map
  except IndexError as e:
    print("Error: Make sure you input row/column as 0, 1, or 2?", e)
  except Exception as e:
    print("Something went wrong!", e)


#inputX = int(input("Enter row: "))
#inputY = int(input("Enter column: "))
#game = game_board(game,player=1,row=inputX,column=inputY)

game = game_board(game,just_display = True)
