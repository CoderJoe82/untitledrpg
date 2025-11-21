import pygame

class Button():
    def __init__(self, x, y, width, height, text, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)
        #Render the text
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        #Center the text on the button
        text_rect = text_surface.get_rect(center = self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered(event.pos):
                return True
        return False