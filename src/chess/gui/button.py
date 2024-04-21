import pygame as p

class Button:
    def __init__(self, text, position, size):
        self.text = text
        self.position = position
        self.size = size
        self.font = p.font.Font(None, 28)
        self.color = p.Color('gray')

    def draw(self, screen):
        p.draw.rect(screen, self.color, (self.position[0], self.position[1], self.size[0], self.size[1]))
        text_surface = self.font.render(self.text, True, p.Color('white'))
        text_rect = text_surface.get_rect(center=(self.position[0] + self.size[0] / 2, self.position[1] + self.size[1] / 2))
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return (self.position[0] < mouse_pos[0] < self.position[0] + self.size[0] and
                self.position[1] < mouse_pos[1] < self.position[1] + self.size[1])
