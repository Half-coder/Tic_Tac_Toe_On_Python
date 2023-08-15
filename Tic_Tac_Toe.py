import random
map = [
       "e", "e", "e",
       "e", "e", "e",
       "e", "e", "e"]
win_maps_player = [
    [
       "X", "e", "e",
       "e", "X", "e",
       "e", "e", "X"
    ],
    [
       "e", "e", "X",
       "e", "X", "e",
       "X", "e", "e"
    ],
    [
       "X", "X", "X",
       "e", "e", "e",
       "e", "e", "e"
    ],
    [
       "e", "e", "e",
       "X", "X", "X",
       "e", "e", "e"
    ],
    [
       "e", "e", "e",
       "e", "e", "e",
       "X", "X", "X"
    ],
    [
       "X", "e", "e",
       "X", "e", "e",
       "X", "e", "e"
    ],
    [
       "e", "X", "e",
       "e", "X", "e",
       "e", "X", "e"
    ],
    [
       "e", "e", "X",
       "e", "e", "X",
       "e", "e", "X"
    ]          
]
win_maps_bot = [
    [
       "O", "e", "e",
       "e", "O", "e",
       "e", "e", "O"
    ],
    [
       "e", "e", "O",
       "e", "O", "e",
       "O", "e", "e"
    ],
    [
       "O", "O", "O",
       "e", "e", "e",
       "e", "e", "e"
    ],
    [
       "e", "e", "e",
       "O", "O", "O",
       "e", "e", "e"
    ],
    [
       "e", "e", "e",
       "e", "e", "e",
       "O", "O", "O"
    ],
    [
       "O", "e", "e",
       "O", "e", "e",
       "O", "e", "e"
    ],
    [
       "e", "O", "e",
       "e", "O", "e",
       "e", "O", "e"
    ],
    [
       "e", "e", "O",
       "e", "e", "O",
       "e", "e", "O"
    ] 
]
player_turn = False
bot_turn = False
check_win = True
retry_bot = True
retry_plr = False
start_while = True
exit_from_program = False

print("Welcome to tic tac toe!\n", "Enter word play to start game!")
data = str(input())
if data == "play":
    player_turn = True
    while start_while:     
        if player_turn:
            player_turn = True
            bot_turn = False
            print(f"Your turn: \n {map[0], map[1], map[2]}\n {map[3], map[4], map[5]}\n {map[6], map[7], map[8]}")
            data_2 = int(input())
            data_2 -= 1
            if(map[data_2] != "X" and data_2 != "O"):
                  map[data_2] = "X"      
            else:
                  print("This cell dont empty!")
            print(f"Your turn: {player_turn}\n {map[0], map[1], map[2]}\n {map[3], map[4], map[5]}\n {map[6], map[7], map[8]}")
            bot_turn = True

        if bot_turn and retry_bot == True:
            player_turn = False
            bot_turn = True
            variants = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            random.shuffle(variants)
            result = random.choice(variants)
            if map[result] == "e" and map[result] != "O" and map[result] != "X":
                  map[result] = "O"
            else:
                  retry_bot = True
            
            player_turn = True
            check_win = True    
                      
            print(f"Bot turn: \n {map[0], map[1], map[2]}\n {map[3], map[4], map[5]}\n {map[6], map[7], map[8]}")
        if exit_from_program == True:
              exit()   
    
        if check_win == True:
              #Проверка игрока
              if map[0] == win_maps_player[0][0] and map[4] == win_maps_player[0][4] and map[8] == win_maps_player[0][8]:
                    player_turn = False
                    bot_turn = False
                    print("Player win!")
                    exit_from_program = True 
              elif map[2] == win_maps_player[1][2] and map[4] == win_maps_player[1][4] and map[6] == win_maps_player[1][6]:
                    player_turn = False
                    bot_turn = False
                    print("Player win!")
                    exit_from_program = True 
              elif map[0] == win_maps_player[2][0] and map[1] == win_maps_player[2][1] and map[2] == win_maps_player[2][2]:
                    player_turn = False
                    bot_turn = False
                    print("Player win!")
                    exit_from_program = True 
              elif map[3] == win_maps_player[3][3] and map[4] == win_maps_player[3][4] and map[5] == win_maps_player[3][5]:
                    player_turn = False
                    bot_turn = False
                    print("Player win!")
                    exit_from_program = True 
              elif map[6] == win_maps_player[4][6] and map[7] == win_maps_player[4][7] and map[8] == win_maps_player[4][8]:
                    player_turn = False
                    bot_turn = False
                    print("Player win!")
                    exit_from_program = True 
              elif map[0] == win_maps_player[0][0] and map[4] == win_maps_player[0][4] and map[8] == win_maps_player[0][8]:
                    player_turn = False
                    bot_turn = False
                    print("Player win!")
                    exit_from_program = True 
              elif map[0] == win_maps_player[5][0] and map[3] == win_maps_player[5][3] and map[6] == win_maps_player[5][6]:
                    player_turn = False
                    bot_turn = False
                    print("Player win!")
                    exit_from_program = True 
              elif map[1] == win_maps_player[6][1] and map[4] == win_maps_player[6][4] and map[7] == win_maps_player[6][7]:
                    player_turn = False
                    bot_turn = False
                    print("Player win!")
                    exit_from_program = True 
              elif map[2] == win_maps_player[7][2] and map[5] == win_maps_player[7][5] and map[8] == win_maps_player[7][8]:
                    player_turn = False
                    bot_turn = False
                    print("Player win!")
                    exit_from_program = True      

              #Проверка бота на выигрыш
              elif map[2] == win_maps_bot[1][2] and map[4] == win_maps_bot[1][4] and map[6] == win_maps_bot[1][6]:
                    player_turn = False
                    bot_turn = False
                    print("Bot win!")
                    exit_from_program = True 
              elif map[0] == win_maps_bot[2][0] and map[1] == win_maps_bot[2][1] and map[2] == win_maps_bot[2][2]:
                    player_turn = False
                    bot_turn = False
                    print("Bot win!")
                    exit_from_program = True 
              elif map[3] == win_maps_bot[3][3] and map[4] == win_maps_bot[3][4] and map[5] == win_maps_bot[3][5]:
                    player_turn = False
                    bot_turn = False
                    print("Bot win!")
                    exit_from_program = True 
              elif map[6] == win_maps_bot[4][6] and map[7] == win_maps_bot[4][7] and map[8] == win_maps_bot[4][8]:
                    player_turn = False
                    bot_turn = False
                    print("Bot win!")
                    exit_from_program = True 
              else:
                    check_win = False
