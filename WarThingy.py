import pygame
import math

screen_width = 800
screen_height = 800
playing = True

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        # player picture is 48 * 56 pixels
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

        self.player.get_angle(pygame.mouse.get_pos())

        key = pygame.key.get_pressed()
        if (key[pygame.K_LEFT] or key[pygame.K_a]):
            if ( 0 < self.player.rect.x ):
                self.player.rect.centerx -= 5
        if (key[pygame.K_RIGHT] or key[pygame.K_d]):
            if ( screen_width > self.player.rect.x + + self.player.image.get_rect().size[0]):
                self.player.rect.centerx += 5
        if (key[pygame.K_UP] or key[pygame.K_w]):
            if (0 < self.player.rect.y ):
                self.player.rect.centery -= 5
        if (key[pygame.K_DOWN] or key[pygame.K_s]):
            if ( screen_height > self.player.rect.y + self.player.image.get_rect().size[1]):
                self.player.rect.centery += 5
        #print self.player.image.get_rect().size
        self.all_sprites.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    game = Main()
    all_sprites = pygame.sprite.Group()
    while game.playing:
        game.clock.tick(60)
        game.main()
