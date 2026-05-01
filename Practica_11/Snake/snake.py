import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, QUIT, KEYDOWN, K_q
import sys
import random

# -------------------- CONSTANTS --------------------
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

GAME_ON = True

# Screen and grid settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
CELL = 10  # Each snake/food block is 10x10 pixels

# Starting speed and level
SPEED = 10
LEVEL = 1
SCORE = 0
FOOD_PER_LEVEL = 3  # Foods needed to advance to next level
FOODS_EATEN = 0     # Track how many foods eaten in current level

# Colors
BLACK  = (0,   0,   0)
WHITE  = (255, 255, 255)
RED    = (255, 0,   0)
GREEN  = (0,   200, 0)
YELLOW = (255, 215, 0)
GRAY   = (40,  40,  40)
ORANGE = (255, 165, 0)

# Timer for food disappearance
# The food will disappear if not eaten within this many frames (ticks)
# At 60 FPS, 300 frames is approx 5 seconds. 
# Note: We use clock.tick(SPEED), so this depends on game speed.
MAX_FOOD_AGE = 150 

# -------------------- SNAKE CLASS --------------------
class Snake():

    def __init__(self):
        # Snake starts as a list of (x, y) positions
        self.snake = [(200, 200), (210, 200), (220, 200), (230, 200), (240, 200)]

        # White body block
        self.skin = pygame.Surface((CELL, CELL))
        self.skin.fill(WHITE)

        # Gray head block (slightly different color)
        self.head = pygame.Surface((CELL, CELL))
        self.head.fill((200, 200, 200))

        self.direction = RIGHT

    def crawl(self, grow=False):
        """
        Move snake one step in current direction.
        If grow=True, don't remove tail (snake gets longer).
        Returns False if snake hits a wall or itself.
        """
        head_x, head_y = self.snake[-1]

        new_head = (head_x, head_y)

        # Calculate new head position based on direction
        if self.direction == RIGHT:
            new_head = (head_x + CELL, head_y)
        elif self.direction == LEFT:
            new_head = (head_x - CELL, head_y)
        elif self.direction == UP:
            new_head = (head_x, head_y - CELL)
        elif self.direction == DOWN:
            new_head = (head_x, head_y + CELL)

        # Check wall collision
        if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
                new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT):
            return False  # Snake hit the wall → game over

        # Check self collision (hit own body)
        if new_head in self.snake:
            return False  # Snake hit itself → game over

        # Add new head
        self.snake.append(new_head)

        # Only remove tail if not growing
        if not grow:
            self.snake.pop(0)

        return True  # Snake is alive


# -------------------- FOOD CLASS --------------------
class Food():

    def __init__(self, snake_body):
        # Generate first food position and properties
        self.respawn(snake_body)

    def respawn(self, snake_body):
        """
        Move food to a new random valid position.
        Assigns a random weight (1, 2, or 3).
        Resets the age timer.
        """
        self.position = self.random_position(snake_body)
        
        # Random weight: 1, 2, or 3
        self.weight = random.randint(1, 3)
        
        # Reset age timer (frames since spawn)
        self.age = 0
        
        # Create visual representation based on weight
        self.create_image()

    def random_position(self, snake_body):
        """
        Generate a random position that:
        - Is on the grid (multiples of CELL)
        - Does not overlap with the snake body
        """
        while True:
            x = random.randrange(0, SCREEN_WIDTH, CELL)
            y = random.randrange(0, SCREEN_HEIGHT, CELL)
            # Only use position if it's not on the snake
            if (x, y) not in snake_body:
                return (x, y)

    def create_image(self):
        """
        Creates the food surface. 
        Size and Color depend on the weight.
        Weight 1: Small, Green
        Weight 2: Medium, Yellow
        Weight 3: Large, Red
        """
        if self.weight == 1:
            size = CELL
            color = GREEN
        elif self.weight == 2:
            size = CELL + 4  # Slightly larger than grid cell
            color = YELLOW
        else: # Weight 3
            size = CELL + 8  # Even larger
            color = RED
            
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        
        # Draw a circle for better visuals
        radius = size // 2
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        
        # Store rect for blitting (centered on the grid position)
        self.rect = self.image.get_rect(center=(self.position[0] + CELL//2, self.position[1] + CELL//2))

    def update_timer(self):
        """
        Increment age. Returns True if food has expired.
        """
        self.age += 1
        if self.age >= MAX_FOOD_AGE:
            return True # Food expired
        return False

# -------------------- SETUP --------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game - Weighted & Timed Food")
clock = pygame.time.Clock()

# Fonts for score and level display
font = pygame.font.SysFont("Verdana", 16)
font_big = pygame.font.SysFont("Verdana", 40)

snake = Snake()

# Create first food avoiding snake's starting position
food = Food(snake.snake)


# -------------------- HELPER FUNCTIONS --------------------
def draw_grid():
    """Draw subtle grid lines on the background."""
    for x in range(0, SCREEN_WIDTH, CELL):
        pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL):
        pygame.draw.line(screen, GRAY, (0, y), (SCREEN_WIDTH, y))

def show_game_over():
    """Display game over screen with final score and level."""
    screen.fill(BLACK)
    go_text = font_big.render("GAME OVER", True, RED)
    score_text = font.render(f"Score: {SCORE}   Level: {LEVEL}", True, WHITE)
    restart_text = font.render("Press Q to quit", True, GRAY)
    screen.blit(go_text, (SCREEN_WIDTH//2 - go_text.get_width()//2, 140))
    screen.blit(score_text, (SCREEN_WIDTH//2 - score_text.get_width()//2, 210))
    screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, 260))
    pygame.display.update()

    # Wait for Q key to quit
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_q:
                    pygame.quit()
                    sys.exit()


# -------------------- GAME LOOP --------------------
while GAME_ON:
    clock.tick(SPEED)

    # Handle input events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            # Change direction but prevent reversing
            if event.key == K_UP and snake.direction != DOWN:
                snake.direction = UP
            elif event.key == K_LEFT and snake.direction != RIGHT:
                snake.direction = LEFT
            elif event.key == K_DOWN and snake.direction != UP:
                snake.direction = DOWN
            elif event.key == K_RIGHT and snake.direction != LEFT:
                snake.direction = RIGHT

    # Check if snake eats food this step
    # We check collision with the food's rect for more accuracy with different sizes
    head_rect = pygame.Rect(snake.snake[-1][0], snake.snake[-1][1], CELL, CELL)
    
    # Simple distance check or rect collider can work. 
    # Since food is centered on grid, we check if head pos matches food grid pos roughly
    # Or simpler: check if head rect collides with food rect
    grow = head_rect.colliderect(food.rect)

    # Move snake (grow if food eaten)
    alive = snake.crawl(grow=grow)

    # Stop game if snake dies
    if not alive:
        GAME_ON = False
        show_game_over()
        break

    # Logic if food was eaten
    if grow:
        # Score increases by the weight of the food
        SCORE += 10 * food.weight
        FOODS_EATEN += 1
        food.respawn(snake.snake)

        # Level up after eating FOOD_PER_LEVEL foods
        if FOODS_EATEN >= FOOD_PER_LEVEL:
            LEVEL += 1
            FOODS_EATEN = 0         # Reset food counter for new level
            SPEED += 2              # Increase speed each level
            # Note: clock.tick(SPEED) handles the delay in the next loop iteration

    else:
        # If food NOT eaten, update its timer
        if food.update_timer():
            # Food expired! Respawn it.
            food.respawn(snake.snake)

    # -------------------- DRAWING --------------------
    screen.fill(BLACK)

    # Draw subtle grid
    draw_grid()

    # Draw snake body (all except last = head)
    for snake_pos in snake.snake[:-1]:
        screen.blit(snake.skin, snake_pos)

    # Draw snake head
    screen.blit(snake.head, snake.snake[-1])

    # Draw food
    screen.blit(food.image, food.rect)

    # Draw score, level, and food info at top
    score_text = font.render(f"Score: {SCORE}", True, YELLOW)
    level_text = font.render(f"Level: {LEVEL}", True, YELLOW)
    # Show remaining time for food visually? Or just weight.
    # Let's show current food weight
    food_info = font.render(f"Food Wgt: {food.weight}", True, WHITE)
    
    # Optional: Draw a small timer bar for food
    timer_pct = 1.0 - (food.age / MAX_FOOD_AGE)
    if timer_pct > 0:
        bar_width = int(50 * timer_pct)
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - 60, 25, 50, 5)) # Background bar
        pygame.draw.rect(screen, RED, (SCREEN_WIDTH - 60, 25, bar_width, 5)) # Time left

    screen.blit(score_text, (5, 5))
    screen.blit(level_text, (SCREEN_WIDTH//2 - level_text.get_width()//2, 5))
    screen.blit(food_info, (SCREEN_WIDTH - food_info.get_width() - 5, 5))

    pygame.display.update()

pygame.quit()