import random


# Parent Player class
class Player:
    moves = ['rock', 'paper', 'scissors']
    last_opponent_move = None

    def move(self):
        pass

    def learn(self, my_move, their_move):
        self.last_opponent_move = their_move


# Rock strategy player
class Rock(Player):
    def move(self):
        return 'rock'


# Random strategy player
class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)


# Human player
class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, Paper, Scissors? ").lower()
            if move in self.moves:
                return move
            print("Please type in Rock, Paper, Or Scissors\n")


# Reflecting player (mimics opponent's last move)
class ReflectPlayer(Player):
    def move(self):
        if self.last_opponent_move:
            return self.last_opponent_move
        else:
            return random.choice(self.moves)


# Cycling player (cycles through moves)
class CyclePlayer(Player):
    def __init__(self):
        self.last_move = None

    def move(self):
        if self.last_move is None:
            self.last_move = random.choice(self.moves)
        else:
            index = self.moves.index(self.last_move)
            self.last_move = self.moves[(index + 1) % 3]
        return self.last_move


# Function to determine winner of a round
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Game class
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            print("Player 1 wins this round!")
            self.p1_score += 1
        elif beats(move2, move1):
            print("Player 2 wins this round!")
            self.p2_score += 1
        else:
            print("It's a tie!")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        menu_options = {
            "starter": Rock(),
            "easy": CyclePlayer(),
            "medium": ReflectPlayer(),
            "hard": RandomPlayer()
        }

        while True:
            option = input(
                """
Welcome to Rock Paper Scissors!
Type Starter, Easy, Medium, or Hard to Begin!
Type Exit to quit.
Please select a game mode: """
            ).lower()

            if option == "exit":
                print("Thanks for playing!")
                return

            if option in menu_options:
                print(f"{option.capitalize()} Mode Selected\nGame start!")
                self.p2 = menu_options[option]
                break

        for round in range(3):
            print(f"Round {round + 1}: ")
            self.play_round()
            print(f"""Score -> Player 1:{self.p1_score}
             | Player 2:{self.p2_score}\n
                        """)

        print(f"""Final score -> Player 1:{self.p1_score}
         | Player 2:{self.p2_score}
                """)
        if self.p1_score > self.p2_score:
            print("Player 1 wins the game!\nGame over!\n")
        elif self.p2_score > self.p1_score:
            print("Player 2 wins the game!\nGame over!\n")
        else:
            print("No winner! It's a draw!")
            print("Game over!\n")
            self.play_game()


if __name__ == "__main__":
    game = Game(HumanPlayer(), Player())
    game.play_game()
