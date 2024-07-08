import pygame
import math
from typing import Tuple

class Polygon:
    def __init__(self) -> None:
        self.screen_width: int = 600
        self.screen_height: int = 600
        self.poly: pygame.Surface = None
        self.points: list[Tuple[int, int]] = []
        self.original_points: list[Tuple[int, int]] = []
        self.center_x: int = self.screen_width // 2
        self.center_y: int = self.screen_height // 2

    def draw_polygon(self, n: int) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Wielokat")
        self.clock = pygame.time.Clock()

        radius: int = min(self.screen_width, self.screen_height) // 4

        angles: list[float] = [2 * math.pi * i / n for i in range(n)]
        self.points = [
            (int(self.center_x + radius * math.cos(angle)),
             int(self.center_y + radius * math.sin(angle)))
            for angle in angles
        ]
        self.original_points = self.points.copy()

        self.poly = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
        pygame.draw.polygon(self.poly, (0, 0, 0), self.points)

        running: bool = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        self.transform_polygon(0)
                    elif event.key == pygame.K_1:
                        self.transform_polygon(1)
                    elif event.key == pygame.K_2:
                        self.transform_polygon(2)
                    elif event.key == pygame.K_3:
                        self.transform_polygon(3)
                    elif event.key == pygame.K_4:
                        self.transform_polygon(4)
                    elif event.key == pygame.K_5:
                        self.transform_polygon(5)
                    elif event.key == pygame.K_6:
                        self.transform_polygon(6)
                    elif event.key == pygame.K_7:
                        self.transform_polygon(7)
                    elif event.key == pygame.K_8:
                        self.transform_polygon(8)
                    elif event.key == pygame.K_9:
                        self.transform_polygon(9)

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.poly, (0, 0))
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def transform_polygon(self, option: int) -> None:
        match option:
            case 0:
                self.reset_polygon()
            case 1:
                self.scale_polygon(0.5, 0.5)
            case 2:
                self.rotate_polygon(45)
            case 3:
                self.rotate_polygon(90)
            case 4:
                self.shear_polygon(0.5, 0)
            case 5:
                self.flatten_top()
            case 6:
                self.shear_polygon(0.5, 0)
                self.rotate_polygon(90)
            case 7:
                self.rotate_polygon(180)
                self.scale_polygon(1, 1.2)
            case 8:
                self.rotate_polygon(90)
                self.align_bottom()
            case 9:
                self.shear_and_align_right()

    def reset_polygon(self) -> None:
        self.points = self.original_points.copy()
        self.poly = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
        pygame.draw.polygon(self.poly, (0, 0, 0), self.points)

    def scale_polygon(self, scale_x: float, scale_y: float) -> None:
        new_points = [(int(self.center_x + (x - self.center_x) * scale_x), 
                       int(self.center_y + (y - self.center_y) * scale_y)) for x, y in self.points]
        self.poly = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
        pygame.draw.polygon(self.poly, (0, 0, 0), new_points)
        self.points = new_points

    def rotate_polygon(self, angle: float) -> None:
        rotated_poly = pygame.transform.rotate(self.poly, angle)
        self.poly = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
        self.poly.blit(rotated_poly, (self.screen_width // 2 - rotated_poly.get_width() // 2,
                                      self.screen_height // 2 - rotated_poly.get_height() // 2))
        self.points = self.get_rotated_points(angle)

    def shear_polygon(self, shear_x: float, shear_y: float) -> None:
        new_points = [(int(x + shear_x * (y - self.center_y)), 
                       int(y + shear_y * (x - self.center_x))) for x, y in self.points]
        self.poly = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
        pygame.draw.polygon(self.poly, (0, 0, 0), new_points)
        self.points = new_points

    def flatten_top(self) -> None:
        new_points = [(x, self.center_y - abs(y - self.center_y) // 2) for x, y in self.points]
        min_y = min(y for x, y in new_points)
        shift_y = self.center_y - min_y
        new_points = [(x, y + shift_y) for x, y in new_points]
        self.poly = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
        pygame.draw.polygon(self.poly, (0, 0, 0), new_points)
        self.points = new_points

    def align_bottom(self) -> None:
        bottom_y = max(y for x, y in self.points)
        shift_y = self.screen_height - bottom_y
        self.points = [(x, y + shift_y) for x, y in self.points]
        self.poly = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
        pygame.draw.polygon(self.poly, (0, 0, 0), self.points)

    def shear_and_align_right(self) -> None:
        self.shear_polygon(0.5, 0)
        max_x = max(x for x, y in self.points)
        shift_x = self.screen_width - max_x
        min_x = min(x for x, y in self.points)
        shift_y = self.center_y - min_x // 2
        new_points = [(x + shift_x, y + shift_y) for x, y in self.points]
        self.poly = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
        pygame.draw.polygon(self.poly, (0, 0, 0), new_points)
        self.points = new_points

    def get_rotated_points(self, angle: float) -> list[Tuple[int, int]]:
        angle_rad = math.radians(angle)
        new_points = []
        for x, y in self.points:
            new_x = self.center_x + (x - self.center_x) * math.cos(angle_rad) - (y - self.center_y) * math.sin(angle_rad)
            new_y = self.center_y + (x - self.center_x) * math.sin(angle_rad) + (y - self.center_y) * math.cos(angle_rad)
            new_points.append((int(new_x), int(new_y)))
        return new_points

if __name__ == "__main__":
    polygon = Polygon()
    n = int(input("Wprowadź liczbę stron: "))
    polygon.draw_polygon(n)