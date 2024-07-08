import pygame

pygame.init()

width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rysowanie kształtów")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


def draw_circle_with_square() -> None:
    screen.fill(WHITE)
    circle_radius = min(width, height) // 4
    pygame.draw.circle(screen, BLACK, (width // 2, height // 2), circle_radius)
    square_size = circle_radius // 2
    pygame.draw.rect(screen, YELLOW, (width // 2 - square_size // 2, height // 2 - square_size // 2, square_size, square_size))


def draw_green_rectangle_with_triangle_cut() -> None:
    screen.fill(WHITE)  # Tło białe
    rect_width, rect_height = width // 2, height // 2
    rect_x, rect_y = width // 4, height // 4
    pygame.draw.rect(screen, GREEN, (rect_x, rect_y, rect_width, rect_height))

    triangle_base = rect_width
    triangle_height = rect_height // 2
    triangle_x = rect_x
    triangle_y = rect_y + rect_height

    pygame.draw.polygon(screen, WHITE, [(triangle_x, triangle_y), (triangle_x + triangle_base, triangle_y), (triangle_x + triangle_base // 2, triangle_y - triangle_height)])


def draw_blue_rectangle_with_triangles() -> None:
    screen.fill(WHITE)
    rect_width, rect_height = width // 2, height // 4
    rect_x, rect_y = width // 4, height // 3
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    points = [(rect_x + rect_width / 2, rect_y), (rect_x + rect_width / 4, height * 0.2), (rect_x + rect_width * 0.75, height * 0.2)]
    points2 = [(rect_x + rect_width / 2, rect_y + rect_height), (rect_x + rect_width / 4, height * 0.75), (rect_x + rect_width * 0.75, height * 0.75)]
    pygame.draw.polygon(screen, BLUE, points)
    pygame.draw.polygon(screen, BLUE, points2)


def draw_letter_Z() -> None:
    screen.fill(WHITE)
    z_width, z_height = width // 2, height // 2
    z_x, z_y = width // 4, height // 4
    pygame.draw.line(screen, RED, (z_x, z_y), (z_x + z_width, z_y), 10)
    pygame.draw.line(screen, RED, (z_x + z_width, z_y), (z_x, z_y + z_height), 10)
    pygame.draw.line(screen, RED, (z_x, z_y + z_height), (z_x + z_width, z_y + z_height), 10)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                draw_circle_with_square()
            elif event.key == pygame.K_2:
                draw_green_rectangle_with_triangle_cut()
            elif event.key == pygame.K_3:
                draw_blue_rectangle_with_triangles()
            elif event.key == pygame.K_4:
                draw_letter_Z()
            pygame.display.flip()

pygame.quit()

