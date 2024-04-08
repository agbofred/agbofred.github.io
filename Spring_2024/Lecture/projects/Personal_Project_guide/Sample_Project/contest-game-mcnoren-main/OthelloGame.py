from pgl import GWindow, GOval, GLabel, GRect, GImage
from OthelloTile import OthelloTile

#constants
GW_WIDTH = 1000
GW_HEIGHT = 800
TOP_PADDING = 50
BOTTOM_PADDING = 50

#calculated constants
BOARD_LENGTH = GW_HEIGHT - TOP_PADDING - BOTTOM_PADDING
BOARD_X = (GW_WIDTH - BOARD_LENGTH) / 2
BOARD_Y = TOP_PADDING
TILE_PADDING = 5

class OthelloGame:

    def __init__(self, s):
        self.size = s
        self.board = [[None for i in range(self.size)]for j in range(self.size)]
        self.turn = True # True = black, False = white
        self.next_token = GOval(GW_WIDTH, GW_HEIGHT, BOARD_LENGTH / self.size - TILE_PADDING * 2, BOARD_LENGTH / self.size - TILE_PADDING * 2)
        self.next_token.set_color("black")
        self.next_token.set_filled(True)
        self.turn_token = GOval(20, BOARD_Y + 10, BOARD_X - 40, BOARD_X - 40)
        self.turn_token.set_fill_color("black")
        self.turn_token.set_filled(True)
        self.possible_moves = []
        self.black_score = 0
        self.white_score = 0
        self.gw = gw = GWindow(GW_WIDTH, GW_HEIGHT)
    
    def create_window(self):
        """This function creates the GWindow and the starting setup for the gameboard."""
        background = GImage("wood_table.jpeg")
        self.gw.add(background, 0, 0)
        
        self.gw.add(self.turn_token)
        
        turn_label = GLabel("Turn:")
        turn_label.set_font("40px 'Ariel'")
        turn_label.set_color("white")
        self.gw.add(turn_label, (BOARD_X - turn_label.get_width()) / 2, BOARD_Y)
        self.gw.scoreboard = GLabel(f"Black Score:{self.black_score}\tWhite Score:{self.white_score}")
        self.gw.scoreboard.set_font("20px 'Areil")
        self.gw.scoreboard.set_color("white")
        self.gw.add(self.gw.scoreboard, 10, GW_HEIGHT - 10)
        self.gw.new_game_button = GLabel("New Game")
        self.gw.new_game_button.set_color("white")
        self.gw.add(self.gw.new_game_button, GW_WIDTH - self.gw.new_game_button.get_width() - TILE_PADDING, self.gw.new_game_button.get_height() + TILE_PADDING)
        
        # create board:
        for r in range(self.size):
            for c in range(self.size):
                x = BOARD_X + c * (BOARD_LENGTH / self.size)
                y = BOARD_Y + r * (BOARD_LENGTH / self.size)
                length = BOARD_LENGTH / len(self.board)
                if self.board[r][c] is None:
                    self.board[r][c] = OthelloTile(x, y, length, None, TILE_PADDING, self.gw)
        middle = self.size // 2 - 1
        self.board[middle][middle].add_token(True)
        self.board[middle][middle+1].add_token(False)
        self.board[middle+1][middle].add_token(False)
        self.board[middle+1][middle+1].add_token(True)
        self.update_scores()

        self.gw.add(self.next_token)
        self.update_possible_moves()

    def update_scores(self):
        black = 0
        white = 0
        for r in range(self.size):
            for c in range(self.size):
                tile = self.board[r][c]
                if tile.get_state() is not None:
                    if tile.get_state(): # Black
                        black += 1
                    else:
                        white += 1
        self.gw.scoreboard.set_label(f"Black Score: {black}\tWhite Score: {white}")
        self.black_score = black
        self.white_score = white
    
    def get_tile(self, x, y):
        """This function returns the tile at a given coordinate or None otherwise."""
        for r in range(self.size):
            for c in range(self.size):
                length = BOARD_LENGTH / len(self.board)
                min_x = BOARD_X + c * (BOARD_LENGTH / self.size)
                min_y = BOARD_Y + r * (BOARD_LENGTH / self.size)
                max_x = min_x + length
                max_y = min_y + length
                if min_x < x < max_x and min_y < y < max_y:
                    return (r,c)
        return (None,None)

    def update_next_token_location(self, event):
        r, c = self.get_tile(event.get_x(), event.get_y())
        if r is not None and c is not None:
            tile = self.board[r][c]
            if self.is_valid_move(r, c):
                self.next_token.set_location(tile.get_x() + TILE_PADDING, tile.get_y() + TILE_PADDING)
                self.next_token.send_to_front()
            else:
                self.next_token.set_location(GW_WIDTH, GW_HEIGHT)
        else:
            self.next_token.set_location(GW_WIDTH, GW_HEIGHT)
    
    def place_token(self, event):
        r, c = self.get_tile(event.get_x(), event.get_y())
        if r is not None and c is not None:
            tile = self.board[r][c]
            if self.is_valid_move(r, c) and not self.is_tile_flipping():
                tile.add_token(self.turn)
                self.find_flips(r, c)
                self.update_scores()
                self.next_player()
                if self.black_score + self.white_score == self.size * self.size:
                    self.end_game()
                else:
                    self.update_possible_moves()
    
    def is_tile_flipping(self):
        for r in range(self.size):
            for c in range(self.size):
                tile = self.board[r][c]
                if tile.is_flipping():
                    return True
        return False
                     
    
    def next_player(self):
        if self.turn: # Black
            self.turn = False 
            self.next_token.set_color("white")
            self.turn_token.set_fill_color("white")
        else:
            self.turn = True
            self.next_token.set_color("black")
            self.turn_token.set_fill_color("black")
    
    def is_game_over(self):
        """This function checks to see whether the game is over"""
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c].get_state() is None:
                    return False
        return True
            
    def is_valid_move(self, row, col):
        if self.board[row][col].get_state() is not None:
            return False
        #up:
        gap = False
        c = col
        r = row - 1
        finished = False
        if(r < 0):
            finished = True
        while not finished:
            if self.board[r][c].get_state() is None:
                finished = True
            elif self.board[r][c].get_state() != self.turn:
                gap = True
            else:
                if gap:
                    return True
                else:
                    finished = True
            r = r - 1
            if(r < 0):
                finished = True
            
        #down:
        gap = False
        c = col
        r = row + 1
        finished = False
        if(r >= self.size):
            finished = True
        while not finished:
            if self.board[r][c].get_state() is None:
                finished = True
            elif self.board[r][c].get_state() != self.turn:
                gap = True
            else:
                if gap:
                    return True
                else:
                    finished = True
            r = r + 1
            if(r >= self.size):
                finished = True
        #left:
        gap = False
        c = col + 1
        r = row
        finished = False
        if(c >= self.size):
            finished = True
        while not finished:
            if self.board[r][c].get_state() is None:
                finished = True
            elif self.board[r][c].get_state() != self.turn:
                gap = True
            else:
                if gap:
                    return True
                else:
                    finished = True
                
            c = c + 1
            if(c >= self.size):
                finished = True
        #right:
        gap = False
        c = col - 1
        r = row
        finished = False
        if(c < 0):
            finished = True
        while not finished:
            if self.board[r][c].get_state() is None:
                finished = True
            elif self.board[r][c].get_state() != self.turn:
                gap = True
            else:
                if gap:
                    return True
                else:
                    finished = True
            c = c - 1
            if(c < 0):
                finished = True
        #right-down:
        gap = False
        c = col + 1
        r = row + 1
        finished = False
        if(c >= self.size or r >= self.size):
            finished = True
        while not finished:
            if self.board[r][c].get_state() is None:
                finished = True
            elif self.board[r][c].get_state() != self.turn:
                gap = True
            else:
                if gap:
                    return True
                else:
                    finished = True
            c = c + 1
            r = r + 1
            if(c >= self.size or r >= self.size):
                finished = True
        #left-down:
        gap = False
        c = col - 1
        r = row + 1
        finished = False
        if(c < 0 or r >= self.size):
            finished = True
        while not finished:
            if self.board[r][c].get_state() is None:
                finished = True
            elif self.board[r][c].get_state() != self.turn:
                gap = True
            else:
                if gap:
                    return True
                else:
                    finished = True
            c = c - 1
            r = r + 1
            if(c < 0 or r >= self.size):
                finished = True
        #right-up:
        gap = False
        c = col + 1
        r = row - 1
        finished = False
        if(c >= self.size or r < 0):
            finished = True
        while not finished:
            if self.board[r][c].get_state() is None:
                finished = True
            elif self.board[r][c].get_state() != self.turn:
                gap = True
            else:
                if gap:
                    return True
                else:
                    finished = True
            c = c + 1
            r = r - 1
            if(c >= self.size or r < 0):
                finished = True
        #left-up:
        gap = False
        c = col - 1
        r = row - 1
        finished = False
        if(c < 0 or r < 0):
            finished = True
        while not finished:
            if self.board[r][c].get_state() is None:
                finished = True
            elif self.board[r][c].get_state() != self.turn:
                gap = True
            else:
                if gap:
                    return True
                else:
                    finished = True
            c = c - 1
            r = r - 1
            if(c < 0 or r < 0):
                finished = True
        return False

    def update_possible_moves(self, second_time = False):
        if len(self.possible_moves) != 0:
            for circle in self.possible_moves:
                circle.set_visible(False)
            self.possible_moves = []
        for r in range(self.size):
            for c in range(self.size):
                if self.is_valid_move(r, c):
                    dot_size = BOARD_LENGTH / self.size / 9
                    dot = GOval(self.board[r][c].get_x() + self.board[r][c].get_length() / 2 - dot_size / 2, self.board[r][c].get_y() + self.board[r][c].get_length() / 2 - dot_size / 2, dot_size, dot_size)
                    dot.set_color("black")
                    dot.set_filled(True)
                    self.possible_moves.append(dot)
                    self.gw.add(dot)
        if len(self.possible_moves) == 0:
            if second_time:
                self.end_game()
            else:
                self.next_player()
                self.update_possible_moves(True)

    def flip_tokens(self, tokens):
        for token in tokens:
            token.flip()
    
    def find_flips(self, row, col):
        #up:
        gap = False
        c = col
        r = row - 1
        finished = False
        if(r < 0):
            finished = True
        tokens = []
        while not finished:
            if self.board[r][c].get_state() is None:
                finished = True
            elif self.board[r][c].get_state() != self.turn:
                gap = True
                tokens.append(self.board[r][c])
            else:
                if gap:
                    self.flip_tokens(tokens)
                    finished = True
                else:
                    finished = True
            r = r - 1
            if(r < 0):
                finished = True
        #down:
        gap = False
        c = col
        r = row + 1
        finished = False
        if(r >= self.size):
            finished = True
        tokens = []
        while not finished:
            if self.board[r][c].get_state() is None:
                finished = True
            elif self.board[r][c].get_state() != self.turn:
                gap = True
                tokens.append(self.board[r][c])
            else:
                if gap:
                    self.flip_tokens(tokens)
                    finished = True
                else:
                    finished = True
            r = r + 1
            if(r >= self.size):
                finished = True
        #left:
        gap = False
        c = col + 1
        r = row
        finished = False
        if(c >= self.size):
            finished = True
        tokens = []
        while not finished:
            if self.board[r][c].get_state() is None:
                finished = True
            elif self.board[r][c].get_state() != self.turn:
                gap = True
                tokens.append(self.board[r][c])
            else:
                if gap:
                    self.flip_tokens(tokens)
                    finished = True
                else:
                    finished = True
                
            c = c + 1
            if(c >= self.size):
                finished = True
        #right:
        gap = False
        c = col - 1
        r = row
        finished = False
        if(c < 0):
            finished = True
        tokens = []
        while not finished:
            if self.board[r][c].get_state() is None:
                finished = True
            elif self.board[r][c].get_state() != self.turn:
                gap = True
                tokens.append(self.board[r][c])
            else:
                if gap:
                    self.flip_tokens(tokens)
                    finished = True
                else:
                    finished = True
            c = c - 1
            if(c < 0):
                finished = True
        #right-down:
        gap = False
        c = col + 1
        r = row + 1
        finished = False
        if(c >= self.size or r >= self.size):
            finished = True
        tokens = []
        while not finished:
            if self.board[r][c].get_state() is None:
                finished = True
            elif self.board[r][c].get_state() != self.turn:
                gap = True
                tokens.append(self.board[r][c])
            else:
                if gap:
                    self.flip_tokens(tokens)
                    finished = True
                else:
                    finished = True
            c = c + 1
            r = r + 1
            if(c >= self.size or r >= self.size):
                finished = True
        #left-down:
        gap = False
        c = col - 1
        r = row + 1
        finished = False
        if(c < 0 or r >= self.size):
            finished = True
        tokens = []
        while not finished:
            if self.board[r][c].get_state() is None:
                finished = True
            elif self.board[r][c].get_state() != self.turn:
                gap = True
                tokens.append(self.board[r][c])
            else:
                if gap:
                    self.flip_tokens(tokens)
                    finished = True
                else:
                    finished = True
            c = c - 1
            r = r + 1
            if(c < 0 or r >= self.size):
                finished = True
        #right-up:
        gap = False
        c = col + 1
        r = row - 1
        finished = False
        if(c >= self.size or r < 0):
            finished = True
        tokens = []
        while not finished:
            if self.board[r][c].get_state() is None:
                finished = True
            elif self.board[r][c].get_state() != self.turn:
                gap = True
                tokens.append(self.board[r][c])
            else:
                if gap:
                    self.flip_tokens(tokens)
                    finished = True
                else:
                    finished = True
            c = c + 1
            r = r - 1
            if(c >= self.size or r < 0):
                finished = True
        #left-up:
        gap = False
        c = col - 1
        r = row - 1
        finished = False
        if(c < 0 or r < 0):
            finished = True
        tokens = []
        while not finished:
            if self.board[r][c].get_state() is None:
                finished = True
            elif self.board[r][c].get_state() != self.turn:
                gap = True
                tokens.append(self.board[r][c])
            else:
                if gap:
                    self.flip_tokens(tokens)
                    finished = True
                else:
                    finished = True
            c = c - 1
            r = r - 1
            if(c < 0 or r < 0):
                finished = True

    def update_new_game_color(self, event):
        if(self.gw.new_game_button.contains(event.get_x(), event.get_y())):
            self.gw.new_game_button.set_color("lightblue")
        else:
            self.gw.new_game_button.set_color("white")
    
    def new_game_check(self, event):
        if(self.gw.new_game_button.contains(event.get_x(), event.get_y())):
            new_game(self.size)
            
    def end_game(self):
        if self.black_score > self.white_score:
            win_label = GLabel("Black Wins!")
        elif self.white_score > self.black_score:
            win_label = GLabel("White Wins!")
        else:
            win_label = GLabel("Tie")
        win_label.set_font("30px 'Ariel'")
        win_label.set_color("white")
        #backdrop = GRect(GW_WIDTH - win_label.get_width() - TILE_PADDING, GW_HEIGHT - TILE_PADDING, win_label.get_width() + TILE_PADDING * 2, win_label.get_height() + TILE_PADDING * 2)
        #backdrop.set_color("white")
        #backdrop.set_filled(True)
        #self.gw.add(backdrop)
        self.gw.add(win_label, GW_WIDTH - win_label.get_width() - TILE_PADDING, GW_HEIGHT - TILE_PADDING)
    
    

    def run(self):
        self.create_window()
        self.gw.add_event_listener("mousemove", self.update_next_token_location)
        self.gw.add_event_listener("mousemove", self.update_new_game_color)
        self.gw.add_event_listener("click", self.place_token)
        self.gw.add_event_listener("click", self.new_game_check)

def new_game(size):
    game = OthelloGame(size)
    game.run()




