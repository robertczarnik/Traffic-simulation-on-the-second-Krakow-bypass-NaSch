import pygame, sys


class GraphicalView(object):

    def __init__(self):
        # initialization
        #7423 x 9439
        self.width = 7423
        self.height = 9439
        self.row = 22
        self.col = 55
        self.heightStep = self.height / (self.row-1)
        self.widthStep = self.width / (self.col-1)
        self.heightStart = -self.heightStep
        self.widthStart = -self.widthStep
        self.firstCrossMap = {}
        self.roadMap = {}
        self.screen = pygame.display.set_mode((self.width, self.height))
        while True:
            # Handle events
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    sys.exit(0)
            bypassImage=pygame.image.load("obwodnica.jpg")
            #bypassImage=pygame.transform.scale(bypassImage,(825,1049))
            #bypassImage=pygame.transform.scale(bypassImage,(7423,9439))
            self.screen.blit(bypassImage,(0,0))
            self.draw()
            pygame.display.flip()

    # map for crossing no.1
    def makeMap1(self):
        pass

    def draw(self):
        self.makeMap1()
        # wszystkie punkty
        for c in range(24):
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(530+8*c, 375-5.9*c, 1, 1))

    """"
    def draw(self):
        self.makeMap1()
        #wszystkie punkty
        for r in range(self.row):
            for c in range(self.col):
                (x, y) = self.roadMap[r, c]
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x, y, 3, 3))"""""





"""""
    def makeMap(self):
        for r in range(self.row):
            self.heightStart += self.heightStep
            self.widthStart = -self.widthStep
            for c in range(self.col):
                self.widthStart += self.widthStep
                self.roadMap[r, c] = (self.widthStart, self.heightStart)
"""""







#skrzyżowanie
"""""
#poziome
pygame.draw.line(self.screen, (255,255,255),self.roadMap[5,0],self.roadMap[5,23], 2)
pygame.draw.line(self.screen, (255,255,255),self.roadMap[5,26],self.roadMap[5,54], 2)
pygame.draw.line(self.screen, (255, 255, 255), self.roadMap[9, 0], self.roadMap[9, 23], 2)
pygame.draw.line(self.screen, (255, 255, 255), self.roadMap[9, 26], self.roadMap[9, 54], 2)
pygame.draw.line(self.screen, (255, 255, 255), self.roadMap[12, 0], self.roadMap[12, 23], 2)
pygame.draw.line(self.screen, (255, 255, 255), self.roadMap[12, 26], self.roadMap[12, 54], 2)
pygame.draw.line(self.screen, (255, 255, 255), self.roadMap[16, 0], self.roadMap[16, 23], 2)
pygame.draw.line(self.screen, (255, 255, 255), self.roadMap[16, 26], self.roadMap[16, 54], 2)

#pionowe
pygame.draw.line(self.screen, (255, 255, 255), self.roadMap[0, 23], self.roadMap[5, 23], 2)
pygame.draw.line(self.screen, (255, 255, 255), self.roadMap[0, 26], self.roadMap[5, 26], 2)
pygame.draw.line(self.screen, (255, 255, 255), self.roadMap[9, 23], self.roadMap[12, 23], 2)
pygame.draw.line(self.screen, (255, 255, 255), self.roadMap[9, 26], self.roadMap[12, 26], 2)
pygame.draw.line(self.screen, (255, 255, 255), self.roadMap[16, 23], self.roadMap[21, 23], 2)
pygame.draw.line(self.screen, (255, 255, 255), self.roadMap[16, 26], self.roadMap[21, 26], 2)
"""""