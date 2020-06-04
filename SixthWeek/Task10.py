class KeyBoard:
    numOfKeys = 0
    stayingPower = 0
    numOfPresses = 0
    presses = 0


def Count(Keys, press):
    cntOfKeys = [0] * Keys
    for i in press:
        cntOfKeys[i - 1] += 1
    return cntOfKeys


def Comparison(power, press):
    for i in range(len(power)):
        if int(power[i]) >= int(press[i]):
            print("NO")
        else:
            print("YES")


n = int(input())
c = [int(i) for i in input().split()]
k = int(input())
pj = [int(i) for i in input().split()]
board = KeyBoard()
board.numOfKeys = n
board.stayingPower = c
board.numOfPresses = k
board.presses = pj
count = Count(board.numOfKeys, board.presses)
Comparison(board.stayingPower, count)
