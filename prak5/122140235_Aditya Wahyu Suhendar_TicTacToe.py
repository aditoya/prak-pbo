"""
Aditya Wahyu Suhendar
122140235
Praktikum PBO RB (Asal kelas RC)
Membuat Game Tic Tac Toe
"""

import pygame
from pygame.locals import *
from abc import ABC, abstractmethod

class Game(ABC):
    def __init__(self, width, height, title):
        pygame.init()
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(title)
        self.font = pygame.font.SysFont(None, 40)

    @abstractmethod
    def handle_events(self):
        pass

    @abstractmethod
    def run(self):
        pass

class TicTacToe(Game):
    def __init__(self):
        super().__init__(300, 300, 'Tic Tac Toe by Aditoya')
        self.line_width = 6
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.clicked = False
        self.player = 1
        self.pos = (0, 0)
        self.markers = [[0]*3 for _ in range(3)]
        self.game_over = False
        self.winner = 0
        self.again_rect = Rect(self.screen_width // 2 - 80, self.screen_height // 2, 160, 50)

    def draw_board(self):
        bg = (255, 255, 210)
        grid = (50, 50, 50)
        self.screen.fill(bg)
        for x in range(1,3):
            pygame.draw.line(self.screen, grid, (0, 100 * x), (self.screen_width,100 * x), self.line_width)
            pygame.draw.line(self.screen, grid, (100 * x, 0), (100 * x, self.screen_height), self.line_width)

    def draw_markers(self):
        for x_pos, row in enumerate(self.markers):
            for y_pos, marker in enumerate(row):
                if marker == 1:
                    pygame.draw.line(self.screen, self.red, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), self.line_width)
                    pygame.draw.line(self.screen, self.red, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), self.line_width)
                elif marker == -1:
                    pygame.draw.circle(self.screen, self.green, (x_pos * 100 + 50, y_pos * 100 + 50), 38, self.line_width)

    def check_game_over(self):
        for x_pos in range(3):
            if sum(self.markers[x_pos]) == 3 or self.markers[0][x_pos] + self.markers[1][x_pos] + self.markers[2][x_pos] == 3:
                self.winner = 1
                self.game_over = True
            elif sum(self.markers[x_pos]) == -3 or self.markers[0][x_pos] + self.markers[1][x_pos] + self.markers[2][x_pos] == -3:
                self.winner = 2
                self.game_over = True

        if self.markers[0][0] + self.markers[1][1] + self.markers[2][2] == 3 or self.markers[2][0] + self.markers[1][1] + self.markers[0][2] == 3:
            self.winner = 1
            self.game_over = True
        elif self.markers[0][0] + self.markers[1][1] + self.markers[2][2] == -3 or self.markers[2][0] + self.markers[1][1] + self.markers[0][2] == -3:
            self.winner = 2
            self.game_over = True

        if not self.game_over:
            tie = all(i != 0 for row in self.markers for i in row)
            if tie:
                self.game_over = True
                self.winner = 0

    def draw_game_over(self):
        if self.winner != 0:
            end_text = " Player " + str(self.winner) + " win!"
        elif self.winner == 0:
            end_text = "Kamu Kalah!"

        end_img = self.font.render(end_text, True, self.blue)
        pygame.draw.rect(self.screen, self.green, (self.screen_width // 2 - 100, self.screen_height // 2 - 60, 200, 50))
        self.screen.blit(end_img, (self.screen_width // 2 - 100, self.screen_height // 2 - 50))

        again_text = 'Main lagi?'
        again_img = self.font.render(again_text, True, self.blue)
        pygame.draw.rect(self.screen, self.green, self.again_rect)
        self.screen.blit(again_img, (self.screen_width // 2 - 80, self.screen_height // 2 + 10))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if self.game_over == False:
                if event.type == pygame.MOUSEBUTTONDOWN and self.clicked == False:
                    self.clicked = True
                if event.type == pygame.MOUSEBUTTONUP and self.clicked == True:
                    self.clicked = False
                    self.pos = pygame.mouse.get_pos()
                    cell_x = self.pos[0] // 100
                    cell_y = self.pos[1] // 100
                    if self.markers[cell_x][cell_y] == 0:
                        self.markers[cell_x][cell_y] = self.player
                        self.player *= -1
                        self.check_game_over()
        return True

    def run(self):
        run = True
        while run:
            self.draw_board()
            self.draw_markers()
            run = self.handle_events()

            if self.game_over:
                self.draw_game_over()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and self.clicked == False:
                        self.clicked = True
                    if event.type == pygame.MOUSEBUTTONUP and self.clicked == True:
                        self.clicked = False
                        pos = pygame.mouse.get_pos()
                        if self.again_rect.collidepoint(pos):
                            self.game_over = False
                            self.player = 1
                            self.pos = (0, 0)
                            self.markers = [[0]*3 for _ in range(3)]
                            self.winner = 0

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()