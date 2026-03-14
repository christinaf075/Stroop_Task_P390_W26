import sys, pygame
pygame.init()
from itertools import compress
import random
import csv

# data storage setup
def init_csv():
    """Initialize CSV file with headers"""
    filename = f"stroop_results.csv"
    
    # Create file with headers
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["trial", "word_number", "match", "reaction_time", "correct"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    
    return filename

# Initialize CSV
csv_filename = init_csv()

# --- Font setup ---
my_font = pygame.font.Font(None, 200)
instr_font = pygame.font.Font(None, 50)
task_font = pygame.font.Font(None,25)

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

def wrap_text(text, font, max_width):
    """Wrap text to fit within a given width"""
    words = text.split(' ')
    lines = []
    current_line = []
    
    for word in words:
        # Test if adding this word would exceed max width
        test_line = ' '.join(current_line + [word])
        test_surface = font.render(test_line, True, (0, 0, 0))
        
        if test_surface.get_width() <= max_width:
            current_line.append(word)
        else:
            # If current line has words, add it to lines
            if current_line:
                lines.append(' '.join(current_line))
                current_line = [word]
            else:
                # If word itself is too long, just add it
                lines.append(word)
                current_line = []
    
    # Add the last line
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines

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

def save_result_to_csv(trial_num, word_num, match_status, rt, correct_status):
    """Save one trial to CSV file"""
    # Append to CSV
    with open(csv_filename, 'a', newline='') as csvfile:
        fieldnames = ["trial", "word_number", "match", "reaction_time", "correct"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writerow({"trial": trial_num, "word_number": word_num, "match": str(match_status), "reaction_time": rt,
        "correct": str(correct_status)})

def show_trial_message(text):
    win_width, win_height = mywindow.get_size()
    mywindow.fill((255, 255, 255))

    # Wrap the instruction text
    if len(text) > 50:
        lines = wrap_text(text, instr_font, win_width - 100)
    else:
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
                if event.key == pygame.K_ESCAPE:
                    print(f"Saving results to: {csv_filename}")
                    pygame.quit()
                    sys.exit()
                else:
                    waiting = False

# Instructions before first trial
win_width, win_height = mywindow.get_size()
instruction_text = ("Welcome to the Stroop Task. You will be presented with a series of colored words for a few seconds. "
                    "State the colour of the word you see by pressing the letter key of the first letter of the color. "
                    "For example, if the color of the word you see is yellow, you would press the 'y' key. "
                    "Always go by the COLOR of the word and not the color the word itself is referring to. "
                    "There are 3 trials of this.")
# Wrap the instruction text
wrapped_lines = wrap_text(instruction_text, instr_font, win_width - 100)
mywindow.fill((255, 255, 255))

# Display wrapped instructions
for i, line in enumerate(wrapped_lines):
    instr_surface = instr_font.render(line, True, (0, 0, 0))
    instr_pos = instr_surface.get_rect(center=(win_width // 2, win_height // 2 - 100 + i * 40))
    mywindow.blit(instr_surface, instr_pos)

# Start message
start_surface = instr_font.render("Press any key to start.", True, (0, 0, 0))
start_pos = start_surface.get_rect(center=(win_width // 2, win_height // 2 + 100))
mywindow.blit(start_surface, start_pos)

pygame.display.flip()

waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            else:
                waiting = False
# --- Trial setup ---
num_trials = 3
# change to 10 later
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if waiting_for_response and event.key in (pygame.K_r, pygame.K_g, pygame.K_b, pygame.K_y):
                reaction_time = pygame.time.get_ticks() - word_start_time
                results[-1]["reaction_time"] = reaction_time

                pressed_color = key_to_color[event.key]
                correct = pressed_color == color
                results[-1]["correct"] = correct
                match_status = color == word_to_color[word]
        
                #save the data to csv
                save_result_to_csv(trial_num=trial + 1, word_num=word_count + 1, match_status=match_status, rt=reaction_time,
                correct_status=correct)

                # Move to next word
                word_count += 1
                if word_count >= words_per_trial:
                    trial += 1
                    word_count = 0
                    trial_msg_shown = False
                if trial >= num_trials:
                    running = False
                new_word()
                showing_word = True
                waiting_for_response = False

    # Display word for 500 ms
    if running and showing_word:
        mywindow.fill((255, 255, 255))
        mywindow.blit(test_text, test_text_pos)
        pygame.display.flip()
        if current_time - word_start_time >= 500:
            showing_word = False
            waiting_for_response = True
            mywindow.fill((255, 255, 255))
            pygame.display.flip()
    elif running and waiting_for_response:
        pass  # Blank screen until key press

pygame.quit()
sys.exit()

# Initialization: Initialize Pygame, set screen dimensions, and define colors (RGB).
# Logic: Create a list of words and a corresponding list of colors.
# Loop: Use random.choice to pick a word and a color, ensuring they don't match for congruent trials.
# Input & Timing: Detect key presses (pygame.K_r, etc.), calculate time_end - time_start, and update the score.