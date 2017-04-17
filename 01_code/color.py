
#COLORS = dict(zip(range(1, 10), 'black red green yellow blue magenta'
#                  ' cyan white reset'.split()))

class BG:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    yellow = '\033[43m'
    blue = '\033[44m'
    magenta = '\033[45m'
    cyan = '\033[46m'
    white = '\033[47m'
    reset = '\033[49m'


class FG:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
    reset = '\033[39m'


class BRIGHT:
    bright = '\033[1m'
    dim = '\033[2m'
    normal = '\033[22m'


class Color:
    resetall = '\033[0m'


#print(BG.red+ FG.green + "Warning: No active frommets remain. Continue?" + BG.reset + FG.reset)

def printe(e) :
	print(BG.red + e + BG.reset)
	exit(1)

