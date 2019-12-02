import pygame, sys
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGRAY = (169, 169, 169)
YELLOW = (222, 178, 0)
PINK = (225, 96, 253)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
ORANGE = (255, 99, 71)
GRAY = (119, 136, 153)
LIGHTORANGE = (255, 176, 56)
INTERMEDIARYORANGE = (255, 154, 0)
LIGHTBLUE = (60, 170, 255)
DARKBLUE = (0, 101, 178)
BEIGE = (178, 168, 152)

WIDTH = 800
HEIGHT = WIDTH
SCREEN_SIZE = (WIDTH, HEIGHT)

RECT_QTT = 50

LEFT_CLICK = 1
SCROLL_CLICK = 4
RIGHT_CLICK = 3

class Game():

    def __init__(self):
        try:
            pygame.init()
        except:
            print('The pygame module did not start successfully')

        self.background = pygame.display.set_mode(SCREEN_SIZE)

        pygame.mouse.set_cursor(*pygame.cursors.broken_x)
        pygame.display.set_caption("Paint")

        self.option_draw = False
        self.brush_color = GREEN
        self.brush_size = WIDTH // RECT_QTT

    def run(self):
        exit = False

        while not exit:
            self.mouse_position = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit = True

                elif event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                    if event.key == K_TAB:
                        self.option_draw = not self.option_draw

                    # Change pencil color
                    elif event.key == K_r:
                        self.brush_color = RED

                    elif event.key == K_b:
                        self.brush_color = BLUE

                    elif event.key == K_o:
                        self.brush_color = ORANGE

                    elif event.key == K_g:
                        self.brush_color = GREEN

                    elif event.key == K_y:
                        self.brush_color = YELLOW
                    # eraser
                    elif event.key == K_e:
                        self.brush_color = BLACK


                elif event.type == MOUSEBUTTONDOWN:

                    if(event.button == RIGHT_CLICK):
                        # fill using bfs algorithm
                        print("Running BFS")
                        self.option_draw = False
                        if self.background.get_at(self.mouse_position) != self.brush_color:
                            self.bfs(self.mouse_position, self.background.get_at(self.mouse_position))
                        print("End BFS")

                    elif(event.button == LEFT_CLICK):
                        # fill using dfs algorithm
                        # brush min size = 20 (because recursion qtt)
                        print("Running DFS")
                        self.option_draw = False
                        if self.background.get_at(self.mouse_position) != self.brush_color:
                            self.dfs(self.mouse_position, self.background.get_at(self.mouse_position))
                        print("End DFS")

                # Drawing dot when mousebuttondown
                if self.option_draw:
                    self.draw_rect_in_position(self.mouse_position)

            pygame.display.update()

        pygame.quit()
        sys.exit(0)

    def bfs(self, s, color):
        queue = []
        neighbors = []

        self.draw_rect_in_position(s)
        queue.append(s)

        while queue:

            neighbors.clear()

            s = queue.pop()
            x, y = s

            # neighbors.append((x + self.brush_size + 1, y + self.brush_size + 1))
            # neighbors.append((x - self.brush_size - 1, y + self.brush_size + 1))
            # neighbors.append((x + self.brush_size + 1, y - self.brush_size - 1))
            # neighbors.append((x - self.brush_size - 1, y - self.brush_size - 1))
            neighbors.append((x + self.brush_size, y))
            neighbors.append((x - self.brush_size, y))
            neighbors.append((x, y - self.brush_size))
            neighbors.append((x, y + self.brush_size))

            for neighbor in neighbors:
                if self.verifyMargin(neighbor) and self.getColor(neighbor) == color:
                    queue.append(neighbor)
                    self.draw_rect_in_position(neighbor)

    def dfs(self, s, color):

        if self.getColor(s) == color:
            stack = []
            neighbors = []
            stack.append(s)

            while (stack):
                node = stack.pop()
                x, y = node

                neighbors.clear()
                # neighbors.append((x + self.brush_size + 1, y + self.brush_size + 1))
                # neighbors.append((x - self.brush_size, y + self.brush_size + 1))
                # neighbors.append((x + self.brush_size + 1, y - self.brush_size))
                # neighbors.append((x - self.brush_size, y - self.brush_size))
                neighbors.append((x + self.brush_size, y))
                neighbors.append((x - self.brush_size, y))
                neighbors.append((x, y - self.brush_size))
                neighbors.append((x, y + self.brush_size))

                self.draw_rect_in_position(node)

                for neighbor in neighbors:
                    if self.verifyMargin(neighbor) and self.getColor(neighbor) == color and neighbor:
                        stack.append(neighbor)


    def draw_rect_in_position(self, s):
        x, y = s

        position_x = self.brush_size * (x // self.brush_size)
        position_y = self.brush_size * (y // self.brush_size)

        rect = pygame.Rect(position_x, position_y, self.brush_size, self.brush_size)
        pygame.draw.rect(self.background, self.brush_color, rect)

    def getColor(self, position):
        x, y = position
        return self.background.get_at((x, y))

    def verifyMargin(self, s):
        x, y = s
        return x >= 0 and x < WIDTH and y >= 0 and y < HEIGHT


def main():
    mygame = Game()
    mygame.run()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interruption')
