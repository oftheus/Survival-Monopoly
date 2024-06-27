import pygame

class DisplayLog(pygame.sprite.Sprite):
    
    _instance = None #Singleton

    @classmethod 
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def init(self, screen, font):
        self.screen = screen
        self.lastLog = None
        self.pos = (400,480)
        self.fonte = font
        
    def addToLog(self, logEntry):
        self.lastLog = logEntry
        #self.displayLog()

    def removeFromLog(self):
        self.lastLog = None
        #self.displayLog()

    def displayLog(self):
        if not self.lastLog == None:
            logText = self.fonte.render(
                    self.lastLog, True, (255, 255, 255))
            self.screen.blit(logText, self.pos)
            #pygame.display.update()
        else:
            logText = self.fonte.render(
                    "", True, (255, 255, 255))
            self.screen.blit(logText, self.pos)
            #pygame.display.update()