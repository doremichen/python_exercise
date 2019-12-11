#! python3

import pygame
import os

_image_lib = {}
def get_image(path):
    global _image_lib
    image = _image_lib.get(path)
    if image == None:
        current_path = os.path.dirname(__file__)
        image = pygame.image.load(os.path.join(current_path, path))
        _image_lib[path] = image
    return image


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()
    x = 30
    y = 30
    done = False

    pygame.key.set_repeat(1, 1)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: y -= 13
                if event.key == pygame.K_DOWN: y += 13
                if event.key == pygame.K_LEFT: x -= 13
                if event.key == pygame.K_RIGHT: x += 13

            screen.fill((255, 255, 255))

            screen.blit(get_image('ball.png'), (x, y))
            pygame.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    main()
