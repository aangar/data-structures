from pathfinder import pathfind
from time import sleep
from os import system, name
if __name__ == '__main__':
    t = 2
    f = 1
    board = [
        [0 , 0 , 0 , 0] ,
        [0 , 0 , f , 0] ,
        [0 , f , f , 0] ,
        [f , t , 0 , 0]
    ]
    basePath = list()
    basePath.append({ 'x': 0, 'y': 0 })

    exists = pathfind(0, 0, t, f, board, basePath)
    
    for _ in range(4):
        print('gamma', flush=True)
        sleep(1)

    if name == 'nt':
        system('cls')
    else:
        system('clear')