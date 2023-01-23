import pygame
import sys
from ButtonforMenu import Button
import main as l
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
BG = pygame.image.load("imagesMenu/background.png")
def getFont(size):  # Returns Press-Start-2P in the desired size
  return pygame.font.Font("imagesMenu/font.ttf", size)

def rules():
  # infinite loop
  while True:
    # get the current position of the mouse
    RULES_MOUSE_POS = pygame.mouse.get_pos()
    # create a window with the dimensions of 1280x720
    SCREEN = pygame.display.set_mode((1280, 720))
    # load image called "rules.png"
    RULES_IMAGE = pygame.image.load("rules.png")  
    # draw the image on the screen at position (0,0)
    SCREEN.blit(RULES_IMAGE, (0, 0))
    # Create a button object called "RULES_BACK" with the text "BACK"
    RULES_BACK = Button(image=None, pos=(950, 65), text_input="BACK", font=getFont(40), base_color="RED", hovering_color="Green")
    # change the color of the button depending on the current position of the mouse
    RULES_BACK.changeColor(RULES_MOUSE_POS)
    # update the screen with the button object
    RULES_BACK.update(SCREEN)
    # loop through events in the event queue
    for event in pygame.event.get():
        # if the event is a quit event (e.g. user closes the window)
        if event.type == pygame.QUIT:
            # stop the pygame library from running
            pygame.quit()
            # stop the program from running
            sys.exit()
        # if the event is a mouse button down event
        if event.type == pygame.MOUSEBUTTONDOWN:
            # check if the mouse is currently over the "RULES_BACK" button
            if RULES_BACK.checkForInput(RULES_MOUSE_POS):
                # call the function "main_menu()"
                mainMenu()
    # update the screen with any changes made during the current iteration of the loop
    pygame.display.update()

def mainMenu():
  # infinite loop
  while True:
    # draw the background image on the screen at position (0,0)
    SCREEN.blit(BG, (0, 0))
    # get the current position of the mouse
    MENU_MOUSE_POS = pygame.mouse.get_pos()
    # create text object with the text "MAIN MENU"
    MENU_TEXT = getFont(100).render("MAIN MENU", True, "#b68f40")
    # create rectangle object that surrounds the "MENU_TEXT" and centers it at position (640, 100)
    MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
    # Create "LOGIN_BUTTON" button object with text "Login" and background image "imagesMenu/LoginRect.png"
    LOGIN_BUTTON = Button(image=pygame.image.load("imagesMenu/LoginRect.png"),
                         pos=(640, 250),
                         text_input="Login",
                         font=getFont(75),
                         base_color="#d7fcd4",
                         hovering_color="White")
    # Create "RULES_BUTTON" button object with text "RULES" and background image "imagesMenu/RulesRect.png"
    RULES_BUTTON = Button(image=pygame.image.load("imagesMenu/RulesRect.png"),
                            pos=(640, 400),
                            text_input="RULES",
                            font=getFont(75),
                            base_color="#d7fcd4",
                            hovering_color="White")
    # Create "QUIT_BUTTON" button object with text "QUIT" and background image "imagesMenu/QuitRect.png"
    QUIT_BUTTON = Button(image=pygame.image.load("imagesMenu/QuitRect.png"),
                         pos=(640, 550),
                         text_input="QUIT",
                         font=getFont(75),
                         base_color="#d7fcd4",
                         hovering_color="White")
    # draw the "MENU_TEXT" on the screen at the position defined by the "MENU_RECT"
    SCREEN.blit(MENU_TEXT, MENU_RECT)
    # change the color of the buttons depending on the current position of the mouse
    for button in [LOGIN_BUTTON, RULES_BUTTON, QUIT_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(SCREEN)
    # loop through events in the event queue
    for event in pygame.event.get():
        # if the event is a quit event (e.g. user closes the window)
        if event.type == pygame.QUIT:
            # stop the pygame library from running
            pygame.quit()
            # stop the program from running
            sys.exit()
        # if the event is a mouse button down event
        if event.type == pygame.MOUSEBUTTONDOWN:
          if LOGIN_BUTTON.checkForInput(MENU_MOUSE_POS):
            l.mainLogin()
          if RULES_BUTTON.checkForInput(MENU_MOUSE_POS):
            rules()
          if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
            pygame.quit()
            sys.exit()
            
    pygame.display.update()

mainMenu()