import numpy as np

white = 1
black = -1
blank = 0
tablesize = 8

class Board(object):
    # 初期設定
    def __init__(self):
        self.cell = np.zeros((tablesize,tablesize))
        self.cell = self.cell.astype(int)
        self.cell[3][3] = self.cell[4][4] = 1
        self.cell[3][4] = self.cell[4][3] = -1
        self.current = black
        self.pass_count = 0
        self.turn = 1

    def turnchange(self):  #  ＊
        self.current*= -1
    def stonenumber(self):
        return self.stones

    def rangecheck(self,x,y):  # ①　盤内かどうか　
        if x == None: x = -1
        if y == None: y = -1
        if x < 0 or tablesize <=x  or y < 0 or tablesize <= y:
            return False
        return True

    def check_can_reverse(self,x,y):  # 置けるかどうか
        if not self.rangecheck(x,y):   # →　①へ
            return False
        elif not self.cell[x][y] == blank:   #  ②
            return False
        elif not self.can_reverse_stone(x,y):   # →　③へ
            return False
        else: return True

    def can_reverse_one(self,x,y,dx,dy):  # ⑶、⑷　　(dx,dy)方向に敵石があり、その先に自石があるかどうか

        if not self.rangecheck(x+dx,y+dy):
            return False
            length = 0
            if not self.cell[x + dx][y + dy] == -self.current: #  ⑶
                return False # (dx,dy)方向が敵石じゃない時False
            else:    
                while self.cell[x+dx][y+dy] == -self.current: 
                    x +=dx
                    y +=dy
                    length += 1
                    if self.cell[x+dx][y+dy] == self.current:  # ⑷-True
                        return length
                    elif not self.cell[x+dx][y+dy] == -self.current:
                        continue
                    else: return False
                else: return False  # ⑷-False

    def can_reverse_stone(self,x,y):  # 　③入力座標ではひっくり返せる石はあるか
        for dx in range(-1,2):
            for dy in range(-1,2):
                if dx == dy == 0: continue   # ⑴
                elif not self.rangecheck(x+dx,y+dy): continue  # ①（調べた範囲が番外だったらエラーが起こるため）
                elif not self.can_reverse_one(x,y,dx,dy):  # →　⑶、⑷の処理へ
                    continue
                else: return True

    def reverse_stone(self,x,y): #  ④ 座標に石を置いて石をひっくり返す
            for dx in (-1,0,1):
                for dy in (-1,0,1):
                    length = self.can_reverse_one(x,y,dx,dy)
                    if length == None: length = 0
                    if length > 0:
                        for l in range(length):
                            k = l+1
                            self.cell[x + dx*k][y + dy*k] *= -1

    def display(self):  # 盤面の状況を表示
        print('==='*10)   #  *(下の文を参照）
        for y in range(tablesize):
            for x in range(tablesize):
                if self.cell[x][y] == white:
                    print('W', end = '  ')
                elif self.cell[x][y] == black:
                    print('B', end = '  ')
                else:
                    print('*', end = '  ')
            print('\n', end = '')

    def put_stone(self,x,y):  # 一回のターン内の行動 
        if self.check_can_reverse(x,y):   # 入力座標に石を置ける
            self.pass_count = 0
            self.cell[x][y] = self.current
            self.reverse_stone(x,y)
            self.turnchange()
            return True
        else:  # 入力座標に石を置けない
            return False

    def check_put_place(self):  # ❶盤面上に石が置ける場所があるか　次のクラスの時に使用
        for i in range(tablesize):
            for j in range(tablesize):
                if self.check_can_reverse(i,j): # (i,j)座標に置いて石が置けたら成立
                    return True
                else:continue
        return False

if __name__ == '__main__':
    board = Board()
    board.display()
    board.put_stone(3,2)
    board.display()
    board.put_stone(2,2)
    board.display()
    board.put_stone(5,2)
    board.display()