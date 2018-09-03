import pygame
import os

pygame.init()

clock = pygame.time.Clock()


class Player():
    walkRight = [pygame.image.load(os.path.join('SideScrollSprites', 'R1.png')),
                 pygame.image.load(os.path.join('SideScrollSprites', 'R2.png')),
                 pygame.image.load(os.path.join('SideScrollSprites', 'R3.png')),
                 pygame.image.load(os.path.join('SideScrollSprites', 'R4.png')),
                 pygame.image.load(os.path.join('SideScrollSprites', 'R5.png')),
                 pygame.image.load(os.path.join('SideScrollSprites', 'R6.png')),
                 pygame.image.load(os.path.join('SideScrollSprites', 'R7.png')),
                 pygame.image.load(os.path.join('SideScrollSprites', 'R8.png')),
                 pygame.image.load(os.path.join('SideScrollSprites', 'R9.png'))]
    walkLeft = [pygame.image.load(os.path.join('SideScrollSprites', 'L1.png')),
                pygame.image.load(os.path.join('SideScrollSprites', 'L2.png')),
                pygame.image.load(os.path.join('SideScrollSprites', 'L3.png')),
                pygame.image.load(os.path.join('SideScrollSprites', 'L4.png')),
                pygame.image.load(os.path.join('SideScrollSprites', 'L5.png')),
                pygame.image.load(os.path.join('SideScrollSprites', 'L6.png')),
                pygame.image.load(os.path.join('SideScrollSprites', 'L7.png')),
                pygame.image.load(os.path.join('SideScrollSprites', 'L8.png')),
                pygame.image.load(os.path.join('SideScrollSprites', 'L9.png'))]
    char = pygame.image.load(os.path.join('SideScrollSprites', 'standing.png'))

    def __init__(self, x, y, width, height, win):
        self.win = win
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.framerate = 27

        self.isJump = False
        self.permJumpCount = 10
        self.jumpCount = self.permJumpCount

        self.left = False
        self.right = False
        self.walkCount = 0

    def move(self, keys):
        (screenWidth, screenHeight) = self.win.get_size()
        if keys[pygame.K_LSHIFT]:
            self.vel = 10
        else:
            self.vel = 5
        if keys[pygame.K_a] and self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False
        elif keys[pygame.K_d] and self.x < screenWidth - self.width - self.vel:
            self.x += self.vel
            self.right = True
            self.left = False
        else:
            self.right = False
            self.left = False
            self.walkCount = 0

        if not self.isJump:
            if keys[pygame.K_w]:
                self.isJump = True

        else:
            if self.jumpCount >= -self.permJumpCount:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = self.permJumpCount

    def draw(self):
        if self.walkCount + 1 >= self.framerate:
            self.walkCount = 0
        if self.left:
            self.win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            self.win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            self.win.blit(self.char, (self.x, self.y))


class Enemy():
    walkRight = [pygame.image.load(os.path.join('SideScrollSprites', 'R1E.png')),
                 pygame.image.load(os.path.join('SideScrollSprites', 'R2E.png')),
                 pygame.image.load(os.path.join('SideScrollSprites', 'R3E.png')),
                 pygame.image.load(os.path.join('SideScrollSprites', 'R4E.png')),
                 pygame.image.load(os.path.join('SideScrollSprites', 'R5E.png')),
                 pygame.image.load(os.path.join('SideScrollSprites', 'R6E.png')),
                 pygame.image.load(os.path.join('SideScrollSprites', 'R7E.png')),
                 pygame.image.load(os.path.join('SideScrollSprites', 'R8E.png'))]
    punchRight = [pygame.image.load(os.path.join('SideScrollSprites', 'R9E.png')),
                  pygame.image.load(os.path.join('SideScrollSprites', 'R10E.png')),
                  pygame.image.load(os.path.join('SideScrollSprites', 'R11E.png'))]
    walkLeft = [pygame.image.load(os.path.join('SideScrollSprites', 'L1E.png')),
                pygame.image.load(os.path.join('SideScrollSprites', 'L2E.png')),
                pygame.image.load(os.path.join('SideScrollSprites', 'L3E.png')),
                pygame.image.load(os.path.join('SideScrollSprites', 'L4E.png')),
                pygame.image.load(os.path.join('SideScrollSprites', 'L5E.png')),
                pygame.image.load(os.path.join('SideScrollSprites', 'L6E.png')),
                pygame.image.load(os.path.join('SideScrollSprites', 'L7E.png')),
                pygame.image.load(os.path.join('SideScrollSprites', 'L8E.png'))]
    punchLeft = [pygame.image.load(os.path.join('SideScrollSprites', 'L9E.png')),
                 pygame.image.load(os.path.join('SideScrollSprites', 'L10E.png')),
                 pygame.image.load(os.path.join('SideScrollSprites', 'L11E.png'))]

    def __init__(self, x, y, width, height, win):
        self.win = win
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 3
        self.health = 10
        self.framerate = 25
        self.left = False
        self.right = False
        self.punch = False
        self.punchCount = 22
        self.walking = True

    def draw(self):
        if self.walkCount + 1 >= self.framerate:
            self.x += 9
            self.walkCount = 0
        if self.punchCount <= 0:
            self.punchCount = 22
        if self.walking:
            if self.left:
                self.win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                self.win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        elif self.punch:
            self.walkCount = 0
            if self.right:
                self.win.blit(self.punchRight[self.punchCount // 9], (self.x, self.y))
                self.punchCount -= 1
            elif self.left:
                self.win.blit(self.punchLeft[self.punchCount // 9], (self.x, self.y))
                self.punchCount -= 1


class App():
    bg = pygame.image.load(os.path.join('SideScrollSprites', 'pixel_background.png'))
    def __init__(self):
        # self.screenWidth = 1000
        # self.screenHeight = 500
        self.win = pygame.display.set_mode((1000, 500))
        # (screenWidth,screenHeight) = self.win.get_size()
        # print("{0}, {1}".format(screenWidth,screenHeight))
        self.man = Player(300, 400, 64, 64, self.win)
        self.goblin = Enemy(500, 405, 64, 64, self.win)

        pygame.display.set_caption("First Game")

    def goblinMove(self):

        if 0 <= self.goblin.x - self.man.x <= 30 or 0 <= self.man.x - self.goblin.x <= 30:
            self.goblin.walking = False
            self.goblin.punch = True
        else:
            if self.goblin.x > self.man.x:
                self.goblin.walking = True
                self.goblin.punch = False
                self.goblin.x -= self.goblin.vel
                self.goblin.right = False
                self.goblin.left = True
            elif self.goblin.x < self.man.x:
                self.goblin.walking = True
                self.goblin.punch = False
                self.goblin.x += self.goblin.vel
                self.goblin.right = True
                self.goblin.left = False


    def redrawGameWindow(self):
        self.win.blit(self.bg, (0, 0))
        self.man.draw()
        self.goblin.draw()
        pygame.display.update()

    def mainLoop(self):
        run = True
        while run: # endless loop of the game
            clock.tick(self.man.framerate)

            # capture quit event here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # capture the key pressed here and act accordingly
            keys = pygame.key.get_pressed()
            self.man.move(keys)
            App.goblinMove(self)
            App.redrawGameWindow(self)

        pygame.quit()

if __name__ == '__main__':
    Game = App()
    Game.mainLoop()
