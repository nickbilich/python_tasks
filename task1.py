import argparse

instructions = "In this program we can create a chessboard. For this you should enter two positive integers."
#проверить количество столбцов
class Chessboard:
    def __init__(self, rows=None, cols=None):
        self.rows = rows
        self.cols = cols
        self.show_board()

    def create_board(self):
        chessboard = []
        for row in range(self.rows):
            inner = []
            for col in range(int(self.cols/2)):
                inner.append('*')
            chessboard.append(inner)
        return chessboard

    def show_board(self):
        for e, row in enumerate(self.create_board()):
            if e % 2 == 1:
                print(''.join([f' {el}' for el in row]))
            else:
                print(' '.join([f'{el}' for el in row]))

def is_valid(value):
    val = int(value)
    if val < 0:
        print(instructions)
        raise argparse.ArgumentError
    return val

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description='Enter two arguments - rows and cols for chessboard')
        parser.add_argument('rows', type=is_valid, help='Rows number')
        parser.add_argument('cols', type=is_valid, help='Cols number')
        args = parser.parse_args()
        Chessboard(args.rows, args.cols)
    except argparse.ArgumentError:
        exc = sys.exc_info()[1]
        print(f'Use positive integer, instead of: {exc}')
    except SystemExit:
        print(instructions)