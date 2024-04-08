# Name:

"""
This is a game where you are being chased. The player needs to avoid being caught by the chaser and
survive all the roudns to win!

Note - my orginal goal was to have a new chaser be added every round to make it more difficult.
I was unable to get it to function in the correct manner for all the chasers to move. But the game
should still be fun
"""

# Now you are free to import whatever you need and take it from here!
from pgl import GWindow, GRect, GLabel
import time #found as a built in module in python
# I'm excited to play these!

Height = 750
Width = 1000
Square_Size = 45
gw = GWindow(Width, Height)
caught = False #Initialize caught variable
round_counter = 0
paused = False

round_label = GLabel("Round 0/5")
round_label.set_color("black")
round_label.set_font("25px 'SansSerif'")

#countdown_label = GLabel("Time: 10")
#countdown_label.set_font("25px 'Sanserif'")
#gw.add(round_label, 10, 20)

def window_design():
    color_b = GRect(Width, Height)
    color_b.set_filled(True)
    color_b.set_fill_color("grey")
    gw.add(color_b)
    
    #return window_design

def player():
    Player = GRect(Width / 2 - Square_Size / 2, Height / 2 - Square_Size / 2, Square_Size, Square_Size)
    Player.set_filled(True)
    Player.set_fill_color("black")
    gw.add(Player)

    return Player

chasers = []
import random

def chaser():
    colors = "wheat","yellow","gold","lemonchiffon","darkgoldenrod", "orange","darkorange", "darksalmon","red", "darkred","crimson"

    chase = GRect(random.randint(0, Width - Square_Size), random.randint(0, Height - Square_Size), Square_Size - 5, Square_Size - 5)
    chase.set_filled(True)
    chase.set_fill_color(random.choice(colors))
    gw.add(chase)

    return chase


def move_player(e):
    if not caught:
        player_instance.set_location(e.get_x() - Square_Size / 2, e.get_y() - Square_Size / 2)

def move_chaser():
    global caught
    paused = False

    if not caught and not paused and game_state == "ongoing":
        dx = player_instance.get_x() - chaser_instance.get_x()
        dy = player_instance.get_y() - chaser_instance.get_y()

        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance != 0:
            dx /= distance
            dy /= distance

        speed = 5
        chaser_instance.move(dx * speed, dy * speed)
        check_collision()

        gw.set_timeout(move_chaser, 18)

def check_collision():
    global caught
    if not caught:
        player_bounds = player_instance.get_bounds()
        chaser_bounds = chaser_instance.get_bounds()

        if (player_bounds.get_x() < chaser_bounds.get_x() + chaser_bounds.get_width() and
                player_bounds.get_x() + player_bounds.get_width() > chaser_bounds.get_x() and
                player_bounds.get_y() < chaser_bounds.get_y() + chaser_bounds.get_height() and
                player_bounds.get_y() + player_bounds.get_height() > chaser_bounds.get_y()):
            
            caught = True
            lose_screen()
        elif round_counter >= 5:
            win_screen()

game_state = "ongoing"

def countdown_timer(time_remaining_list, paused_list):
    global caught, gamed_state
    time_remaining = time_remaining_list[0]
    paused = paused_list[0]

    if not caught and not paused and time_remaining > 0:
        #countdown_label.set_label(f"Time: {time_remaining}")
        time_remaining -= 1
        time_remaining_list[0] = time_remaining
        gw.set_timeout(lambda: countdown_timer(time_remaining_list, paused_list), 1000)
    elif not caught and not paused:
        end_round()

def start_round():
    global caught, round_counter, paused, game_state
    caught = False

    if round_counter < 5 and game_state == "ongoing":
        #resets positions after each round
        player_instance.set_location(Width / 2 - Square_Size / 2, Height / 2 - Square_Size / 2)
        chaser_instance.set_location(gw.get_width() - Square_Size, gw.get_height() - Square_Size)
        
        #updates the label
        round_counter += 1
        round_label.set_label(f"Round {round_counter}/5")

        #starts timer
        gw.set_timeout(end_round, 10000)

        paused = True
        
    else:
        if game_state == "ongoing":
            game_state == "won"
            win_screen()
        else:
            lose_screen()


def lose_screen():
    global caught, game_state
    caught = True
    game_state = "lost" #sets game state to lost

    caught_label = GLabel("Caught - You Lose!")
    caught_label.set_font("36px bold 'SansSerif'")
    caught_label.set_color("black")
    gw.add(caught_label, (Width - caught_label.get_width()) / 2, Height / 2)
    gw.set_timeout(start_round, 2000) #New
    game_state = "ended"

def win_screen():
    global game_state
    game_state = "won"

    win_label = GLabel("You Win!")
    win_label.set_font("36px bold 'SanSerif")
    gw.add(win_label, (Width - win_label.get_width()) / 2, Height / 2)
    game_state = "ended"

def resume_round():
    global paused
    paused = False
    gw.set_timeout(move_chaser, 18)


def end_round():
    global caught, round_counter, countdown_label
    caught = True

    if game_state == "ongoing":
        caught_label = GLabel(f"Round {round_counter} - Time's Up!")
        caught_label.set_font("36px bold 'SanSerif'")
        gw.add(caught_label, (Width - caught_label.get_width()) / 2, Height / 2)

        gw.set_timeout(lambda: gw.remove(caught_label), 2000)
        gw.set_timeout(lambda: reset_round(), 2000)

def reset_round():
    global caught, round_counter, game_state
    caught = False
    #countdown_label.set_label("Time: 10")

    round_counter += 1
    round_label.set_label(f"Round {round_counter}/5")

    player_instance.set_location(Width / 2 - Square_Size / 2, Height / 2 - Square_Size / 2)
    chaser_instance.set_location(gw.get_width() - Square_Size, gw.get_height() - Square_Size)

    #gw.set_timeout(lambda: gw.set_timeout(move_chaser, 18), 2000)
    if round_counter <= 5 and game_state == "ongoing":

        gw.set_timeout(move_chaser, 18)
        gw.set_timeout(end_round, 10000)
    elif game_state == "ongoing":
        game_state = "won"
        win_screen()

gw.set_timeout(resume_round, 2000)

if __name__ == '__main__':
    window_design()
    player_instance = player()
    chaser_instance = chaser()
    
    gw.add(round_label, 10, 20)


    gw.add_event_listener("mousemove", move_player)
    gw.set_timeout(move_chaser, 18)
    gw.set_timeout(start_round, 2000)
