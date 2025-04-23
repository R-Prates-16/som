import pygame

class Inventario2:
    def __init__(self):
        pygame.init()

        self.WHITE = (255, 255, 255)
        self.font = pygame.font.Font(None, 50)  # Ajustado para o mesmo tamanho do Inventario1
        self.title_font = pygame.font.Font(None, 60)  # Aumentado um pouco o tamanho da fonte do título

        self.inventory_open = False
        self.inventory_rect = pygame.Rect(650, 80, 500, 600)  # Movido mais para a direita
        self.items = []  # Começa vazio

        # Carrega a imagem de fundo do baú
        self.bau_fundo = pygame.image.load("fundo.jpeg")
        self.bau_fundo = pygame.transform.scale(self.bau_fundo, (self.inventory_rect.width, self.inventory_rect.height))

        # Carrega a imagem do baú para o círculo
        self.bau_image = pygame.image.load("bau.png")
        self.bau_image = pygame.transform.scale(self.bau_image, (80, 80))  # Ajustado para ficar dentro do círculo

    def draw_inventory(self, screen):
        # Desenha a imagem de fundo do inventário
        screen.blit(self.bau_fundo, self.inventory_rect.topleft)
        
        # Desenhar círculo transparente para a imagem do baú
        circle_x = self.inventory_rect.left + 120
        circle_y = self.inventory_rect.y + 100
        s = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.circle(s, (255, 255, 255, 100), (50, 50), 50)
        screen.blit(s, (circle_x - 50, circle_y - 50))

        # Posicionar a imagem do baú dentro do círculo
        bau_x = circle_x - self.bau_image.get_width() // 2 - 3
        bau_y = circle_y - self.bau_image.get_height() // 2
        screen.blit(self.bau_image, (bau_x, bau_y))

        # Escreve "Baú" ao lado do círculo
        title_text = self.title_font.render("Baú", True, self.WHITE)
        title_x = circle_x + 80  # Posiciona ao lado do círculo
        title_y = circle_y - 20  # Alinha com o centro do círculo
        screen.blit(title_text, (title_x, title_y))

        # Desenha os itens no inventário
        for i, (item_name, item_image) in enumerate(self.items):
            x, y = self.inventory_rect.left + 50, self.inventory_rect.top + 200 + i * 60  # Ajustado para novo tamanho
            screen.blit(item_image, (x, y))  # Desenha a imagem do item
            text = self.font.render(item_name, True, self.WHITE)
            screen.blit(text, (x + 50, y + 5))  # Ajustado para novo tamanho

    def get_item_at(self, pos):
        for i, item in enumerate(self.items):
            x, y = self.inventory_rect.left + 50, self.inventory_rect.top + 200 + i * 60
            if pygame.Rect(x, y, 300, 50).collidepoint(pos):
                return item
        return None