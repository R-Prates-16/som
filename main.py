import pygame
from inventario1 import Inventario1
from inventario2 import Inventario2

class Jogo:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

        self.BLACK = (0, 0, 0)
        self.RED = (200, 0, 0)
        self.WHITE = (255, 255, 255)

        self.button_rect = pygame.Rect(self.WIDTH - 150, self.HEIGHT - 100, 140, 60)  # Botão vermelho

        self.dragging_item = None
        self.dragging_from = None

        self.inventario1 = Inventario1()
        self.inventario2 = Inventario2()

        self.running = True

    def run(self):
        while self.running:
            self.screen.fill(self.BLACK)

            for event in pygame.event.get():
                self.handle_event(event)

            if self.inventario1.inventory_open:
                self.inventario1.draw_inventory(self.screen)
            if self.inventario2.inventory_open:
                self.inventario2.draw_inventory(self.screen)

            self.draw_button()

            if self.dragging_item:
                self.draw_dragging_item()

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LALT, pygame.K_RALT):
                self.inventario1.inventory_open = not self.inventario1.inventory_open
            if event.key == pygame.K_ESCAPE:
                self.running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.inventario2.inventory_open = not self.inventario2.inventory_open

            if self.inventario1.inventory_open:
                item = self.inventario1.get_item_at(event.pos)
                if item:
                    self.dragging_item = item
                    self.dragging_from = "inventory1"

            if self.inventario2.inventory_open:
                item = self.inventario2.get_item_at(event.pos)
                if item:
                    self.dragging_item = item
                    self.dragging_from = "inventory2"

        if event.type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_button_up(event)

    def handle_mouse_button_up(self, event):
        if self.dragging_item:
            if self.inventario2.inventory_open and self.inventario2.inventory_rect.collidepoint(event.pos) and self.dragging_from == "inventory1":
                if self.dragging_item in self.inventario1.items:
                    self.inventario1.items.remove(self.dragging_item)
                    self.inventario2.items.append(self.dragging_item)

            elif self.inventario1.inventory_open and self.inventario1.inventory_rect.collidepoint(event.pos) and self.dragging_from == "inventory2":
                if self.dragging_item in self.inventario2.items:
                    self.inventario2.items.remove(self.dragging_item)
                    self.inventario1.items.append(self.dragging_item)

            self.dragging_item = None
            self.dragging_from = None

    def draw_button(self):
        pygame.draw.rect(self.screen, self.RED, self.button_rect, border_radius=10)
        text = self.inventario1.font.render("Abrir", True, self.WHITE)
        self.screen.blit(text, (self.button_rect.x + 20, self.button_rect.y + 10))

    def draw_dragging_item(self):
        text = self.inventario1.font.render(self.dragging_item[0], True, self.WHITE)
        self.screen.blit(text, pygame.mouse.get_pos())

if __name__ == "__main__":
    jogo = Jogo()
    jogo.run()
