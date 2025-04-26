import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Among Us")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Kecepatan permainan
clock = pygame.time.Clock()
FPS = 60

# Mengatur karakter crewmate
crewmate_width = 40
crewmate_height = 60
crewmate_x = WIDTH // 2
crewmate_y = HEIGHT // 2
crewmate_speed = 5

# Fungsi untuk menggambar crewmate
def draw_crewmate(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, crewmate_width, crewmate_height))  # Badan
    pygame.draw.circle(screen, WHITE, (x + crewmate_width // 2, y + 10), 10)  # Kepala
    pygame.draw.rect(screen, BLACK, (x + 10, y + 20, 20, 30))  # Ransel

# Fungsi utama
def main():
    global crewmate_x, crewmate_y

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and crewmate_x > 0:
            crewmate_x -= crewmate_speed
        if keys[pygame.K_RIGHT] and crewmate_x < WIDTH - crewmate_width:
            crewmate_x += crewmate_speed
        if keys[pygame.K_UP] and crewmate_y > 0:
            crewmate_y -= crewmate_speed
        if keys[pygame.K_DOWN] and crewmate_y < HEIGHT - crewmate_height:
            crewmate_y += crewmate_speed

        # Menggambar crewmate
        draw_crewmate(crewmate_x, crewmate_y)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()