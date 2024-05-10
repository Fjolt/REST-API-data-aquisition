import logging
import pygame
import os

from data_aquisition import load_data
from data_handling import UseOfData, export_data
from interface import Button

# Path to histogram made from data
IMAGE_PATH = 'csv_data_statistics/histogram_state.png'


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="logs.log"
    )

    pygame.init()
    button1 = Button("Create pretty CSV files", (100, 100))
    button2 = Button("Get data for statistics", (100, 200))

    buttons = [button1, button2]
    screen = pygame.display.set_mode((800, 700))
    pygame.display.set_caption("User Interface")

    running: bool = True

    while running:
        screen.fill((0,0,0))

        if os.path.exists(IMAGE_PATH):
            image: pygame.Surface = pygame.image.load(IMAGE_PATH)
            resized_img: pygame.Surface = pygame.transform.scale(image, (500, 350))
            screen.blit(resized_img, (100, 300))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                if buttons[0].rect.collidepoint(event.pos):
                    # Button for pretty csv format creation
                    users,jobs = load_data()
                    export_data(UseOfData.PRETTY, users, jobs)

                elif buttons[1].rect.collidepoint(event.pos):
                    # Button for statistics csv creation
                    users,jobs = load_data()
                    export_data(UseOfData.USEFUL, users, jobs)

        # Draw buttons
        for button in buttons:
            button.is_hovered = button.rect.collidepoint(pygame.mouse.get_pos())
            button.draw(screen)

        pygame.display.flip()

    pygame.quit()

    export_data(UseOfData.PRETTY, users, jobs)

if __name__ == '__main__':
    main()
