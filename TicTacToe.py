import pygame
import sys
import os

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption("TIC TAC TOE")
clock = pygame.time.Clock()

# Helper function to safely load images
def load_image_safe(filename, convert_alpha=False):
    try:
        image = pygame.image.load(filename)
        return image.convert_alpha() if convert_alpha else image.convert()
    except pygame.error as e:
        print(f"Error loading image '{filename}': {e}")
        return pygame.Surface((100, 100))  # fallback blank surface

# Load and prepare assets
icon_image = load_image_safe('captionimage.png')
pygame.display.set_icon(icon_image)

background = load_image_safe('backgroundimage.png')
background = pygame.transform.scale(background, (800, 700))

title_image = load_image_safe('titleimagewhite.png', convert_alpha=True)
title_rect = title_image.get_rect(center=(400, 150))

button_clicked = load.image.load('Playclicked.png')
button_unclicked = load_image_safe('Playunclick.png')
button_clicked = pygame.transform.scale(button_clicked, (200, 100))
button_unclicked = pygame.transform.scale(button_unclicked, (200, 100))
button_rect = button_unclicked.get_rect(center=(400, 400))

# Button and color animation state
clicked = False
color_cycle = [(255, 255, 255), (255, 0, 0), (255, 165, 0), (255, 255, 0),
               (0, 255, 0), (0, 255, 255), (0, 0, 255), (255, 0, 255)]
color_index = 0
color_timer = 0
color_interval = 300  # milliseconds

# Main loop
while True:
    dt = clock.tick(60)  # Limit to 60 FPS
    color_timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if button_rect.collidepoint(event.pos) and clicked:
                clicked = False

    # Cycle title tint color
    if color_timer >= color_interval:
        color_timer = 0
        color_index = (color_index + 1) % len(color_cycle)

    tinted_title = title_image.copy()
    tint = pygame.Surface(tinted_title.get_size(), pygame.SRCALPHA)
    tint.fill(color_cycle[color_index])
    tinted_title.blit(tint, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    # Draw everything
    screen.blit(background, (0, 25))
    screen.blit(tinted_title, title_rect)
    screen.blit(button_clicked if clicked else button_unclicked, button_rect)

    # Update only changed areas
    pygame.display.update([title_rect, button_rect])