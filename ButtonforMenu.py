#Class foor the buttons located in Main Menu
class Button():
  def __init__(self, image, pos, text_input, font, base_color, hovering_color):
    # assign the "image" parameter to an instance variable called "image"
    self.image = image
    # assign the x-coordinate of the "pos" tuple to an instance variable called "x_pos"
    self.x_pos = pos[0]
    # assign the y-coordinate of the "pos" tuple to an instance variable called "y_pos"
    self.y_pos = pos[1]
    # assign the "font" parameter to an instance variable called "font"
    self.font = font
    # assign the "base_color" and "hovering_color" parameters to instance variables with the same name
    self.base_color, self.hovering_color = base_color, hovering_color
    # assign the "text_input" parameter to an instance variable called "text_input"
    self.text_input = text_input
    # create text object with the text "text_input" and color "base_color"
    self.text = self.font.render(self.text_input, True, self.base_color)
    # if the "image" is None, assign the text object to the image
    if self.image is None:
        self.image = self.text
    # create a rectangle object that surrounds the "image" and centers it at position (x_pos, y_pos)
    self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
    # create a rectangle object that surround the "text" and centers it at position (x_pos, y_pos)
    self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
    
  def update(self, screen):
    # if the button has an image, draw the image on the screen at the position defined by the "rect" variable
    if self.image is not None:
        screen.blit(self.image, self.rect)
    # draw the text on the screen at the position defined by the "text_rect" variable
    screen.blit(self.text, self.text_rect)

  def checkForInput(self, position):
    # check if the x-coordinate of the position is within the range of the left and right sides of the button rectangle
    # and check if the y-coordinate of the position is within the range of the top and bottom sides of the button rectangle
    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
        # if the above conditions are met, return True
        return True
    # if the above conditions are not met, return False
    return False

  def changeColor(self, position):
    # check if the x-coordinate of the position is within the range of the left and right sides of the button rectangle
    # and check if the y-coordinate of the position is within the range of the top and bottom sides of the button rectangle
    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
        # if the above conditions are met, re-render the text with the color "hovering_color"
        self.text = self.font.render(self.text_input, True, self.hovering_color)
    else:
        # if the above conditions are not met, re-render the text with the color "base_color"
        self.text = self.font.render(self.text_input, True, self.base_color)
