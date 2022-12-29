from pathfinder import pathfind
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
    print(exists)