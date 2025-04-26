import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

 
# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Kecepatan permainan
clock = pygame.time.Clock()
FPS = 60

# Mengatur burung
bird_width = 34
bird_height = 24
bird_x = 50
bird_y = HEIGHT // 2
bird_y_change = 0
gravity = 0.5
jump_speed = -8

# Mengatur pipa
pipe_width = 70
pipe_height = random.randint(150, 400)
pipe_gap = 150
pipe_x = WIDTH
pipe_speed = 5

# Skor
score = 0
font = pygame.font.SysFont("Arial", 30)

# Fungsi untuk menggambar burung
def draw_bird(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, bird_width, bird_height))

# Fungsi untuk menggambar pipa
def draw_pipe(x, height):
    pygame.draw.rect(screen, BLACK, (x, 0, pipe_width, height))  # Pipa atas
    pygame.draw.rect(screen, BLACK, (x, height + pipe_gap, pipe_width, HEIGHT))  # Pipa bawah

# Fungsi utama
def main():
    global bird_y, bird_y_change, pipe_x, pipe_height, score

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_y_change = jump_speed

        # Mengatur gravitasi
        bird_y_change += gravity
        bird_y += bird_y_change

        # Menggerakkan pipa
        pipe_x -= pipe_speed
        if pipe_x < -pipe_width:
            pipe_x = WIDTH
            pipe_height = random.randint(150, 400)
            score += 1  # Tambah skor saat melewati pipa

        # Menggambar burung dan pipa
        draw_bird(bird_x, bird_y)
        draw_pipe(pipe_x, pipe_height)

        # Cek tabrakan
        if (bird_y > HEIGHT or bird_y < 0 or
                (pipe_x < bird_x + bird_width < pipe_x + pipe_width and
                 (bird_y < pipe_height or bird_y + bird_height > pipe_height + pipe_gap))):
            print("Game Over! Skor Anda:", score)
            running = False

        # Menampilkan skor
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()