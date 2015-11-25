import pygame
import math

screen_width = 800
screen_height = 800
playing = True

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images/player.png')
        self.original = self.image
        self.rect = self.image.get_rect(center=location)
        self.angle = 0

    def get_angle(self, mouse):
        """
        Find the new angle between the center of the player and the mouse
        :param mouse:
        :return:
        """
        offset = (mouse[1]-self.rect.centery, mouse[0]-self.rect.centerx)
        self.angle = 135-math.degrees(math.atan2(*offset))
        # Rotate player by angle
        self.image = pygame.transform.rotate(self.original, self.angle)


class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode([screen_width, screen_height])

        self.all_sprites = pygame.sprite.Group()
        self.player = Player((400, 400))
        self.all_sprites.add(self.player)
        self.playing = True

        self.clock = pygame.time.Clock()

    def main(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

            if event.type == pygame.MOUSEMOTION:
                self.player.get_angle(event.pos)

        self.all_sprites.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    game = Main()

    while game.playing:
        game.clock.tick(120)
        game.main()
