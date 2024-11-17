from random import randrange

import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_position_x = 0
        mole_position_y = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_x = event.pos[0]
                    click_y = event.pos[1]
                    if (click_x > mole_position_x and click_x < mole_position_x + 32) and (click_y > mole_position_y and click_y < mole_position_y + 32):
                        mole_position_x = random.randrange(0, 20) * 32
                        mole_position_y = random.randrange(0, 16) * 32
            screen.fill((255, 253, 208))
            for i in range (32):
                pygame.draw.line(screen, "black", (32 * i, 0), (32 * i, 512))
            for i in range (32):
                pygame.draw.line(screen, "black", (0, 32 * i), (640, 32 * i))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_position_x, mole_position_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()


