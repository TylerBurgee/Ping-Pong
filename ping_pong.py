# IMPORT MODULES
import pygame as pg
import random

pg.mixer.init()
pg.font.init()

# DEFINE COLORS
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# ------ CREATE WINDOW CLASS ------
class Window (object):

    def __init__(self):
        # DEFINE SCREEN ATTRIBUTES
        self.running = False
        self.reset = False
        self.background = pg.image.load("baseball_field.png")
        self.WIDTH = 800
        self.HEIGHT = 600
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pg.time.Clock()
        self.FPS = 60
        self.matches = 0
        
        # DEFINE FONT ATTRIBUTES
        self.font = pg.font.SysFont("Comic Sans MS", 30)
        
        self.ball_hit = pg.mixer.Sound("baseball_hit.wav")
        pg.mixer.music.load("baseball_theme.ogg")
        pg.mixer.music.play(-1)

        self.winner = self.font.render("", False, WHITE)

    def START(self):

        # DEFINE PLAYER 1 ATTRIBUTES
        self.player1 = pg.image.load("bat.png")
        self.x1 = 5
        self.y1 = self.HEIGHT / 2
        self.y1v = 0
        self.player1_points = 0
        self.point_counter1 = self.font.render("Player 1: " + str(self.player1_points), False, WHITE)

        # DEFINE PLAYER 2 ATTRIBUTES
        self.player2 = pg.image.load("bat.png")
        self.x2 = 775
        self.y2 = self.HEIGHT / 2
        self.y2v = 0
        self.player2_points = 0
        self.point_counter2 = self.font.render("Player 2: " + str(self.player2_points), False, WHITE)

        # DEFINE BALL ATTRIBUTES
        self.ball = pg.image.load("baseball.png")
        self.bx = self.WIDTH / 2
        self.by = random.randint(15, 555)
        self.bxv = random.choice([6, -6])
        self.byv = random.choice([6, -6])

        self.matches = 0

        # SET BACKGROUND
        self.screen.blit(self.background, [0, 0])

        # INSTRUCTIONS
        self.start_text = self.font.render("Press Anywhere To Start Game", False, WHITE)
        self.screen.blit(self.start_text, [self.WIDTH / 2 - 200, self.HEIGHT / 2 - 45])
        self.screen.blit(self.winner, [self.WIDTH / 2 - 100, self.HEIGHT / 2 + 90])

        pg.display.update()

        # MAKE USER-CLICK START GAME
        button_pressed = False
        while button_pressed == False:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                        self.running = True
                        return 0

    def RESET(self):

        # DEFINE PLAYER 1 ATTRIBUTES
        self.player1 = pg.image.load("bat.png")
        self.x1 = 5
        self.y1 = self.HEIGHT / 2
        self.y1v = 0

        # DEFINE PLAYER 2 ATTRIBUTES
        self.player2 = pg.image.load("bat.png")
        self.x2 = 775
        self.y2 = self.HEIGHT / 2
        self.y2v = 0

        # DEFINE BALL ATTRIBUTES
        self.ball = pg.image.load("baseball.png")
        self.bx = self.WIDTH / 2
        self.by = random.randint(15, 555)
        self.bxv = random.choice([6, -6])
        self.byv = random.choice([6, -6])

        # SET BACKGROUND
        self.screen.blit(self.background, [0, 0])

        # INSTRUCTIONS
        self.start_text = self.font.render("Press Anywhere To Continue", False, WHITE)
        self.screen.blit(self.start_text, [self.WIDTH / 2 - 200, self.HEIGHT / 2 - 45])

        pg.display.update()

        # MAKE USER-CLICK START GAME
        button_pressed = False
        while button_pressed == False:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                        self.running = True
                        return 0

    # MAKE FUNCTION THAT INITIALIZES PYGAME WINDOW
    def start_window(self):
        pg.init()

    # MAKE FUNCTOIN THAT PROCESSES EVENTS
    def event_handling(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                        self.y1v = -8
                if event.key == pg.K_s:
                        self.y1v = 8
                if event.key == pg.K_UP:
                        self.y2v = -8
                if event.key == pg.K_DOWN:
                        self.y2v = 8

            if event.type == pg.KEYUP:
                if event.key == pg.K_w:
                    self.y1v = 0
                if event.key == pg.K_s:
                    self.y1v = 0
                if event.key == pg.K_UP:
                    self.y2v = 0
                if event.key == pg.K_DOWN:
                    self.y2v = 0

        # ADD VELOCITY TO PLAYER 1 POSITION
        self.y1 += self.y1v

        # ADD VELOCITY TO PLAYER 2 POSITION
        self.y2 += self.y2v

        # ADD VELOCITY TO BALL
        self.bx += self.bxv
        self.by += self.byv

    def collision(self):

        #  MAKE BALL BOUNCE OF Y-AXIS WALLS
        if (self.by > self.HEIGHT - 30):
            self.byv = -self.byv
        elif (self.by < 0):
            self.byv = -self.byv

        # MAKE BALL BOUNCE OFF PLAYER 1
        if (self.bx in range(20, 25) and self.by in range(int(self.y1) - 20, int(self.y1) + 65)):
            pg.mixer.Sound.play(self.ball_hit)
            self.bxv = -self.bxv

        # MAKE BALL BOUNCE OFF PLAYER 2
        if (self.bx in range(755, 780) and self.by in range(int(self.y2) - 20, int(self.y2) + 65)):
            pg.mixer.Sound.play(self.ball_hit)
            self.bxv = -self.bxv

        # MAKE BALL RESET WHEN IT GOES OFF-SCREEN
        if (self.bx > self.WIDTH):
            self.player1_points += 1
            self.point_counter1 = self.font.render("Player 1: " + str(self.player1_points), False, WHITE)
            self.running = False
        if (self.bx < 0):
            self.player2_points += 1
            self.point_counter2 = self.font.render("Player 2: " + str(self.player2_points), False, WHITE)
            self.running = False

        # MAKE BOUNDARIES FOR PLAYER 1
        if (self.y1 > self.HEIGHT - 45):
            self.y1 = self.HEIGHT - 47
        elif (self.y1 < 0):
            self.y1 = 2

        # MAKE BOUNDARIES FOR PLAYER 2
        if (self.y2 > self.HEIGHT - 45):
            self.y2 = self.HEIGHT - 47
        elif (self.y2 < 0):
            self.y2 = 2

    # MAKE FUNCTION THAT DRAWS OBJECTS TO SCREEN
    def draw(self):
        # BACKGROUND
        self.screen.blit(self.background, [0, 0])
        # PLAYER 1
        self.screen.blit(self.player1, [self.x1, self.y1])
        # PLAYER 2
        self.screen.blit(self.player2, [self.x2, self.y2])
        # BALL
        self.screen.blit(self.ball, [self.bx, self.by])

        self.screen.blit(self.point_counter1, [10, self.HEIGHT - 50])
        self.screen.blit(self.point_counter2, [600, self.HEIGHT - 50])

    # MAKE FUNCTION THAT RENDERS DRAWN OBJECTS TO SCREEN
    def render(self):
        pg.display.update()
        self.clock.tick(self.FPS)

Game = Window()

def START_SCREEN():
    if __name__ == '__main__':
        Game.start_window()
        Game.START()
        LOOP()

def RESET_SCREEN():
    Game.start_window()
    Game.RESET()
    LOOP()

def LOOP():
        while Game.running:
            Game.start_window()
            Game.event_handling()
            Game.collision()
            Game.draw()
            Game.render()
        Game.matches += 1
        if (Game.matches == 6):
            if (Game.player1_points > Game.player2_points):
                Game.winner = Game.font.render("Player 1 WINS!!!", False, WHITE)
            elif (Game.player2_points > Game.player1_points):
                Game.winner = Game.font.render("Player 2 WINS!!!", False, WHITE)
            elif (Game.player2_points == Game.player1_points):
                Game.winner = Game.font.render("Tie Game!!!", False, WHITE)
            START_SCREEN()
        RESET_SCREEN()
        
START_SCREEN()

