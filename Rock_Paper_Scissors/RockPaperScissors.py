import pygame, sys, random

pygame.init()
win = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 45)
font1 = pygame.font.Font(None, 70)
click = False
my_score = 0
bot_score = 0

is_rock = 'false'
is_paper = 'false'
is_scissor = 'false' 

rock = pygame.image.load('Rock.png')
paper = pygame.image.load('Paper.png')
scissor = pygame.image.load('Scissors.png')

objects = [rock, paper, scissor]
bot_choice = random.choice(objects)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def txt_obj(text, font):
    txt_surface = font.render(text, True, (0,0,0))
    return txt_surface, txt_surface.get_rect()

def bot():
    if bot_choice == rock:
        return 'bot rock'

    if bot_choice == paper:
        return 'bot paper'

    if bot_choice == scissor:
        return 'bot scissor'

def who_wins():
    global is_rock, is_paper, is_scissor
    global my_score, bot_score

    #ROCK
    if is_rock == 'true':
        win.blit(rock, (70,75))

        #ROCK VS ROCK
        if bot() == 'bot rock':
            win.blit(rock, (315,75))

            draw_text('TIE', font, (0,0,0), win, 100,300)

        #ROCK VS PAPER
        elif bot() == 'bot paper':
            win.blit(paper, (315,225))

            draw_text('LOSE', font, (0,0,0), win, 100,300)

        #ROCK VS SCISSOR
        elif bot() == 'bot scissor':
            win.blit(scissor, (315,375))

            draw_text('WIN', font, (0,0,0), win, 100,300)


    #PAPER
    if is_paper == 'true':
        win.blit(paper, (70,225))

        #PAPER VS ROCK
        if bot() == 'bot rock':
            win.blit(rock, (315,75))

            draw_text('WIN', font, (0,0,0), win, 100,300)

        #PAPER VS PAPER
        elif bot() == 'bot paper':
            win.blit(paper, (315,225))

            draw_text('TIE', font, (0,0,0), win, 100,300)

        #PAPER VS SCISSOR
        elif bot() == 'bot scissor':             
            win.blit(scissor, (315,375))

            draw_text('LOSE', font, (0,0,0), win, 100,300)

    #SCISSOR
    if is_scissor == 'true':
        win.blit(scissor, (70,375))

        #SCISSOR VS ROCK
        if bot() == 'bot rock':
            win.blit(rock, (315,75))

            draw_text('LOSE', font, (0,0,0), win, 100,300)

        #SCISSOR VS PAPER
        elif bot() == 'bot paper':
            win.blit(paper, (315,225))

            draw_text('WIN', font, (0,0,0), win, 100,300)

        #SCISSOR VS SCISSOR
        elif bot() == 'bot scissor':
            win.blit(scissor, (315,375))

            draw_text('TIE', font, (0,0,0), win, 100,300)


def menu():
    global is_rock, is_paper, is_scissor
    global bot_choice, objects

    is_rock = 'false'
    is_paper = 'false'
    is_scissor = 'false'

    bot_choice = random.choice(objects)
    while True:
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mx, my = pygame.mouse.get_pos()

        win.fill((255,255,255))

        split = pygame.Rect(250,0, 5,600)
        pygame.draw.rect(win, (0,0,0), split)

        draw_text('YOU', font1, (0,0,0), win, 70, 10)
        draw_text('BOT', font1, (0,0,0), win, 315, 10)


        #ROCK BUTTON
        rock_btn = pygame.Rect(70,75, 100,100)
        pygame.draw.rect(win, (255,255,255), rock_btn)
        win.blit(rock, (70,75))

        if rock_btn.collidepoint((mx, my)):
            if click:
                is_rock = 'true'
                game()

        win.blit(rock, (315,75))

        #PAPER BUTTON
        paper_btn = pygame.Rect(70,225, 100,100)
        pygame.draw.rect(win, (255,255,255), paper_btn)
        win.blit(paper, (70,225))

        if paper_btn.collidepoint((mx, my)):
            if click:
                is_paper = 'true'
                game()

        win.blit(paper, (315,225))

        #SCISSOR BUTTON
        scissor_btn = pygame.Rect(70,375, 100,100)
        pygame.draw.rect(win, (255,255,255), scissor_btn)
        win.blit(scissor, (70,375))

        if scissor_btn.collidepoint((mx, my)):
            if click:
                is_scissor = 'true'
                game()

        win.blit(scissor, (315,375))

        pygame.display.update()

def game():
    global is_rock, is_paper, is_scissor
    global my_score, bot_score
    while True:

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mx, my = pygame.mouse.get_pos()

        win.fill((255,255,255))

        who_wins()      

        #BACK BUTTON
        back_btn = pygame.Rect(335,10, 150,50)
        back_btn_text = pygame.font.Font('freesansbold.ttf', 25)
        txt_surf, txt_rect = txt_obj("BACK", back_btn_text)
        txt_rect.center = ((335+(150/2)), (10+(50/2)))
        pygame.draw.rect(win, (255,0,255), back_btn)
        win.blit(txt_surf, txt_rect)
        if back_btn.collidepoint((mx, my)):
            if click:
                menu()

        #SPLIT SCREEN
        split = pygame.Rect(250,0, 5,600)
        pygame.draw.rect(win, (0,0,0), split)

        draw_text('YOU', font1, (0,0,0), win, 70, 10)
        draw_text('BOT', font1, (0,0,0), win, 315, 10)

        #SCORE
        draw_text(str(my_score), font1, (0,0,0), win, 70, 375)
        draw_text(str(bot_score), font1, (0,0,0), win, 200, 375)

        pygame.display.update()

menu()    