from functions import *

# time and type of game
gameType = input("vsPlayer or vsComputer? ").lower()
verifiedGameType = verify_game_type(gameType)
gameTime = input("How many times would you like to play? ")
print("")  # to put and empty line between gametime input line and the next line
verifiedGameTime = verify_game_time(gameTime)

for i in range(1, verifiedGameTime + 1):
    if verifiedGameType == "vsplayer":
        # vsPlayer game
        PlayersMoveFirst = input("Enter the first move Rock/Raper/Scissors: ").lower()
        PlayerMoveSecond = input("Enter the second move Rock/Paper/Scissors: ").lower()
        verifiedMoves = verify_pmoves_vsplayer_game(PlayersMoveFirst, PlayerMoveSecond)
        verifiedPlayerMoveFirst = verifiedMoves[0]
        verifiedPlayerMoveSecond = verifiedMoves[1]
        finalResultVSPLA = verify_final_result_vspla_game(verifiedMoves[0], verifiedMoves[1])
        print(f"The first players move was {verifiedPlayerMoveFirst}")
        print(f"The second players move was {verifiedPlayerMoveSecond}")
        print(finalResultVSPLA)
        # score board
        scoreBoard = score_board_vsplayer(finalResultVSPLA)
        print(f'First players win count: {scoreBoard[0]}')
        print(f'Second players win count: {scoreBoard[1]}')
        print(f'''Ties count: {scoreBoard[2]}
            
            ''')

    elif verifiedGameType == "vscomputer":
        # vsComputer game
        playerMove = input("Enter a move Rock/Raper/Scissors: ").lower()
        verifiedPlayerMove = verify_player_move_vscomputer_game(playerMove)
        verifiedComputerMove = verify_computer_move_vscomputer_game()
        finalResultVSCOM = verify_final_result_vscom_game(verifiedPlayerMove, verifiedComputerMove)
        print(f"Your move was: {verifiedPlayerMove}")
        print(f"The computers move was: {verifiedComputerMove}")
        print(finalResultVSCOM)

        # score board
        scoreBoard2 = score_board_vscomputer(finalResultVSCOM)
        print(f"The players win count: {scoreBoard2[0]}")
        print(f"The players lose count: {scoreBoard2[1]}")
        print(f"""Ties count: {scoreBoard2[2]}
              
              """)

