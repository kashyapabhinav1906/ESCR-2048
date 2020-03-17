import random

tiles = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

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
        return 'Game Over'

def win(tiles):
    for i in range(4):
        for j in range(4):
            if tiles[i][j] == 2048:
                return 'Congratulations! You have won the game.'

def left(tiles):
    new_tiles=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        p=0
        for j in range(4):
            if tiles[i][j]!=0:
                new_tiles[i][p]=tiles[i][j]             
                p+=1

    for i in range(4):
        for j in range(3):
            if new_tiles[i][j]==new_tiles[i][j+1] and new_tiles[i][j]!=0:
                new_tiles[i][j]+=new_tiles[i][j]                 
                new_tiles[i][j+1]=0

    final_tiles=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        q=0
        for j in range(4):
            if new_tiles[i][j]!=0:
                final_tiles[i][q]=new_tiles[i][j]             
                q+=1
    random_generate(final_tiles)
    win(final_tiles)
    return final_tiles

def right(tiles):
    new_tiles=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        p=3
        for j in range(4)[::-1]:
            if tiles[i][j]!=0:
                new_tiles[i][p]=tiles[i][j]             
                p-=1

    for i in range(4):
        for j in range(3)[::-1]:
            if new_tiles[i][j+1]==new_tiles[i][j] and new_tiles[i][j+1]!=0:
                new_tiles[i][j+1]+=new_tiles[i][j+1]                 
                new_tiles[i][j]=0

    final_tiles=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        q=3
        for j in range(4)[::-1]:
            if new_tiles[i][j]!=0:
                final_tiles[i][q]=new_tiles[i][j]             
                q-=1
    random_generate(final_tiles)
    win(final_tiles)
    return final_tiles


def up(tiles):
    new_tiles=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for j in range(4):
        p=0
        for i in range(4):
            if tiles[i][j]!=0:
                new_tiles[p][j]=tiles[i][j]             
                p+=1

    for j in range(4):
        for i in range(3):
            if new_tiles[i][j]==new_tiles[i+1][j] and new_tiles[i][j]!=0:
                new_tiles[i][j]+=new_tiles[i][j]                 
                new_tiles[i+1][j]=0

    final_tiles=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for j in range(4):
        q=0
        for i in range(4):
            if new_tiles[i][j]!=0:
                final_tiles[q][j]=new_tiles[i][j]             
                q+=1
    random_generate(final_tiles)
    win(final_tiles)
    return final_tiles

def down(tiles):
    new_tiles=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for j in range(4):
        p=3
        for i in range(4)[::-1]:
            if tiles[i][j]!=0:
                new_tiles[p][j]=tiles[i][j]             
                p-=1

    for j in range(4):
        for i in range(3)[::-1]:
            if new_tiles[i+1][j]==new_tiles[i][j] and new_tiles[i+1][j]!=0:
                new_tiles[i+1][j]+=new_tiles[i+1][j]                 
                new_tiles[i][j]=0

    final_tiles=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for j in range(4):
        q=3
        for i in range(4)[::-1]:
            if new_tiles[i][j]!=0:
                final_tiles[q][j]=new_tiles[i][j]             
                q-=1
    random_generate(final_tiles)
    win(final_tiles)
    return final_tiles

# TESTING

# problem in this type
# print(initialise(tiles))
# print(right(tiles))
# print(left(right(tiles)))
# print(up(right(left(tiles))))
# print(down(up(right(left(tiles)))))


# working correctly
# print(right([[0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 0], [0, 0, 2, 0]]))
# print(up([[0, 0, 0, 2], [2, 0, 0, 2], [0, 0, 0, 0], [0, 0, 0, 2]]))
