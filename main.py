import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 10

# Colors
BABY_PINK = (255, 182, 193)  # RGB for baby pink
PURPLE = (128, 0, 128)
BLUE = (0, 0, 128)
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Ball properties
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_speed_x = BALL_SPEED
ball_speed_y = BALL_SPEED

# Paddles
paddle_a = pygame.Rect(50, HEIGHT // 2 - 60, 10, 120)
paddle_b = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 60, 10, 120)

# Scores
score_a = 0
score_b = 0

# Fonts
font = pygame.font.Font(None, 36)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Paddle movement
    if keys[pygame.K_w] and paddle_a.top > 0:
        paddle_a.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle_a.bottom < HEIGHT:
        paddle_a.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle_b.top > 0:
        paddle_b.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle_b.bottom < HEIGHT:
        paddle_b.y += PADDLE_SPEED

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed_x = -ball_speed_x

    # Score
    if ball.left <= 0:
        score_b += 1
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_speed_x = BALL_SPEED

    if ball.right >= WIDTH:
        score_a += 1
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_speed_x = -BALL_SPEED

    # Clear the screen with baby pink background
    screen.fill(BABY_PINK)

    # Draw paddles, ball, and scores with purple and blue colors
    pygame.draw.rect(screen, PURPLE, paddle_a)
    pygame.draw.rect(screen, BLUE, paddle_b)
    pygame.draw.ellipse(screen, WHITE, ball)
    score_display = font.render(f"{score_a} - {score_b}", True, WHITE)
    screen.blit(score_display, (WIDTH // 2 - 36, 20))

    # Update the display
    pygame.display.flip()

    # Control game speed
    pygame.time.Clock().tick(60)
