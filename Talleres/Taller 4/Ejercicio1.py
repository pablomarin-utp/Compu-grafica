import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
WHITE = (255, 255, 255)
screen.fill(WHITE)

for x in range(0, 500, 100):
    pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, 500))
for y in range(0, 500, 100):
    pygame.draw.line(screen, (200, 200, 200), (0, y), (500, y))

pygame.draw.line(screen, (255, 0, 0), (50, 50), (450, 50), 5)
pygame.draw.line(screen, (0, 255, 0), (50, 100), (450, 100), 10)
pygame.draw.line(screen, (0, 0, 255), (50, 150), (450, 150), 2)

pygame.image.save(screen, "e1_lineas.png")
pygame.quit()
