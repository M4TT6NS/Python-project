import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set.mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Game")

def main():
  run = True

  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        break

  pygame.quit()

if __name__ == "__main__":
  main()
