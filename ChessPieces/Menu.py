import pygame as py, sys

mainClock = py.time.Clock()
from pygame.locals import *

py.init()
white = (255, 255, 255)
navy = (43, 44, 64)
purple = (131, 103, 125)
blue = (104, 126, 140)
grey = (202, 202, 202)
py.display.set_caption('base game')
screen = py.display.set_mode((672, 672), 0, 2)

image2 = py.image.load(r'C:\Users\danim\OneDrive\Documents\College\ChessProject\num2.png')
image3 = py.image.load(r'C:\Users\danim\OneDrive\Documents\College\ChessProject\num3.png')
image4 = py.image.load(r'C:\Users\danim\OneDrive\Documents\College\ChessProject\num4.png')
image5 = py.image.load(r'C:\Users\danim\OneDrive\Documents\College\ChessProject\num5.png')
image6 = py.image.load(r'C:\Users\danim\OneDrive\Documents\College\ChessProject\num6.png')
image7 = py.image.load(r'C:\Users\danim\OneDrive\Documents\College\ChessProject\num7.png')
image8 = py.image.load(r'C:\Users\danim\OneDrive\Documents\College\ChessProject\num8.png')
image9 = py.image.load(r'C:\Users\danim\OneDrive\Documents\College\ChessProject\num9.png')
IMAGES = [image4, image5, image6, image7, image8, image9]


dialogue_font = py.font.SysFont('Verdana', 80)
dialogue = dialogue_font.render("Play Chess", True, (navy))
dialogue1_font = py.font.SysFont('Verdana', 16)
dialogue1 = dialogue1_font.render("Click the screen to begin!", True, (white))
dialogue11_font = py.font.SysFont('Verdana', 10)
dialogue11 = dialogue1_font.render("Press esc to exit", True, (white))
dialogue2_font = py.font.SysFont('Verdana', 40)
dialogue2 = dialogue2_font.render("Main Menu", True, (white))

dialogue3_font = py.font.SysFont('Verdana', 35)
dialogue3 = dialogue3_font.render("Play", True, (navy))

dialogue4_font = py.font.SysFont('Verdana', 35)
dialogue4 = dialogue4_font.render("Log in", True, (navy))

dialogue5_font = py.font.SysFont('Verdana', 35)
dialogue5 = dialogue5_font.render("Instructions", True, (navy))

dialogue6_font = py.font.SysFont('Verdana', 40)
dialogue6 = dialogue6_font.render("Instructions", True, (white))

dialogue7_font = py.font.SysFont('Verdana', 30)
dialogue7 = dialogue7_font.render("Next", True, (navy))


click = False
def main_menu():
    while True:

        screen.fill(purple)
        py.draw.rect(screen, white, py.Rect(14, 12, 642, 642), 10)
        screen.blit(image2, (430, 338))
        screen.blit(image3, (40, 400))
        screen.blit(dialogue, (125, 180))
        screen.blit(dialogue1, (240, 290))
        screen.blit(dialogue11, (510, 620))


        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    py.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                click = True
                if click:
                    menu()

        py.display.update()
        mainClock.tick(60)

# function used to write all the code for the menu section of the program
def menu():
    running = True
    while running:
        # While loop used to help the program differ between when the
        # program is and isn't running allowing for the escape/ exit game
        # function to work.
        screen.fill(purple)
        py.draw.rect(screen, white, py.Rect(14, 12, 642, 642), 10)
        py.draw.rect(screen, white, py.Rect(180, 200, 300, 340))
        py.draw.rect(screen, blue, py.Rect(185, 205, 290, 330))
        screen.blit(dialogue2, (220, 205))
        screen.blit(dialogue, (25, 10))
        # ^^writing the user interface for the main menu by loading in boxes
        # used for text as well as dialogue.
        mx, my = py.mouse.get_pos()

        button_1 = py.Rect(210, 260, 240, 70)  # creating the rectangles for the
        button_2 = py.Rect(210, 350, 240, 70)  # buttons that will lead to the
        button_3 = py.Rect(210, 440, 240, 70)  # other sections of the game.

        # writing the for loops for the buttons that will allow the user to navigate
        # through the pages of the game once pressed.
        if button_1.collidepoint((mx, my)):
            if click:
                main()
        py.draw.rect(screen, (grey), button_1)
        if button_2.collidepoint((mx, my)):
            if click:
                main_menu()
        py.draw.rect(screen, (grey), button_2)
        if button_3.collidepoint((mx, my)):
            if click:
                instructions()
        py.draw.rect(screen, (grey), button_3)
        click = False
        screen.blit(dialogue3, (295, 267))
        screen.blit(dialogue4, (280, 357))
        screen.blit(dialogue5, (222, 447))
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        py.display.update()
        mainClock.tick(60)

def main():
    pass

def instructions():
    running = True
    while running:
        screen.fill(purple)
        py.draw.rect(screen, white, py.Rect(14, 12, 642, 642), 10)
        py.draw.rect(screen, white, py.Rect(180, 200, 300, 340))
        py.draw.rect(screen, blue, py.Rect(185, 205, 290, 330))
        screen.blit(dialogue, (25, 10))
        mx, my = py.mouse.get_pos()
        screen.blit(dialogue6, (210, 148))
        screen.blit(dialogue11, (510, 620))
        # Creating the user interface for the instructions page by
        # calling upon shape and text variable.

        # Here I've created the button that will allow users to flip
        # through the instructions.
        button_4 = py.Rect(490, 350, 80, 70)
        # Creating an if statement that should allow users to flip
        # through the images once the button is pressed
        if button_4.collidepoint((mx, my)):
            if click:
                screen.blit(image4, (180, 200))
        py.draw.rect(screen, (grey), button_4)
        click = False
        screen.blit(dialogue7, (495, 362))
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        py.display.update()
        mainClock.tick(60)


main_menu()