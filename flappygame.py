import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
GRAVITY = 1
JUMP_STRENGTH = -20
PLAYER_SPEED = 10
OBSTACLE_SPEED = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Subway Surfer 2D')

# Fonts
FONT = pygame.font.Font(None, 36)

# Player class
class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 100))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        self.velocity_y = 0
        self.is_jumping = False

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.is_jumping = False

        if self.rect.top < 0:
            self.rect.top = 0

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = JUMP_STRENGTH
            self.is_jumping = True

    def move_left(self):
        self.rect.x -= PLAYER_SPEED
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.x += PLAYER_SPEED
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Obstacle class
class Obstacle:
    def __init__(self, x, y, width, height):
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= OBSTACLE_SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Game loop
def game_loop():
    clock = pygame.time.Clock()
    player = Player()
    obstacles = [Obstacle(SCREEN_WIDTH + i * 300, SCREEN_HEIGHT - 100, 50, 100) for i in range(5)]
    score = 0
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    player.jump()
                if event.key == pygame.K_LEFT:
                    player.move_left()
                if event.key == pygame.K_RIGHT:
                    player.move_right()
                if event.key == pygame.K_r and game_over:
                    player = Player()
                    obstacles = [Obstacle(SCREEN_WIDTH + i * 300, SCREEN_HEIGHT - 100, 50, 100) for i in range(5)]
                    score = 0
                    game_over = False

        if not game_over:
            player.update()

            for obstacle in obstacles:
                obstacle.update()
                if obstacle.rect.right < 0:
                    obstacle.rect.x = SCREEN_WIDTH
                    obstacle.rect.y = SCREEN_HEIGHT - 100 - random.randint(0, 100)
                    score += 1

                # Check for collisions
                if player.rect.colliderect(obstacle.rect):
                    game_over = True

        # Draw
        screen.fill(BLACK)
        player.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)

        if game_over:
            game_over_text = FONT.render("Game Over! Press 'R' to restart", True, WHITE)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2))

        score_text = FONT.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
