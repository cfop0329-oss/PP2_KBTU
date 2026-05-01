# Imports
import pygame, sys
from pygame.locals import K_LEFT, K_RIGHT, QUIT
import random, time
import os

# Base directory so files load correctly from any working directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Initializing pygame and sound mixer
pygame.init()
pygame.mixer.init()

# Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

# Defining colors as RGB tuples
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)

# Game variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0  # Variable to track collected coins

# Difficulty Scaling Variable
# Every time this many coins are collected, the game speed increases
COINS_TO_SPEED_UP = 5 

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background image
# Ensure you have an 'images' folder with 'street.png' in the same directory
try:
    background = pygame.image.load(os.path.join(BASE_DIR, "images", "street.png"))
except FileNotFoundError:
    # Fallback if image is missing: create a simple gray surface
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background.fill(GREEN)

# Create the display surface
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer Game")

# Load and play background music on infinite loop
try:
    pygame.mixer.music.load(os.path.join(BASE_DIR, "music", "background.wav"))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
except FileNotFoundError:
    pass # Continue without music if file is missing


class Enemy(pygame.sprite.Sprite):
    """
    Represents the enemy car (car2) coming from the top.
    """
    def __init__(self, *groups):
        super().__init__(*groups)
        try:
            self.image = pygame.image.load(os.path.join(BASE_DIR, "images", "car2.png"))
        except FileNotFoundError:
            self.image = pygame.Surface((40, 70))
            self.image.fill(RED)
        
        self.rect = self.image.get_rect()
        # Spawn at random x position at the top
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        # Move down based on current global SPEED
        self.rect.move_ip(0, SPEED)
        
        # If enemy goes off screen, reset to top and increase score
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    """
    Represents the player's car (car1).
    """
    def __init__(self, *groups):
        super().__init__(*groups)
        try:
            self.image = pygame.image.load(os.path.join(BASE_DIR, "images", "car1.png"))
        except FileNotFoundError:
            self.image = pygame.Surface((40, 70))
            self.image.fill(BLUE)
            
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        # Move Left if within screen bounds
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        
        # Move Right if within screen bounds
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    """
    Represents a collectible coin.
    Feature: Random weights (1, 2, 3) affecting size and potentially score value.
    """
    def __init__(self, *groups):
        super().__init__(*groups)
        
        # Assign a random weight: 1, 2, or 3
        self.weight = random.randint(1, 3)
        
        # Size of the coin depends on its weight
        # Weight 1: Small, Weight 2: Medium, Weight 3: Large
        radius = 5 + (self.weight * 3) 
        diameter = radius * 2
        
        # Create a transparent surface for the coin
        self.image = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        
        # Draw the coin (Yellow circle with black border)
        center_pos = (radius, radius)
        pygame.draw.circle(self.image, YELLOW, center_pos, radius)
        pygame.draw.circle(self.image, BLACK, center_pos, radius, 2)
        
        self.rect = self.image.get_rect()
        # Spawn at random x position at top of screen
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)

    def move(self):
        # Coins fall slightly slower than enemies for visual variety
        self.rect.move_ip(0, SPEED * 0.8)
        
        # If coin goes off screen uncollected, respawn at top
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()

    def respawn(self):
        """Resets the coin to the top with a new random position and weight."""
        self.weight = random.randint(1, 3)
        radius = 5 + (self.weight * 3)
        diameter = radius * 2
        
        # Recreate image to match new weight size
        self.image = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (radius, radius), radius)
        pygame.draw.circle(self.image, BLACK, (radius, radius), radius, 2)
        
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)


# ---------------------- SETUP SPRITES ----------------------

P1 = Player()
E1 = Enemy()

# Create a group for enemies
enemies = pygame.sprite.Group()
enemies.add(E1)

# Create a group for coins
# We start with 3 coins on screen for better gameplay flow
coins = pygame.sprite.Group()
for _ in range(3):
    new_coin = Coin()
    coins.add(new_coin)

# Group containing all sprites (Player, Enemy, Coins) for drawing
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(coins)

# User event to increase speed gradually over time (optional difficulty creep)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# -------------------- GAME LOOP --------------------
while True:

    for event in pygame.event.get():
        # Gradual speed increase every second
        if event.type == INC_SPEED:
            SPEED += 0.2
            
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    DISPLAYSURF.blit(background, (0, 0))

    # Display Score (Top Left)
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Display Coins Collected (Top Right)
    coin_text = font_small.render("Coins: " + str(COINS), True, YELLOW)
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 100, 10))

    # Move and draw all sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # --- LOGIC: Collecting Coins ---
    # Check if Player rect collides with any coin in the coins group
    collected_coins = pygame.sprite.spritecollide(P1, coins, False)
    
    for coin in collected_coins:
        # Increase coin count by the weight of the specific coin collected
        COINS += coin.weight
        
        # FEATURE: Increase Enemy Speed when player earns N coins
        # We check if the total coins collected is a multiple of COINS_TO_SPEED_UP
        if COINS > 0 and COINS % COINS_TO_SPEED_UP == 0:
            SPEED += 1.5  # Boost speed significantly
            # Optional: Flash screen or play sound here to indicate speed up
            
        # Respawn the collected coin to keep the game going
        coin.respawn()

    # --- LOGIC: Collision with Enemy ---
    if pygame.sprite.spritecollideany(P1, enemies):
        # Stop music and play crash sound
        pygame.mixer.music.stop()
        try:
            crash_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "music", "crash.wav"))
            crash_sound.play()
        except FileNotFoundError:
            pass
        
        time.sleep(1) # Pause briefly before showing Game Over

        # Fill screen with red
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        # Show final stats
        final_stats = font_small.render(f"Score: {SCORE} | Coins: {COINS}", True, BLACK)
        DISPLAYSURF.blit(final_stats, (100, 350))

        pygame.display.update()
        
        # Clean up sprites
        for entity in all_sprites:
            entity.kill()
            
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Update display and tick clock
    pygame.display.update()
    FramePerSec.tick(FPS)