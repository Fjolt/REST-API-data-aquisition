import logging
import pygame
import os

from data_aquisition import load_data
from data_handling import UseOfData, export_data, compute_statistics
from interface import buttons_init

# Path to graph made from data and data for statistics
IMAGE_PATH = "csv_data_statistics/graph.png"
CSV_STAT_PATH = "csv_data_statistics/jobs.csv"


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="logs.log"
    )

    pygame.init()
    logging.info('Interface initialised.')

    buttons = buttons_init()
    screen = pygame.display.set_mode((800, 700))
    pygame.display.set_caption("User Interface")

    running: bool = True
    graph_style = "bar"
    graph_col = "Status"

    while running:
        screen.fill((0,0,0))

        if os.path.exists(IMAGE_PATH):
            try:
                image: pygame.Surface = pygame.image.load(IMAGE_PATH)
                screen.blit(image, (100, 200))
                logging.info("Graph succesfully loaded.")
            except Exception as e:
                logging.error('Failed to get the graph.')
                logging.error(f'{str(e)}')

        # Handle events in pygame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                if buttons[0].rect.collidepoint(event.pos):
                    # Button for pretty csv format creation
                    users,jobs = load_data()
                    logging.info("Exporting data to pretty csv...")
                    try:
                        export_data(UseOfData.PRETTY, users, jobs)
                        logging.info("Pretty csvs have been exported")
                    except Exception as e:
                        running = False

                elif buttons[1].rect.collidepoint(event.pos):
                    # Button for statistics csv creation
                    users,jobs = load_data()
                    logging.info("Exporting data to csv...")
                    try:
                        export_data(UseOfData.USEFUL, users, jobs, graph_style)
                        logging.info("Statistics have been updated.")
                    except Exception as e:
                        running = False
                        logging.error(f'{str(e)}')

                elif buttons[2].rect.collidepoint(event.pos):
                    # Button to change GRAPH_STYLE to bar plot
                    graph_style = "bar"
                    if os.path.exists(IMAGE_PATH):
                        compute_statistics(CSV_STAT_PATH, graph_col, graph_style)

                elif buttons[3].rect.collidepoint(event.pos):
                    # Button to change GRAPH_STYLE to line plot
                    graph_style = "line"
                    if os.path.exists(IMAGE_PATH):
                        compute_statistics(CSV_STAT_PATH, graph_col, graph_style)

                elif buttons[4].rect.collidepoint(event.pos):
                    # Button to change graph_col to Status
                    graph_col = "Status"
                    if os.path.exists(IMAGE_PATH):
                        compute_statistics(CSV_STAT_PATH, graph_col, graph_style)

                elif buttons[5].rect.collidepoint(event.pos):
                    # Button to change graph_col to State
                    graph_col = "State"
                    if os.path.exists(IMAGE_PATH):
                        compute_statistics(CSV_STAT_PATH, graph_col, graph_style)

                elif buttons[6].rect.collidepoint(event.pos):
                    # Button to change graph_col to Type
                    graph_col = "Type"
                    if os.path.exists(IMAGE_PATH):
                        compute_statistics(CSV_STAT_PATH, graph_col, graph_style)

        # Draws buttons in pygame window.
        for button in buttons:
            button.is_hovered = button.rect.collidepoint(pygame.mouse.get_pos())
            button.draw(screen)

        pygame.display.flip()

    pygame.quit()

    export_data(UseOfData.PRETTY, users, jobs)

if __name__ == '__main__':
    main()
