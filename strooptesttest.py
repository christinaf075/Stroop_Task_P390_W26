import sys, pygame
pygame.init()
from itertools import compress
import random

# --- Font setup ---
my_font = pygame.font.Font(None, 200)
instr_font = pygame.font.Font(None, 50)

# --- Words and colors ---
words = ["RED", "BLUE", "GREEN", "YELLOW"]

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

colors = [RED, GREEN, BLUE, YELLOW]

key_to_color = {
    pygame.K_r: RED,
    pygame.K_g: GREEN,
    pygame.K_b: BLUE,
    pygame.K_y: YELLOW
}

word_to_color = {
    "RED": RED,
    "GREEN": GREEN,
    "BLUE": BLUE,
    "YELLOW": YELLOW
}

# Store results
results = []

# Fullscreen window
mywindow = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def new_word():
    global word, color, test_text, test_text_pos, word_start_time
    word = random.choice(words)
    color = random.choice(colors)
    test_text = my_font.render(word, True, color)
    win_width, win_height = mywindow.get_size()
    test_text_pos = test_text.get_rect(center=(win_width // 2, win_height // 2))

    # Check if word text matches the color
    match = color == word_to_color[word]

    results.append({
        "trial": trial + 1,
        "word_number": word_count + 1,
        "word": word,
        "color": color,
        "match": match,
        "reaction_time": None,
        "correct": None
    })

    # Start reaction timer
    word_start_time = pygame.time.get_ticks()

def show_trial_message(text):
    win_width, win_height = mywindow.get_size()
    mywindow.fill((255, 255, 255))
    lines = text.split("\n")
    for i, line in enumerate(lines):
        msg_surface = instr_font.render(line, True, (0, 0, 0))
        msg_pos = msg_surface.get_rect(center=(win_width // 2, win_height // 2 - 50 + i * 100))
        mywindow.blit(msg_surface, msg_pos)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Instructions before first trial
win_width, win_height = mywindow.get_size()
instr_surface1 = instr_font.render("State the colour of the word you see", True, (0, 0, 0))
instr_pos1 = instr_surface1.get_rect(center=(win_width // 2, win_height // 2 - 50))
instr_surface2 = instr_font.render("Press any key to start", True, (0, 0, 0))
instr_pos2 = instr_surface2.get_rect(center=(win_width // 2, win_height // 2 + 50))

mywindow.fill((255, 255, 255))
mywindow.blit(instr_surface1, instr_pos1)
mywindow.blit(instr_surface2, instr_pos2)
pygame.display.flip()

waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            waiting = False

# --- Trial setup ---
num_trials = 3
words_per_trial = 2

running = True
trial = 0
word_count = 0
trial_msg_shown = False

new_word()
showing_word = True
waiting_for_response = False

# --- Main trial loop ---
while running:
    current_time = pygame.time.get_ticks()
    win_width, win_height = mywindow.get_size()

    # Show trial messages for 2nd and 3rd trials
    if word_count == 0 and trial > 0 and not trial_msg_shown:
        if trial == 1:
            show_trial_message("Second Trial\nPress any key to start")
        elif trial == 2:
            show_trial_message("Third Trial\nPress any key to start")
        new_word()
        showing_word = True
        waiting_for_response = False
        trial_msg_shown = True

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if waiting_for_response and event.key in (pygame.K_r, pygame.K_g, pygame.K_b, pygame.K_y):
                reaction_time = pygame.time.get_ticks() - word_start_time
                results[-1]["reaction_time"] = reaction_time

                pressed_color = key_to_color[event.key]
                correct = pressed_color == color
                results[-1]["correct"] = correct

                # PRINT ALL THREE TO TERMINAL IN ONE LINE
                match_status = results[-1]["match"]
                print(f"Trial {trial+1}, Word {word_count+1}: Match={match_status}, Correct={correct}, ReactionTime={reaction_time} ms")

                # Move to next word
                word_count += 1
                if word_count >= words_per_trial:
                    trial += 1
                    word_count = 0
                    trial_msg_shown = False
                if trial >= num_trials:
                    running = False
                    break
                new_word()
                showing_word = True
                waiting_for_response = False

    # Display word for 500 ms
    if showing_word:
        mywindow.fill((255, 255, 255))
        mywindow.blit(test_text, test_text_pos)
        pygame.display.flip()
        if current_time - word_start_time >= 500:
            showing_word = False
            waiting_for_response = True
            mywindow.fill((255, 255, 255))
            pygame.display.flip()
    elif waiting_for_response:
        pass  # Blank screen until key press

pygame.quit()
sys.exit()

# Initialization: Initialize Pygame, set screen dimensions, and define colors (RGB).
# Logic: Create a list of words and a corresponding list of colors.
# Loop: Use random.choice to pick a word and a color, ensuring they don't match for congruent trials.
# Input & Timing: Detect key presses (pygame.K_r, etc.), calculate time_end - time_start, and update the score.