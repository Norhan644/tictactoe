import itertools


def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
            

    #Horizontal
    for row in game:
        print(row)
    if row.count(row[0])== len(row) and row[0] != 0:
    #if all_same(row):
        print(f"player {row[0]} is the winner horrizontly!")
        return True

    #Diagonal
    diags = []
    for row, col in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"player {diags[0]} is the winner diagonally!")
        return True

# for rows, cols in zip(list(reversed(range(len(game)))), range(len(game))):
#     print(rows, cols)    
    diag = []
    for ix in range(len(game)):
        diag.append(game[ix][ix])
    if all_same(diags):
        print(f"player {diags[0]} is the winner diagonally!")
        return True

    #Vertical
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
    #if check.count(check[0])== len(check) and check[0] != 0:
    if all_same(check):
        print(f"player {check[0]} is the winner vertically!")
        return True
    return False


def game_board(game_map, player=2, row=0, column=0, Just_display= False):
    try:
        if game_map[row][column] !=0:
            print("choose another")
            return game_map, False
        #print("     1  2  3")
        print("   " + "  ".join([str(i) for i in range(len(game_map))])) ##gameSize
        if not Just_display :
            game_map[row][column] = player
        for  count, row in enumerate(game_map):  #enumerate built in func that return index
            print(count, row)
        return game_map, True

    except IndexError as e:    #out of index
        print("Error: make sure you input row/column as 0, 1 or 2?", e)
        return False
    except Exception as e:     #pass wrong parameter
        print("something went very wrong!!!")
        return game_map, False

play = True
players = [1, 2]
while play:
    game_size = int(input("what size game of tic tac toe?"))       
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game, Just_display=True)
    player_choice = itertools.cycle([1, 2])

    while not game_won:
        current_player = next(player_choice)
        print(f"current plaer:{current_player}")
        played = False

        while not played:
            column_choise = int(input("what column do you want to play?"))
            row_choise = int(input("what row do you want to play?"))
            game, played = game_board(game, current_player, row_choise, column_choise)
        
        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again(y/n)")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("Byeeeeeeee")
                play = False 
            else:
                print("not a valid ansower ")
                play = False
        