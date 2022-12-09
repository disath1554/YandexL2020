import pygame
from math import sin, cos, radians

WIDTH, HEIGHT = 301, 301
def fan(screen, angle=60):
    r = 100
    cx, cy = WIDTH // 2, HEIGHT // 2
    for a in [angle, angle + 120, angle + 240]:
        pygame.draw.polygon(screen, "orange",
                            ((cx, cy),
                             (int(r * sin(radians(a - 10))) + cx,
                              int(r * cos(radians(a - 10))) + cy),
                             (int(r * sin(radians(a + 10))) + cx,
                              int(r * cos(radians(a + 10))) + cy)),0)
    pygame.draw.circle(screen, "orange", (cx, cy), 20, 0)
        


def main():
    pygame.init()
    pygame.display.set_caption('Вентилятор')
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    angle = 60
    speed = 0
    fan(screen)
    pygame.display.flip()
    
    while running:
    # красим фон
        screen.fill(pygame.Color('black'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # реакция на нажатие мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = pygame.mouse.get_pressed()
                # изменяем скорость в нужную сторону
                if event.button == 3:
                    speed += 2 / 180
                elif event.button == 1:
                    speed -= 2 / 180
        # смещаем лопасти
        angle += speed
        fan(screen, angle)
        pygame.display.flip()
    clock.tick(50)
    pygame.quit()

if __name__ == '__main__':
    main()
