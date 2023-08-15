import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
RECT_COLOR = (0, 0, 0)
RECT_WIDTH = 10
MAX_RECT_HEIGHT = 400
NUM_RECTANGLES = WIDTH // RECT_WIDTH

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Selection Sort Visualization")

class RectangleSorter:
    def __init__(self):
        self.rect_heights = [random.randint(10, MAX_RECT_HEIGHT) for _ in range(NUM_RECTANGLES)]
        self.sorted = False
        self.clock = pygame.time.Clock()

    def draw_rectangles(self):
        for i, height in enumerate(self.rect_heights):
            rect = pygame.Rect(i * RECT_WIDTH, HEIGHT - height, RECT_WIDTH, height)
            pygame.draw.rect(screen, RECT_COLOR, rect)

    def selection_sort(self):
        for i in range(len(self.rect_heights)):
            min_idx = i
            for j in range(i + 1, len(self.rect_heights)):
                if self.rect_heights[j] < self.rect_heights[min_idx]:
                    min_idx = j

            self.rect_heights[i], self.rect_heights[min_idx] = self.rect_heights[min_idx], self.rect_heights[i]

            screen.fill(BACKGROUND_COLOR)
            self.draw_rectangles()
            pygame.display.flip()
            pygame.time.wait(50)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if not self.sorted:
                self.selection_sort()
                self.sorted = True

            screen.fill(BACKGROUND_COLOR)
            self.draw_rectangles()
            pygame.display.flip()
            self.clock.tick(30)

if __name__ == "__main__":
    sorter = RectangleSorter()
    sorter.run()
