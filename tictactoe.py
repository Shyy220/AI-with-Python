import random
from colorama import init, Fore, Style


init(autoreset=True)

def display_board(board):

    def color_cell(cell):
        if cell == "X":
            return Fore.RED + cell + Style.RESET_ALL
        elif cell =="0":
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL


    print()
    print(" " + color_cell(board[0])) + " | " + color_cell(board[1]) + " | " + color_cell(board[2])
    print(Fore.CYAN + "---+---+---")
    print(" " + color_cell(board[3])) + " | " + color_cell(board[4]) + " | " + color_cell(board[5])
    print(Fore.CYAN + "---+---+---")
    print(" " + color_cell(board[6])) + " | " + color_cell(board[7]) + " | " + color_cell(board[8])

def player_choice():

    while True:

        choice = input(Fore.GREEN + "Choose X or O: ").upper()

        if choice == "X":
            return "X", "0"

        elif choice == "0":
            return "0", "X"

        else:
            print(Fore.RED + "Please enter X or O.")

def player_move(board, symbol):

    while True:


      try:
        move = int(input(Fore.GREEN + "Enter your move (1-9): "))

        if move >= 1 and move <=9:

            if board[move - 1].isdigit():
                board[move - 1] = symbol
                break
            else:
                print(Fore.RED + "that posostion is already taken!")

        else:
            print(Fore.RED + "Enter a number between 1 and 9")

      except ValueError:
        print(Fore.RED + "Please enter a valid number.")

def check_win(board, symbol):

    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == symbol:
            return True

        return False

def check_full(board):

    for cell in board:
        if cell.isdigit():
            return False

        return True

def ai_move(board, ai_symbol, player_symbol):


    for i in range(9):

        if board[i].isdigit():

          temp_board = board.copy()
          temp_board[i] = player_symbol

          if check_win(temp_board, player_symbol):
              board[i] = ai_symbol
              print(Fore.MAGENTA + f"AI chose posistion {i + 1}")
              return

    if board[4].isdigit():
        board[4] = ai_symbol
        print(Fore.MAGENTA + "AI chose posistion 5")
        return

    possible_moves = []

    for i in range(9):
        if board[i].isdigit():
            possible_moves.append(i)

    move = random.choice(possible_moves)

    board[move] = ai_symbol

    print(Fore.MAGENTA + f"AI chose posistion {move + 1}")


def tic_tac_toe():

        print(Fore.CYAN + "=" * 35)
        print(Fore.CYAN + "    TIC TAC TOE WITH AI")
        print(Fore.CYAN + "=" * 35)

        player_name = input(Fore.GREEN + "Enter your name: ")

        while True:

            board = [
                "1","2","3",
                "4","5","6",
                "7","8","9"

            ]

            player_symbol, ai_symbol = player_choice()

            turn = "Player"

            while True:

                display_board(board)

                if turn == "Player":

                    player_move(board, player_symbol)

                    if check_win(board, player_symbol):

                        display_board(board)

                        print(
                            Fore.GREEN +
                            f"Congrats {player_name}! You Won!!"
                            )
                        break

                    if check_full(board):

                        display_board(board)

                        print(Fore.YELLOW + "It's a Tie")
                        break

                    turn = "AI"
                else:

                    ai_move(board, ai_symbol, player_symbol)

                    if check_win(board, ai_symbol):

                        display_board(board)

                        print(Fore.RED + "AI wins!")
                        break

                    if check_full(board):

                        display_board(board)

                        print(Fore.YELLOW + "Its a Tie!")
                        break

                    turn = "Player"

                play_again = input(
                    Fore.GREEN + "Do you wanna play again? (yes/no):"
                ).lower()

                if play_again != "yes":
                    print(Fore.CYAN + "Thank You for playing!")
                    break

if __name__ == "__main__":
    tic_tac_toe()

                

        

