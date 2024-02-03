import pygame, sys
from list import game

#not done


class bubble:
    def __init__(self):
        pygame.init()
        self.game1 = game()
        self.screen = pygame.display.set_mode((440, 800))
        pygame.display.set_caption("bubblesort sim")
        self.clock = pygame.time.Clock()

        self.game_active = 1
    def gameLoop(self):
        while True:
            if self.game_active == 1:
                self.game1.drawList(self.screen)
                self.game1.bubblesort()
                pygame.time.delay(1000)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()
            self.clock.tick(30)

game2 = bubble()
game2.gameLoop()

