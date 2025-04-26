import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran papan
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Membuat layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catur")

# Memuat gambar bidak catur
pieces = {
    'b_pawn': pygame.image.load('images/b_pawn.png'),
    'b_rook': pygame.image.load('images/b_rook.png'),
    'b_knight': pygame.image.load('images/b_knight.png'),
    'b_bishop': pygame.image.load('images/b_bishop.png'),
    'b_queen': pygame.image.load('images/b_queen.png'),
    'b_king': pygame.image.load('images/b_king.png'),
    'w_pawn': pygame.image.load('images/w_pawn.png'),
    'w_rook': pygame.image.load('images/w_rook.png'),
    'w_knight': pygame.image.load('images/w_knight.png'),
    'w_bishop': pygame.image.load('images/w_bishop.png'),
    'w_queen': pygame.image.load('images/w_queen.png'),
    'w_king': pygame.image.load('images/w_king.png'),
}

# Mengatur posisi awal bidak catur
def create_board():
    board = [[None for _ in range(8)] for _ in range(8)]
    
    # Bidak hitam
    board[0] = ['b_rook', 'b_knight', 'b_bishop', 'b_queen', 'b_king', 'b_bishop', 'b_knight', 'b_rook']
    board[1] = ['b_pawn'] * 8
    
    # Bidak putih
    board[6] = ['w_pawn'] * 8
    board[7] = ['w_rook', 'w_knight', 'w_bishop', 'w_queen', 'w_king', 'w_bishop', 'w_knight', 'w_rook']
    
    return board

# Menggambar papan dan bidak
def draw_board(board):
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board[row][col]
            if piece:
                screen.blit(pieces[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

# Fungsi utama
def main():
    board = create_board()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        draw_board(board)
        pygame.display.flip()

if __name__ == "__main__":
    main()