#Name: Eshan Adatia 
#Date: December 20, 2022
#Progam Name: BlackJack Game with GUI and Database
#Description: BlackJack game that has a login in the window using a database to determine the funds in which the user can use/bet. The game is shown through GUI using buttons 
#Program Purpose: Create a functional game that incorporates everything we learned in grade 11 comp sci

#Purpose of this code: Menu that connects rules, with login database and game
import pygame, sys
from ButtonforMenu import Button

#Initalizes screen and sets specific dimensions
pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
#Creates backround image from image file and transforms image to window size
BG = pygame.image.load("imagesMenu/Background.png")
SCREEN.blit(pygame.transform.scale(BG, (1280, 720)), (0,0))

#Gets the specific font from images file and returns in specific size
def font_size(size):  
  return pygame.font.Font("imagesMenu/font.ttf", size)

#Rules for User displayed function
def rules():
  while True:
    #Gets mouse position when button is clicked
    RULES_MOUSE_POS = pygame.mouse.get_pos()
    #Fills screen ith white to overlap menu
    SCREEN.fill("white")
    #Fills in options text
    RULES_TEXT = font_size(45).render("This is the RULES screen.", True,
                                       "Black")
    #Creates a rectangle where the text is displayed and sets dimensions of rectangle
    RULES_RECT = RULES_TEXT.get_rect(center=(640, 260))
    SCREEN.blit(RULES_TEXT, RULES_RECT)
    #Creates a back button to go back to main menu, sets position, text, font, and colour
    RULES_BACK = Button(image=None,
                          pos=(640, 460),
                          text_input="BACK",
                          font=font_size(75),
                          base_color="Black",
                          hovering_color="Green")

    RULES_BACK.changeColor(RULES_MOUSE_POS)
    #Updates screen when back button is clicked
    RULES_BACK.update(SCREEN)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if RULES_BACK.checkForInput(RULES_MOUSE_POS):
          loading_menu()

    pygame.display.update()


def loading_menu():
  while True:
    SCREEN.blit(BG, (0, 0))

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    MENU_TEXT = font_size(100).render("LOADING MENU", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

    LOGIN_BUTTON = Button(image=pygame.image.load("imagesMenu/LoginRect.png"),
                         pos=(640, 250),
                         text_input="LOGIN",
                         font=font_size(75),
                         base_color="#d7fcd4",
                         hovering_color="White")
    RULES_BUTTON = Button(image=pygame.image.load("imagesMenu/RulesRect.png"),
                            pos=(640, 400),
                            text_input="RULES",
                            font=font_size(75),
                            base_color="#d7fcd4",
                            hovering_color="White")
    QUIT_BUTTON = Button(image=pygame.image.load("imagesMenu/QuitRect.png"),
                         pos=(640, 550),
                         text_input="QUIT",
                         font=font_size(75),
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
          LoginWindow()
        if RULES_BUTTON.checkForInput(MENU_MOUSE_POS):
          rules()
        if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
          pygame.quit()
          sys.exit()

    pygame.display.update()


loading_menu()
