def pathfind(x, y, target, board, path):
    '''
    syntax for board usage
    x = subelement, spec sptos
    y = row index
    '''
    if board[y][x] == target:
        return path

    canGoUp = y - 1 >= 0 and len(board[y - 1]) - 1 >= x
    canGoDown = y + 1 <= len(board) - 1 and len(board[y + 1]) - 1 >= x
    
    currentRow = board[y]
    canGoRight = x + 1 <= len(currentRow) - 1
    canGoLeft = x - 1 >= 0

    leftResult = None
    rightResult = None
    upResult = None
    downResult = None

    if canGoUp:
        nextX = x
        nextY = y - 1
        history = isInPath(nextX, nextY, path)
        if not history and not board[nextY][nextX] == 1:
            newPath = list(path)
            newPath.append(generateCoordinates(nextX, nextY))
            upResult = pathfind(nextX, nextY, target, board, newPath)
    if canGoDown:
        nextX = x
        nextY = y + 1
        history = isInPath(nextX, nextY, path)
        if not history and not board[nextY][nextX] == 1:
            newPath = list(path)
            newPath.append(generateCoordinates(nextX, nextY))
            downResult = pathfind(nextX, nextY, target, board, newPath)
    if canGoLeft:
        nextX = x - 1
        nextY = y
        history = isInPath(nextX, nextY, path)
        if not history and not board[nextY][nextX] == 1:
            newPath = list(path)
            newPath.append(generateCoordinates(nextX, nextY))
            leftResult = pathfind(nextX, nextY, target, board, newPath)
    if canGoRight:
        nextX = x + 1
        nextY = y
        history = isInPath(nextX, nextY, path)
        if not history and not board[nextY][nextX] == 1:
            newPath = list(path)
            newPath.append(generateCoordinates(nextX, nextY))
            rightResult = pathfind(nextX, nextY, target, board, newPath)

    exists = list()
    for i in [leftResult, rightResult, upResult, downResult]:
        if not i == None:
            exists.append(i)
   
    if len(exists) > 0:
        currentLowPath = exists[0]
        for i in exists:
            if len(i) < len(currentLowPath):
                currentLowPath = i
        return currentLowPath


def generateCoordinates(x, y):
    #tf you think it does???
    return { 'x' : x, 'y' : y }

def isInPath(x , y, path):
    doesContain = False
    step = 0
    while not doesContain and step < len(path):
        pair = path[step]
        if pair.get('x') == x and pair.get('y') == y:
            doesContain = True
        step += 1
    return doesContain

if __name__ == '__main__':
    t = 2
    board = [
        [0 , 0 , 0 , 0] ,
        [0 , 0 , 1 , 0] ,
        [0 , 1 , 1 , 0] ,
        [1 , t , 0 , 0]
    ]
    basePath = list()
    basePath.append(generateCoordinates(0, 0))

    exists = pathfind(0, 0, t, board, basePath)
    print(exists)