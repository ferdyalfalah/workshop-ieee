import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Kecepatan permainan
clock = pygame.time.Clock()
FPS = 60

# Mengatur karakter dino
dino_width = 40
dino_height = 40
dino_x = 50
dino_y = HEIGHT - dino_height - 10
dino_y_change = 0
gravity = 1
jump_speed = 15
is_jumping = False

# Mengatur rintangan
cactus_width = 20
cactus_height = 40
cactus_x = WIDTH
cactus_y = HEIGHT - cactus_height - 10
cactus_speed = 7

# Fungsi untuk menggambar dino
def draw_dino(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, dino_width, dino_height))

# Fungsi untuk menggambar kaktus
def draw_cactus(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, cactus_width, cactus_height))

# Fungsi utama
def main():
    global dino_y, dino_y_change, is_jumping, cactus_x

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jumping:
                    dino_y_change = -jump_speed
                    is_jumping = True

        # Mengatur gravitasi
        if is_jumping:
            dino_y += dino_y_change
            dino_y_change += gravity
            if dino_y >= HEIGHT - dino_height - 10:
                dino_y = HEIGHT - dino_height - 10
                is_jumping = False

        # Menggerakkan kaktus
        cactus_x -= cactus_speed
        if cactus_x < 0:
            cactus_x = WIDTH + random.randint(100, 300)

        # Menggambar dino dan kaktus
        draw_dino(dino_x, dino_y)
        draw_cactus(cactus_x, cactus_y)

        # Cek tabrakan
        if (dino_x + dino_width > cactus_x and dino_x < cactus_x + cactus_width and
                dino_y + dino_height > cactus_y):
            print("Game Over!")
            running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()