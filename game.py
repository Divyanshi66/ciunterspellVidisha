import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Anime Hero Adventure')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define the character (anime hero)
hero_width, hero_height = 50, 50
hero_x, hero_y = width // 2 - hero_width // 2, height - hero_height - 10
hero_speed = 5

# Enemy (obstacle)
enemy_width, enemy_height = 50, 50
enemy_speed = 5
enemies = []

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Font for score
font = pygame.font.SysFont(None, 36)

# Function to draw the character
def draw_hero(x, y):
    pygame.draw.rect(screen, (0, 0, 255), (x, y, hero_width, hero_height))

# Function to draw the enemies
def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

# Function to handle movement
def move_hero(x, y):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= hero_speed
    if keys[pygame.K_RIGHT] and x < width - hero_width:
        x += hero_speed
    if keys[pygame.K_UP] and y > 0:
        y -= hero_speed
    if keys[pygame.K_DOWN] and y < height - hero_height:
        y += hero_speed
    return x, y

# Function to handle enemy movement
def move_enemies():
    global enemies
    for enemy in enemies:
        enemy[1] += enemy_speed
        if enemy[1] > height:
            enemy[1] = -enemy_height
            enemy[0] = random.randint(0, width - enemy_width)

# Function to check for collision
def check_collision(hero_rect, enemies):
    for enemy in enemies:
        if hero_rect.colliderect(enemy):
            return True
    return False

# Main game loop
def game_loop():
    global hero_x, hero_y, enemies
    
    running = True
    score = 0

    while running:
        screen.fill(WHITE)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Move the hero
        hero_x, hero_y = move_hero(hero_x, hero_y)
        
        # Move the enemies
        if random.random() < 0.02:  # Random chance to create a new enemy
            new_enemy_x = random.randint(0, width - enemy_width)
            enemies.append([new_enemy_x, -enemy_height])
        
        move_enemies()

        # Draw the hero
        draw_hero(hero_x, hero_y)

        # Draw the enemies
        draw_enemies()

        # Check for collision
        hero_rect = pygame.Rect(hero_x, hero_y, hero_width, hero_height)
        if check_collision(hero_rect, enemies):
            running = False

        # Display score
        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))
        
        # Increase score as time passes
        score += 1

        # Update the screen
        pygame.display.update()

        # Control the frame rate
        clock.tick(60)

    pygame.quit()

# Run the game
game_loop()
import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Anime Hero Adventure')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define the character (anime hero)
hero_width, hero_height = 50, 50
hero_x, hero_y = width // 2 - hero_width // 2, height - hero_height - 10
hero_speed = 5

# Enemy (obstacle)
enemy_width, enemy_height = 50, 50
enemy_speed = 5
enemies = []

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Font for score
font = pygame.font.SysFont(None, 36)

# Function to draw the character
def draw_hero(x, y):
    pygame.draw.rect(screen, (0, 0, 255), (x, y, hero_width, hero_height))

# Function to draw the enemies
def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

# Function to handle movement
def move_hero(x, y):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= hero_speed
    if keys[pygame.K_RIGHT] and x < width - hero_width:
        x += hero_speed
    if keys[pygame.K_UP] and y > 0:
        y -= hero_speed
    if keys[pygame.K_DOWN] and y < height - hero_height:
        y += hero_speed
    return x, y

# Function to handle enemy movement
def move_enemies():
    global enemies
    for enemy in enemies:
        enemy[1] += enemy_speed
        if enemy[1] > height:
            enemy[1] = -enemy_height
            enemy[0] = random.randint(0, width - enemy_width)

# Function to check for collision
def check_collision(hero_rect, enemies):
    for enemy in enemies:
        if hero_rect.colliderect(enemy):
            return True
    return False

# Main game loop
def game_loop():
    global hero_x, hero_y, enemies
    
    running = True
    score = 0

    while running:
        screen.fill(WHITE)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Move the hero
        hero_x, hero_y = move_hero(hero_x, hero_y)
        
        # Move the enemies
        if random.random() < 0.02:  # Random chance to create a new enemy
            new_enemy_x = random.randint(0, width - enemy_width)
            enemies.append([new_enemy_x, -enemy_height])
        
        move_enemies()

        # Draw the hero
        draw_hero(hero_x, hero_y)

        # Draw the enemies
        draw_enemies()

        # Check for collision
        hero_rect = pygame.Rect(hero_x, hero_y, hero_width, hero_height)
        if check_collision(hero_rect, enemies):
            running = False

        # Display score
        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))
        
        # Increase score as time passes
        score += 1

        # Update the screen
        pygame.display.update()

        # Control the frame rate
        clock.tick(60)

    pygame.quit()

# Run the game
game_loop()
