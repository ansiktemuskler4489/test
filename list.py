import pygame
import random


class game:
    def __init__(self):
        
        self.x = 10
        self.y = 100
        self.listNums = [79, 100, 44, 41, 30, 57, 95, 1, 86, 11]
        self.cell_sizeY = int(800/len(self.listNums))
        self.offset = 20


    def make_list(self):
        tempList = []
        sizeList = random.randint(5, self.x)
        for i in range(sizeList):
            randomNum = random.randint(0, self.y)
            tempList.append(randomNum)
        return tempList

    def drawList(self, screen):
        for i in range(len(self.listNums)):
            cell_rect = pygame.Rect(20, i * self.cell_sizeY + 20, self.listNums[i]*4, 50)
            pygame.draw.rect(screen, (255, 0, 0), cell_rect)

    def bubblesort(self):
        change = 0
        # while change != len(self.listNums)-1:
        for y in range(1000):
            for i in range(len(self.listNums)-1):
                if self.listNums[i] <= self.listNums[i+1]:
                    temp = self.listNums[i]
                    self.listNums[i] = self.listNums[i+1] 
                    self.listNums[i+1] = temp
                else:
                    print("hej")