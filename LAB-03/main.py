import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Centered Blue Shapes')

# Colors
blue = (0, 0, 255)
background_color = (255, 255, 255)

# Fill the background
screen.fill(background_color)

# Define the shapes' positions for a centered layout
# Vertical offsets for spacing and centering
vertical_offset_triangle = 200  # Adjust as needed to fit the design
vertical_offset_rectangle = vertical_offset_triangle + 50  # Rectangle height + some space
vertical_offset_second_triangle = vertical_offset_rectangle + 50  # Additional space for the second triangle

# First triangle (rotated 180 degrees) at the top
triangle1_points = [(250, vertical_offset_triangle), (350, vertical_offset_triangle), (300, vertical_offset_triangle + 50)]

# Rectangle directly below the first triangle
rectangle_y = vertical_offset_rectangle
rectangle = (250, rectangle_y, 100, 50)

# Second triangle below the rectangle
triangle2_points = [(250, vertical_offset_second_triangle + 50), (350, vertical_offset_second_triangle + 50), (300, vertical_offset_second_triangle)]

# Drawing the shapes centered
pygame.draw.polygon(screen, blue, triangle1_points)
pygame.draw.rect(screen, blue, rectangle)
pygame.draw.polygon(screen, blue, triangle2_points)

# Update the display
pygame.display.flip()

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
