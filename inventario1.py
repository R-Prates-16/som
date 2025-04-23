import pygame

class Inventario1:
    def __init__(self):
        pygame.init()
        
        self.DARK_GRAY = (50, 50, 50)
        self.WHITE = (255, 255, 255)
        self.font = pygame.font.Font(None, 50)  # Aumentado
        self.title_font = pygame.font.Font(None, 55)  # Aumentado um pouco para "Guerreiro"
        
        self.inventory_open = False
        self.inventory_rect = pygame.Rect(80, 80, 500, 600)  # Aumentado
        
        # Carregar imagens
        self.bg_image = pygame.image.load("fundo.jpeg")
        self.bg_image = pygame.transform.scale(self.bg_image, (500, 600))  # Ajustado para o novo tamanho

        self.character_image = pygame.image.load("personagem.png")
        self.character_image = pygame.transform.scale(self.character_image, (80, 80))  # Ajustado proporcionalmente
        
        self.items = [
            ("Espada", pygame.image.load("espada.png")),
            ("Escudo", pygame.image.load("escudo.png")),
            ("Armadura", pygame.image.load("armadura.png")),
            ("Poção", pygame.image.load("pocao.png")),
            ("Velocidade", pygame.image.load("velocidade.png"))
        ]
        
        # Ajustar tamanhos e deslocamento
        for i in range(len(self.items)):
            if self.items[i][0] == "Poção":
                new_size = (55, 55)  # Ajustado proporcionalmente
            elif self.items[i][0] == "Armadura":
                new_size = (60, 60)  # Ajustado proporcionalmente
            else:
                new_size = (40, 40)  # Ajustado proporcionalmente
            
            self.items[i] = (self.items[i][0], pygame.transform.scale(self.items[i][1], new_size))

    def draw_inventory(self, screen):
        pygame.draw.rect(screen, self.DARK_GRAY, self.inventory_rect, border_radius=25)  # Ajustado
        screen.blit(self.bg_image, (self.inventory_rect.x, self.inventory_rect.y))

        # Desenhar círculo transparente do personagem
        circle_x = self.inventory_rect.x + 120  # Ajustado
        circle_y = self.inventory_rect.y + 100  # Ajustado
        s = pygame.Surface((100, 100), pygame.SRCALPHA)  # Ajustado
        pygame.draw.circle(s, (255, 255, 255, 100), (50, 50), 50)  # Ajustado
        screen.blit(s, (circle_x - 50, circle_y - 50))

        # Posicionar personagem dentro do círculo
        char_x = circle_x - self.character_image.get_width() // 2 - 3
        char_y = circle_y - self.character_image.get_height() // 2
        screen.blit(self.character_image, (char_x, char_y))

        # Nome do personagem
        text = self.title_font.render("Guerreiro", True, self.WHITE)  # Usando a fonte aumentada
        screen.blit(text, (self.inventory_rect.x + 220, self.inventory_rect.y + 80))  # Ajustado

        # Desenhar os itens do inventário
        for i, (item_name, item_image) in enumerate(self.items):
            x_offset = -10 if item_name in ["Poção", "Armadura"] else 0  # Ajustado
            x = self.inventory_rect.left + 50 + x_offset  # Ajustado
            y = self.inventory_rect.top + 200 + i * 60  # Ajustado
            screen.blit(item_image, (x, y))

            text = self.font.render(item_name, True, self.WHITE)
            screen.blit(text, (self.inventory_rect.left + 120, y + 5))  # Ajustado

    def get_item_at(self, pos):
        for i, (item_name, item_image) in enumerate(self.items):
            x_offset = -10 if item_name in ["Poção", "Armadura"] else 0
            x = self.inventory_rect.left + 50 + x_offset
            y = self.inventory_rect.top + 200 + i * 60
            if pygame.Rect(x, y, 250, 50).collidepoint(pos):
                return (item_name, item_image)
        return None

