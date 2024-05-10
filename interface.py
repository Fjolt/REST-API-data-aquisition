import pygame
from typing import List

# Coordinates of the first main button
# And size parameters of csv choice buttons
CSV_CHOICE_X = 50
CSV_CHOICE_Y = 25
CSV_CHOICE_HEIGHT = 50
CSV_CHOICE_WIDTH = 300

# Button class
class Button:
    def __init__(self, text, position = (CSV_CHOICE_X, CSV_CHOICE_Y),
                 height=CSV_CHOICE_HEIGHT, width=CSV_CHOICE_WIDTH, text_size=30,
                 color=(0, 150, 50)):
        self.text = text
        self.font = pygame.font.Font(None, text_size)
        self.color = color
        self.hover_color = (0, 50, 150)
        self.position = position
        self.width, self.height = width, height
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        self.is_hovered = False

    def draw(self, screen):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


# Initializes all buttons used in our interface
# There are 3 types: export choice, graph choice and coumn choice.
def buttons_init() -> List[Button]:
    # Main big buttons to choose the way of export.
    # These trigger data aqusition.
    button1 = Button("Create pretty CSV files")
    button2 = Button("Get data for statistics", position=(CSV_CHOICE_X, CSV_CHOICE_Y + 100))

    button_small_height = 30
    button_small_width = 150

    graph_choice_x = CSV_CHOICE_X + CSV_CHOICE_WIDTH  + 50
    graph_choice_color = (50, 0, 200)

    # Smaller buttons to choose the type of the graph.
    button_small1 = Button("Bar plot", (graph_choice_x, CSV_CHOICE_Y),
                           height=button_small_height, width=button_small_width, text_size=25,
                           color=graph_choice_color)
    button_small2 = Button("Line plot", (graph_choice_x, CSV_CHOICE_Y + 2*button_small_height),
                           height=button_small_height, width=button_small_width, text_size=25,
                           color=graph_choice_color)

    column_choice_x = graph_choice_x + button_small_width  + 50
    column_choice_color = (100, 0, 50)

    # Smaller buttons to choose which column to take the data from.
    button_small3 = Button("Status", (column_choice_x, CSV_CHOICE_Y),
                           height=button_small_height, width=button_small_width, text_size=25,
                           color=column_choice_color)
    button_small4 = Button("State", (column_choice_x, CSV_CHOICE_Y + 2*button_small_height),
                           height=button_small_height, width=button_small_width, text_size=25,
                           color=column_choice_color)
    button_small5 = Button("Type", (column_choice_x, CSV_CHOICE_Y + 4*button_small_height),
                           height=button_small_height, width=button_small_width, text_size=25,
                           color=column_choice_color)

    return [button1, button2, button_small1, button_small2, button_small3,
            button_small4, button_small5]