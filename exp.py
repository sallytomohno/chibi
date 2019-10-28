class Expr :
    def eval(self) :
        pass
    
def expr(x):
    if not isinstance(x, Expr) :
        x = Val(x)
    return x
class Binary(Expr) :
    def __init__(self, left, right) :
        self.left = expr(left)
        self.right = expr(right)
    def __repr__(self) :
        classname = self.__class__.__name__
        return f'{classname}({self.left} , {self.right})'
class Val(Expr) :
    __slots__ = ["value"]
    def __init__(self, value = 0) :
        self.value = value
    def eval(self) :
        return self.value
    def __repr__(self) :
        return f'Val({self.value})'
class Add(Binary) :
    __slots__ = ["left", "right"]
    def __init__(self, left, right) :
        self.left = expr(left)
        self.right = expr(right)
    def eval(self) :
        return self.left.eval() + self.right.eval()
class Mul(Binary) :
    __slots__ = ["left", "right"]
    def __init__(self, left, right) :
        self.left = expr(left)
        self.right = expr(right)
    
    def eval(self) :
        return self.left.eval() * self.right.eval()
class Sub(Binary) :
    __slots__ = ["left", "right"]
    def __init__(self, left, right) :
        self.left = expr(left)
        self.right = expr(right)
    
    def eval(self) :
        return self.left.eval() - self.right.eval()
    
class Div(Binary) :
    __slots__ = ["left", "right"]
    def __init__(self, left, right) :
        self.left = expr(left)
        self.right = expr(right)
        
    def eval(self) :
        return self.left.eval() // self.right.eval()
e = Add(1, 2)
assert e.eval () == 3
print("OK")




