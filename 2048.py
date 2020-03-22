import pygame
import random

pygame.init()      # initialising pygame

# creating game window
screen_width = 400
screen_height = 600
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('2048 Game')
pygame.display.update()

# global game variables
game_over = False
score = 0
with open("highscore.txt", "r") as f:
    highscore = f.read()

# for handling fps
clock = pygame.time.Clock()

# for writing in game window
font = pygame.font.SysFont(None, 60)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x,y])

# list of images
numbers = [pygame.image.load(str(2**i)+'.gif') for i in range(1,12)]
eg = pygame.image.load('empty_grid.gif')
GameOver = pygame.image.load('game_over.gif')
winner = pygame.image.load('winner.gif')

# dictionary of number images
number_images = {2: numbers[0], 4: numbers[1], 8: numbers[2], 16: numbers[3], 32: numbers[4], 64: numbers[5],
128: numbers[6], 256: numbers[7], 512: numbers[8], 1024: numbers[9], 2048: numbers[10]}


# functions for grid visualisation

def mat_to_grid(tiles):
    game_window.blit(eg, (0, 200))
    for i in range(4):
        for j in range(4):
            if tiles[i][j] != 0:
                game_window.blit(number_images[tiles[i][j]], (j*100, (i+2)*100))
    pygame.display.update()


def move_left(image, x1, y1, x2, y2):
    (x, y) = (x1, y1)
    game_window.blit(image, (x, y))
    pygame.display.update()
    while x>x2:
        x -= 1
        game_window.blit(image, (x, y))
        pygame.display.update()

def move_right(image, x1, y1, x2, y2):
    (x, y) = (x1, y1)
    game_window.blit(image, (x, y))
    pygame.display.update()
    while x<x2:
        x += 1
        game_window.blit(image, (x, y))
        pygame.display.update()

def move_up(image, x1, y1, x2, y2):
    (x, y) = (x1, y1)
    game_window.blit(image, (x, y))
    pygame.display.update()
    while y>y2:
        y -= 1
        game_window.blit(image, (x, y))
        pygame.display.update()

def move_down(image, x1, y1, x2, y2):
    (x, y) = (x1, y1)
    game_window.blit(image, (x, y))
    pygame.display.update()
    while y<y2:
        y += 1
        game_window.blit(image, (x, y))
        pygame.display.update()

# functions for control
def initialise(tiles):
    i1 = random.randint(0, 3)
    j1 = random.randint(0, 3)
    i2 = random.randint(0, 3)
    j2 = random.randint(0, 3)
    if i2 == i1 and j2 == j1:
        i2 = random.randint(0, 3)
        j2 = random.randint(0, 3)
    tiles[j1][i1] = 2
    tiles[j2][i2] = 2
    return tiles

def random_generate(tiles):
    global game_over
    zero_tiles = []
    for i in range(4):
        for j in range(4):
            if tiles[i][j] == 0:
                zero_tiles.append([i, j])
    if len(zero_tiles) > 0:
        x = random.randint(0, len(zero_tiles)-1)
        tiles[zero_tiles[x][0]][zero_tiles[x][1]] = 2
        return tiles
    else:
        game_over = True

def win(tiles):
    for i in range(4):
        for j in range(4):
            if tiles[i][j] == 2048:
                game_window.blit(winner, (0, 0))

def left(tiles):
    global score
    global number_images
    new_tiles=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        p=0
        for j in range(4):
            if tiles[i][j]!=0:
                new_tiles[i][p]=tiles[i][j] 
                move_left(number_images[tiles[i][j]], j*100, (i+2)*100, p*100, (i+2)*100)            
                p+=1

    for i in range(4):
        for j in range(3):
            if new_tiles[i][j]==new_tiles[i][j+1] and new_tiles[i][j]!=0:
                new_tiles[i][j]+=new_tiles[i][j]                 
                new_tiles[i][j+1]=0
                game_window.blit(number_images[new_tiles[i][j]], (j*100, (i+2)*100))
                score += new_tiles[i][j]

    final_tiles=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        q=0
        for j in range(4):
            if new_tiles[i][j]!=0:
                final_tiles[i][q]=new_tiles[i][j]   
                move_left(number_images[new_tiles[i][j]], j*100, (i+2)*100, q*100, (i+2)*100)          
                q+=1

    random_generate(final_tiles)
    win(final_tiles)
    return final_tiles

def right(tiles):
    global score
    global number_images
    new_tiles=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        p=3
        for j in range(4)[::-1]:
            if tiles[i][j]!=0:
                new_tiles[i][p]=tiles[i][j]
                move_right(number_images[tiles[i][j]], j*100, (i+2)*100, p*100, (i+2)*100)             
                p-=1

    for i in range(4):
        for j in range(3)[::-1]:
            if new_tiles[i][j+1]==new_tiles[i][j] and new_tiles[i][j+1]!=0:
                new_tiles[i][j+1]+=new_tiles[i][j+1]                 
                new_tiles[i][j]=0
                game_window.blit(number_images[new_tiles[i][j+1]], ((j+1)*100, (i+2)*100))
                score += new_tiles[i][j+1]

    final_tiles=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        q=3
        for j in range(4)[::-1]:
            if new_tiles[i][j]!=0:
                final_tiles[i][q]=new_tiles[i][j]
                move_right(number_images[new_tiles[i][j]], j*100, (i+2)*100, q*100, (i+2)*100)             
                q-=1
    random_generate(final_tiles)
    win(final_tiles)
    return final_tiles


def up(tiles):
    global score
    global number_images
    new_tiles=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for j in range(4):
        p=0
        for i in range(4):
            if tiles[i][j]!=0:
                new_tiles[p][j]=tiles[i][j] 
                move_up(number_images[tiles[i][j]], j*100, (i+2)*100, j*100, (p+2)*100)            
                p+=1

    for j in range(4):
        for i in range(3):
            if new_tiles[i][j]==new_tiles[i+1][j] and new_tiles[i][j]!=0:
                new_tiles[i][j]+=new_tiles[i][j]                 
                new_tiles[i+1][j]=0
                game_window.blit(number_images[new_tiles[i][j]], ((j)*100, (i+2)*100))
                score += new_tiles[i][j]

    final_tiles=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for j in range(4):
        q=0
        for i in range(4):
            if new_tiles[i][j]!=0:
                final_tiles[q][j]=new_tiles[i][j] 
                move_up(number_images[new_tiles[i][j]], j*100, (i+2)*100, j*100, (q+2)*100)            
                q+=1
    random_generate(final_tiles)
    win(final_tiles)
    return final_tiles

def down(tiles):
    global score
    global number_images
    new_tiles=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for j in range(4):
        p=3
        for i in range(4)[::-1]:
            if tiles[i][j]!=0:
                new_tiles[p][j]=tiles[i][j]  
                move_down(number_images[tiles[i][j]], j*100, (i+2)*100, j*100, (p+2)*100)           
                p-=1

    for j in range(4):
        for i in range(3)[::-1]:
            if new_tiles[i+1][j]==new_tiles[i][j] and new_tiles[i+1][j]!=0:
                new_tiles[i+1][j]+=new_tiles[i+1][j]                 
                new_tiles[i][j]=0
                game_window.blit(number_images[new_tiles[i+1][j]], ((j)*100, (i+3)*100))
                score += new_tiles[i+1][j]

    final_tiles=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for j in range(4):
        q=3
        for i in range(4)[::-1]:
            if new_tiles[i][j]!=0:
                final_tiles[q][j]=new_tiles[i][j]   
                move_down(number_images[new_tiles[i][j]], j*100, (i+2)*100, j*100, (q+2)*100)          
                q-=1
    random_generate(final_tiles)
    win(final_tiles)
    return final_tiles




    
# game loop
def gameloop():             
    # game variables
    exit_game = False
    global game_over
    game_over = False
    tiles = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    global score
    score = 0
    global highscore

    # coordinates for first two tiles
    initialise(tiles)
    
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            game_window.blit(GameOver, (0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        
        else:
            game_window.fill((255, 255, 255))
            mat_to_grid(tiles)
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        tiles = down(tiles)
                        mat_to_grid(tiles)
                    elif event.key == pygame.K_UP:
                        tiles = up(tiles)
                        mat_to_grid(tiles)
                    elif event.key == pygame.K_LEFT:
                        tiles = left(tiles)
                        mat_to_grid(tiles)
                    elif event.key == pygame.K_RIGHT:
                        tiles = right(tiles)
                        mat_to_grid(tiles)
            if score >= int(highscore):
                highscore = score
        text_screen("Score: " + str(score), (0, 0, 255), 5, 5)
        text_screen("Highscore: "+str(highscore), (0, 0, 255), 5, 60)
        pygame.display.update()
        clock.tick(120)
    pygame.quit()
    quit()

gameloop()



