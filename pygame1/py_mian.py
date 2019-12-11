#! python3

import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    # draw rect
    is_blue = False
    X = 30
    Y = 30

    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_blue = not is_blue

        # press
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: Y -= 3
        if pressed[pygame.K_DOWN]: Y += 3
        if pressed[pygame.K_LEFT]: X -= 3
        if pressed[pygame.K_RIGHT]: X += 3

        # refresh
        screen.fill((0, 0, 0))
        color = (0, 128, 255) if is_blue else (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(X, Y, 60, 60))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
