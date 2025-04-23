import pygame
import sys

pygame.init()
pygame.mixer.init()

# Tela
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Menu de Volume Estilizado")

# Fonte
fonte = pygame.font.SysFont("arial", 24, bold=True)

# Cores
COR_BG = (20, 20, 30)
COR_MENU = (30, 30, 45)
COR_SOMBRA = (0, 0, 0, 80)
COR_SLIDER_BG = (60, 60, 80)
COR_SLIDER_FILL = (0, 200, 255)
COR_SLIDER_FILL_BORDA = (0, 150, 200)
COR_CIRCULO = (0, 255, 180)
COR_TEXTO = (255, 255, 255)
COR_BORDA_MENU = (70, 130, 180)

# Música
pygame.mixer.music.load("54.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

# Efeito
try:
    efeito_som = pygame.mixer.Sound("passos.wav")
except FileNotFoundError:
    efeito_som = None

# Volumes
volume_musica = 0.5
volume_efeitos = 0.5
menu_ativo = False

def desenhar_slider(x, y, valor, texto):
    largura_slider = 300
    altura_slider = 12
    pos = int(x + largura_slider * valor)

    # Texto
    label = fonte.render(f"{texto}", True, COR_TEXTO)
    TELA.blit(label, (x, y - 40))

    # Fundo do slider
    pygame.draw.rect(TELA, COR_SLIDER_BG, (x, y, largura_slider, altura_slider), border_radius=10)

    # Volume
    pygame.draw.rect(TELA, COR_SLIDER_FILL_BORDA, (x, y, largura_slider * valor, altura_slider), border_radius=10)
    pygame.draw.rect(TELA, COR_SLIDER_FILL, (x + 2, y + 2, largura_slider * valor - 4, altura_slider - 4), border_radius=10)

    # Círculo
    pygame.draw.circle(TELA, COR_CIRCULO, (pos, y + altura_slider // 2), 10)

    return pygame.Rect(x, y, largura_slider, altura_slider), pygame.Rect(pos - 10, y - 5, 20, 20)

clock = pygame.time.Clock()
arrastando_musica = False
arrastando_efeito = False

# Loop principal
while True:
    TELA.fill(COR_BG)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                menu_ativo = not menu_ativo
            if evento.key == pygame.K_SPACE and efeito_som:
                efeito_som.play()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if menu_ativo:
                if slider_musica.collidepoint(evento.pos):
                    arrastando_musica = True
                if slider_efeito.collidepoint(evento.pos):
                    arrastando_efeito = True

        if evento.type == pygame.MOUSEBUTTONUP:
            arrastando_musica = False
            arrastando_efeito = False

        if evento.type == pygame.MOUSEMOTION:
            if arrastando_musica:
                rel_x = evento.pos[0] - slider_bg_musica.x
                volume_musica = max(0, min(1, rel_x / slider_bg_musica.width))
                pygame.mixer.music.set_volume(volume_musica)

            if arrastando_efeito and efeito_som:
                rel_x = evento.pos[0] - slider_bg_efeito.x
                volume_efeitos = max(0, min(1, rel_x / slider_bg_efeito.width))
                efeito_som.set_volume(volume_efeitos)

    if menu_ativo:
        menu_x, menu_y, menu_l, menu_a = 200, 150, 400, 300

        # Sombra
        sombra = pygame.Surface((menu_l, menu_a), pygame.SRCALPHA)
        pygame.draw.rect(sombra, COR_SOMBRA, (5, 5, menu_l, menu_a), border_radius=20)
        TELA.blit(sombra, (menu_x - 5, menu_y - 5))

        # Menu
        pygame.draw.rect(TELA, COR_MENU, (menu_x, menu_y, menu_l, menu_a), border_radius=20)
        pygame.draw.rect(TELA, COR_BORDA_MENU, (menu_x, menu_y, menu_l, menu_a), 2, border_radius=20)

        # Sliders
        slider_bg_musica, slider_musica = desenhar_slider(menu_x + 50, menu_y + 80, volume_musica, "Música")
        slider_bg_efeito, slider_efeito = desenhar_slider(menu_x + 50, menu_y + 170, volume_efeitos, "Efeitos")

    pygame.display.update()
    clock.tick(60)