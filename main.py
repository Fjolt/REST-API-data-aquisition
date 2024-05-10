import logging
import pygame

from data_aquisition import load_data
from data_handling import UseOfData, export_data
from interface import Button


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="logs.log"
    )
    graphs = []

    pygame.init()
    button1 = Button("Create pretty CSV files", (100, 100))
    button2 = Button("Show statistics", (100, 200))

    buttons = [button1, button2]
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("User Interface")

    running: bool = True

    while running:
        screen.fill((0,0,0))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                if buttons[0].rect.collidepoint(event.pos):
                    users,jobs = load_data()
                    export_data(UseOfData.PRETTY, users, jobs)
                elif buttons[1].rect.collidepoint(event.pos):
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
