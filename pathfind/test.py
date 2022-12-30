from pathfinder import pathfind, printPath
from time import sleep
from os import system, name
if __name__ == '__main__':
    t = 2
    f = 1
    board = [
        [0 , 0 , 0 , 0, 0, 0, 0] ,
        [0 , 0 , f , f, f, f, 0] ,
        [0 , f , 0 , 0, 0, f, 0] ,
        [0 , f , 0 , f, 0, f, 0] ,
        [f , t , 0 , f, 0, 0, 0]
    ]
    basePath = list()
    basePath.append({ 'x': 0, 'y': 0 })

    exists = pathfind(0, 0, t, f, board, basePath)
    
    for step in range(len(exists)):
        if name == 'nt':
            system('cls')
        else:
            system('clear')
        printPath(exists, board, step)
        sleep(.5)