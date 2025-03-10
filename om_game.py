import hashlib
import random

def generate_mines(client_seed, server_seed, nonce, size, num_mines):
    combined_seed = f"{server_seed}:{client_seed}:{nonce}"
    hash_value = hashlib.sha256(combined_seed.encode()).hexdigest()
    rng = random.Random(int(hash_value, 16))
    
    mine_positions = set()
    while len(mine_positions) < num_mines:
        flat_index = rng.randint(0, size * size - 1)
        x, y = divmod(flat_index, size)
        mine_positions.add((x, y))
    
    return mine_positions

class MinesGame:
    def _init_(self, size, num_mines, client_seed, server_seed, nonce):
        self.size = size
        self.num_mines = num_mines
        self.client_seed = client_seed
        self.server_seed = server_seed
        self.nonce = nonce
        self.grid = self.create_grid()
        self.revealed = [[False for _ in range(size)] for _ in range(size)]
        self.adjacent_mines = [[0 for _ in range(size)] for _ in range(size)]
        self.place_mines()
        self.calculate_adjacent_mines()
    
    def create_grid(self):
        return [[0 for _ in range(self.size)] for _ in range(self.size)]
    
    def place_mines(self):
        mine_positions = generate_mines(self.client_seed, self.server_seed, self.nonce, self.size, self.num_mines)
        self.mines = list(mine_positions)
        # Assume the first mine is the bomb
        self.bomb = self.mines[0]  
        for (x, y) in mine_positions:
            self.grid[x][y] = 1

    def calculate_adjacent_mines(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y] == 1:
                    continue
                count = 0
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.size and 0 <= ny < self.size and self.grid[nx][ny] == 1:
                        count += 1
                self.adjacent_mines[x][y] = count

    def reveal(self, x, y):
        if self.grid[x][y] == 1:
            return False  # Hit a mine
        self.revealed[x][y] = True
        return True  # Safe spot

    def print_grid(self, reveal_mines=False):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if reveal_mines and self.grid[i][j] == 1:
                    if (i, j) == self.bomb:
                        row.append('B')  # Mark the bomb
                    else:
                        row.append('M')  # Mark the mines
                elif self.revealed[i][j]:
                    row.append(str(self.adjacent_mines[i][j]))
                else:
                    row.append('.')
            print(" ".join(row))

class MinesBot:
    def _init_(self, game):
        self.game = game
        self.safe_moves = []
        self.risky_moves = []
        self.predictions = []
        self.update_moves()

    def update_moves(self):
        self.safe_moves.clear()
        self.risky_moves.clear()
        size = self.game.size
        for i in range(size):
            for j in range(size):
                if not self.game.revealed[i][j]:
                    if self.game.adjacent_mines[i][j] == 0:
                        self.safe_moves.append((i, j))
                    else:
                        self.risky_moves.append((i, j))

    def make_move(self):
        if self.safe_moves:
            return self.safe_moves.pop(0)
        else:
            self.risky_moves.sort(key=lambda move: self.game.adjacent_mines[move[0]][move[1]])
            if self.risky_moves:
                return self.risky_moves.pop(0)
            else:
                return None  # No more moves available

    def predict_mines_and_bomb(self, num_mines):
        possible_mines = [(i, j) for i in range(self.game.size) for j in range(self.game.size) if not self.game.revealed[i][j]]
        random.shuffle(possible_mines)
        self.predictions = possible_mines[:num_mines]
        return self.predictions
# Example of creating a game
client_seed = "heKCYZ-by1"
server_seed = "3605ce5232feb50ac1b86847e53795bac97cc81e484cb2f2f1c3b7ba6c2f6e00"
nonce = 0
size = 5
num_mines = 6  # Set this to the number of mines you select (6 in this case)

game = MinesGame(size, num_mines, client_seed, server_seed, nonce)
print("Initial grid with mines and bomb revealed:")
game.print_grid(reveal_mines=True)
print("\n")

# Example of running the bot
bot = MinesBot(game)
while True:
    move = bot.make_move()
    if move is None:
        print("No more moves available.")
        break
    x, y = move
    result = game.reveal(x, y)
    if not result:
        print(f"Bot hit a mine at ({x}, {y})!")
        game.print_grid(reveal_mines=True)
        break
    else:
        print(f"Bot safely revealed ({x}, {y}).")
        game.print_grid()
        bot.update_moves()
        if all(all(row) for row in game.revealed):
            print("Bot successfully revealed all safe spots!")
            break

# Prediction example
num_predictions = 6  # Number of mines to predict, including the bomb
predictions = bot.predict_mines_and_bomb(num_predictions)
print(f"Predicted mine positions (including bomb): {predictions}")
print("\nFinal grid with mines and bomb revealed:")
game.print_grid(reveal_mines=True)