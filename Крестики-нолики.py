size = 3
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win_comb = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8),(3,6,9),(3,5,7), (1,5,9)]
def xo():
    print("_" * 13)
    for i in range(size):
        print("|", board[i*3], "|", board[i*3+1], "|", board[i*3 + 2],"|")
    print("_"*13)

def inpu(player):
    while True:
        value = int(input(f"Укажите номер клетки, {player}: "))
        if not (value in range(1, 9)):
            print("Неверный ввод, повторите.")
            continue
        value = int(value)
        if str(board[value-1]) in "XO":
            print("Эта поле уже занято")
            continue
        board[value-1] = player
        break


def check():
    for j in win_comb:
        if (board[j[0]-1]) == (board[j[1]-1]) == (board[j[2]-1]):
            return board[j[1]-1]
    else:
        return False
def base():
    counter = 0
    while True:
        xo()
        if counter % 2 == 0:
            inpu("X")
        else:
            inpu("O")
        if counter > 3:
            winner = check()
            if winner:
                print(winner, "выйграл!")
                break
        counter += 1
        if counter > 8:
            xo()
            print("Ничья")
            break




base()