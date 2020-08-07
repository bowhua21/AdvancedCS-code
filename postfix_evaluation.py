import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}

def evaluate(expression):
    exp = expression.split()
    s = []
    for i in exp:
        if i.isnumeric():
            s.append(i)
        else:
            right = (int)(s.pop())
            left = (int)(s.pop())
            s.append(ops[i](left,right))
    return s

print(evaluate("8 3 5 + *"))