import pygame
import sys
from ButtonforMenu import Button
import BlackJack as bj
import main as l
import tkinter
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("imagesMenu/background.png")
def get_font(size):  # Returns Press-Start-2P in the desired size
  return pygame.font.Font("imagesMenu/font.ttf", size)


def Rules():
  while True:
    RULES_MOUSE_POS = pygame.mouse.get_pos()
    SCREEN = pygame.display.set_mode((1280, 720))
    RULES_IMAGE = pygame.image.load("rules.png")
    SCREEN.blit(RULES_IMAGE, (0, 0))
    

    RULES_BACK = Button(image=None,
                          pos=(200, 65),
                          text_input="BACK",
                          font=get_font(40),
                          base_color="RED",
                          hovering_color="Green")

    RULES_BACK.changeColor(RULES_MOUSE_POS)
    RULES_BACK.update(SCREEN)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if RULES_BACK.checkForInput(RULES_MOUSE_POS):
          main_menu()

    pygame.display.update()


def main_menu():
  while True:
    SCREEN.blit(BG, (0, 0))

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

    LOGIN_BUTTON = Button(image=pygame.image.load("imagesMenu/LoginRect.png"),
                         pos=(640, 250),
                         text_input="Login",
                         font=get_font(75),
                         base_color="#d7fcd4",
                         hovering_color="White")
    RULES_BUTTON = Button(image=pygame.image.load("imagesMenu/RulesRect.png"),
                            pos=(640, 400),
                            text_input="RULES",
                            font=get_font(75),
                            base_color="#d7fcd4",
                            hovering_color="White")
    QUIT_BUTTON = Button(image=pygame.image.load("imagesMenu/QuitRect.png"),
                         pos=(640, 550),
                         text_input="QUIT",
                         font=get_font(75),
                         base_color="#d7fcd4",
                         hovering_color="White")

    SCREEN.blit(MENU_TEXT, MENU_RECT)

    for button in [LOGIN_BUTTON, RULES_BUTTON, QUIT_BUTTON]:
      button.changeColor(MENU_MOUSE_POS)
      button.update(SCREEN)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if LOGIN_BUTTON.checkForInput(MENU_MOUSE_POS):
          l.main_login()
        if RULES_BUTTON.checkForInput(MENU_MOUSE_POS):
          Rules()
        if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
          pygame.quit()
          sys.exit()

    pygame.display.update()

main_menu()