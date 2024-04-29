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
        self._screen_width = width
        self._screen_height = height
        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))
        pygame.display.set_caption(title)
        self._font = pygame.font.SysFont(None, 40)

    @abstractmethod
    def handle_events(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def get_screen_width(self):
        return self._screen_width

    def get_screen_height(self):
        return self._screen_height

    def set_screen_width(self, width):
        self._screen_width = width
        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))

    def set_screen_height(self, height):
        self._screen_height = height
        self._screen = pygame.display.set_mode((self._screen_width, self._screen_height))

class TicTacToe(Game):
    def __init__(self):
        super().__init__(300, 300, 'Tic Tac Toe by Aditoya')
        self._line_width = 6
        self._red = (255, 0, 0)
        self._green = (0, 255, 0)
        self._blue = (0, 0, 255)
        self._clicked = False
        self._player = 1
        self._pos = (0, 0)
        self._markers = [[0]*3 for _ in range(3)]
        self._game_over = False
        self._winner = 0
        self._again_rect = Rect(self.get_screen_width() // 2 - 80, self.get_screen_height() // 2, 160, 50)

    def get_player(self):
        return self._player

    def set_player(self, player):
        self._player = player

    def get_markers(self):
        return self._markers

    def set_markers(self, markers):
        self._markers = markers

    def get_game_over(self):
        return self._game_over

    def set_game_over(self, game_over):
        self._game_over = game_over

    def get_winner(self):
        return self._winner

    def set_winner(self, winner):
        self._winner = winner

    def draw_board(self):
        bg = (255, 255, 210)
        grid = (50, 50, 50)
        self._screen.fill(bg)
        for x in range(1,3):
            pygame.draw.line(self._screen, grid, (0, 100 * x), (self.get_screen_width(),100 * x), self._line_width)
            pygame.draw.line(self._screen, grid, (100 * x, 0), (100 * x, self.get_screen_height()), self._line_width)

    def draw_markers(self):
        for x_pos, row in enumerate(self.get_markers()):
            for y_pos, marker in enumerate(row):
                if marker == 1:
                    pygame.draw.line(self._screen, self._red, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), self._line_width)
                    pygame.draw.line(self._screen, self._red, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), self._line_width)
                elif marker == -1:
                    pygame.draw.circle(self._screen, self._green, (x_pos * 100 + 50, y_pos * 100 + 50), 38, self._line_width)

    def check_game_over(self):
        for x_pos in range(3):
            if sum(self.get_markers()[x_pos]) == 3 or self.get_markers()[0][x_pos] + self.get_markers()[1][x_pos] + self.get_markers()[2][x_pos] == 3:
                self.set_winner(1)
                self.set_game_over(True)
            elif sum(self.get_markers()[x_pos]) == -3 or self.get_markers()[0][x_pos] + self.get_markers()[1][x_pos] + self.get_markers()[2][x_pos] == -3:
                self.set_winner(2)
                self.set_game_over(True)

        if self.get_markers()[0][0] + self.get_markers()[1][1] + self.get_markers()[2][2] == 3 or self.get_markers()[2][0] + self.get_markers()[1][1] + self.get_markers()[0][2] == 3:
            self.set_winner(1)
            self.set_game_over(True)
        elif self.get_markers()[0][0] + self.get_markers()[1][1] + self.get_markers()[2][2] == -3 or self.get_markers()[2][0] + self.get_markers()[1][1] + self.get_markers()[0][2] == -3:
            self.set_winner(2)
            self.set_game_over(True)

        if not self.get_game_over():
            tie = all(i != 0 for row in self.get_markers() for i in row)
            if tie:
                self.set_game_over(True)
                self.set_winner(0)

    def draw_game_over(self):
        if self.get_winner() != 0:
            end_text = " Player " + str(self.get_winner()) + " win!"
        elif self.get_winner() == 0:
            end_text = "Kamu Kalah!"

        end_img = self._font.render(end_text, True, self._blue)
        pygame.draw.rect(self._screen, self._green, (self.get_screen_width() // 2 - 100, self.get_screen_height() // 2 - 60, 200, 50))
        self._screen.blit(end_img, (self.get_screen_width() // 2 - 100, self.get_screen_height() // 2 - 50))

        again_text = 'Main lagi?'
        again_img = self._font.render(again_text, True, self._blue)
        pygame.draw.rect(self._screen, self._green, self._again_rect)
        self._screen.blit(again_img, (self.get_screen_width() // 2 - 80, self.get_screen_height() // 2 + 10))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if self.get_game_over() == False:
                if event.type == pygame.MOUSEBUTTONDOWN and self._clicked == False:
                    self._clicked = True
                if event.type== pygame.MOUSEBUTTONUP and self._clicked == True:
                    self._clicked = False
                    self._pos = pygame.mouse.get_pos()
                    cell_x = self._pos[0] // 100
                    cell_y = self._pos[1] // 100
                    if self._markers[cell_x][cell_y] == 0:
                        self._markers[cell_x][cell_y] = self._player
                        self._player *= -1
                        self.check_game_over()
        return True

    def run(self):
        run = True
        while run:
            self.draw_board()
            self.draw_markers()
            run = self.handle_events()

            if self.get_game_over():
                self.draw_game_over()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and self._clicked == False:
                        self._clicked = True
                    if event.type == pygame.MOUSEBUTTONUP and self._clicked == True:
                        self._clicked = False
                        pos = pygame.mouse.get_pos()
                        if self._again_rect.collidepoint(pos):
                            self.set_game_over(False)
                            self.set_player(1)
                            self._pos = (0, 0)
                            self.set_markers([[0]*3 for _ in range(3)])
                            self.set_winner(0)

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
