import random

scoresVSPlayer = {
    'fwin': 0,
    'swin': 0,
    'ties': 0
}
scoresVSComputer = {
    'pwin': 0,
    'plose': 0,
    'tie': 0
}
results = {
    'tieResult': "Its a tie! ",
    'FWinResult': "The first player wins! ",
    'SWinResult': "The second player wins! ",
    'WinResult': "You win! ",
    'LoseResult': "You lose! "
}
options = ["rock", "paper", "scissors"]


def verify_game_time(entry):
    if entry.isdigit():
        return int(entry)
    while not entry.isdigit():
        print("please choose a correct option")
        entry2 = input("How many times would you like to play? ")
        if entry2.isdigit():
            return int(entry2)


def verify_game_type(entry):
    if entry in ["vsplayer", "vscomputer"]:
        return entry
    while entry not in ["vsplayer", "vscomputer"]:
        print("please choose a correct game type")
        entry2 = input("vsPlayer or vsComputer? ")
        if entry2 in ["vsplayer", "vscomputer"]:
            return entry2


def verify_pmoves_vsplayer_game(entry1, entry2):
    if entry1 in options and entry2 in options:
        return [entry1, entry2]
    while entry1 not in options or entry2 not in options:
        print("please choose a correct move")
        reentry1 = input("Enter the first move rock/paper/scissors: ")
        reentry2 = input("Enter the first move rock/paper/scissors: ")
        if reentry1 and reentry2 in options:
            return [reentry1, reentry2]


def verify_player_move_vscomputer_game(entry):
    if entry in options:
        return entry
    while entry not in options:
        print("please choose a correct move")
        reentry = input("Enter a move Rock/Raper/Scissors: ")
        if reentry in options:
            return reentry


def verify_computer_move_vscomputer_game():
    randop = random.choice(options)
    return randop


def verify_final_result_vspla_game(p1, p2):
    res = ''
    if p1 == p2:
        res = results['tieResult']
    elif p1 == "rock" and p2 == "paper":
        res = results['SWinResult']
    elif p1 == "rock" and p2 == "scissors":
        res = results['FWinResult']
    elif p1 == "paper" and p2 == "rock":
        res = results['FWinResult']
    elif p1 == "paper" and p2 == "scissors":
        res = results['SWinResult']
    elif p1 == "scissors" and p2 == "rock":
        res = results['SWinResult']
    elif p1 == "scissors" and p2 == "paper":
        res = results['FWinResult']
    return res


def verify_final_result_vscom_game(pm, cm):
    res = ''
    if pm == cm:
        res = results['tieResult']
    elif pm == "rock" and cm == "paper":
        res = results['LoseResult']
    elif pm == "rock" and cm == "scissors":
        res = results['WinResult']
    elif pm == "paper" and cm == "rock":
        res = results['WinResult']
    elif pm == "paper" and cm == "scissors":
        res = results['LoseResult']
    elif pm == "scissors" and cm == "rock":
        res = results['LoseResult']
    elif pm == "scissors" and cm == "paper":
        res = results['WinResult']
    return res


def score_board_vsplayer(res):
    if res == results['tieResult']:
        scoresVSPlayer['ties'] += 1
    elif res == results['FWinResult']:
        scoresVSPlayer['fwin'] += 1
    elif res == results['SWinResult']:
        scoresVSPlayer['swin'] += 1

    return [scoresVSPlayer['fwin'], scoresVSPlayer['swin'], scoresVSPlayer['ties']]


def score_board_vscomputer(res):
    if res == results['tieResult']:
        scoresVSComputer['tie'] += 1
    if res == results['WinResult']:
        scoresVSComputer['pwin'] += 1
    if res == results['LoseResult']:
        scoresVSComputer['plose'] += 1
    return [scoresVSComputer['pwin'], scoresVSComputer['plose'], scoresVSComputer['tie']]
