import pygame
import sys 

# Initialize Pygame
pygame.init()

# these conditions must be Constant
WIDTH, HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 50

OBSTACLE_COLOR = (0, 80, 220)
SPEED = 5
GRAVITY = 1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
greenbackground_img = pygame.image.load("assets/greengrass.jpg")

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Running Obstacle Game")



# Initialize player's position and velocity
player_x, player_y = WIDTH // 4, HEIGHT // 2
player_velocity = 0

#  store obstacles
obstacles = []

# Clock to control the frame rate
clock = pygame.time.Clock()

#  this Function  helps us to generate  new obstacles
def spawn_obstacle():
    obstacle_x = WIDTH
    obstacle_y = random.randint(0, HEIGHT - OBSTACLE_HEIGHT)
    obstacles.append([obstacle_x, obstacle_y])

# Game loop
running = True
score = 0

while running:
    screen.blit(greenbackground_img,(0, 530))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #  player input conditions
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player_velocity = -15  # Jump by setting a negative velocity

    #  this helps us Update player position
    player_y += player_velocity
    player_velocity += GRAVITY

    # Keep the player within the screen bounds
    if player_y >= HEIGHT - PLAYER_HEIGHT:
        player_y = HEIGHT - PLAYER_HEIGHT
        player_velocity = 0

    # this helps when it comes to creating  new obstacles
    def random ():
        if random.randint(1, 100) < 10:
            spawn_obstacle()

    #  this helps Update obstacle positions and removes them when the player overcomes them
    for obstacle in obstacles:
        obstacle[0] -= SPEED

    obstacles = [obstacle for obstacle in obstacles if obstacle[0] > -OBSTACLE_WIDTH]

    #  this helps us Check when collisions happen
    for obstacle in obstacles:
        if (
            player_x < obstacle[0] + OBSTACLE_WIDTH
            and player_x + PLAYER_WIDTH > obstacle[0]
            and player_y < obstacle[1] + OBSTACLE_HEIGHT
            and player_y + PLAYER_HEIGHT > obstacle[1]
        ):
            running = False

    # Clear the screen

    

    # Draw the obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle[0], obstacle[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

    # Update the display
    pygame.display.update()

    # this allows us to update the score
    score += 1

    # Set the frame rate
    clock.tick(30)

# Game over
print("Game Over. Your Score:", score)

# Quit Pygame
pygame.quit()
sys.exit()








