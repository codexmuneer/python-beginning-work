'''TAKE INPUT AS A STRING AND RETURN ANS'''
def arithmetic_operation(equation):
    '''
    Returns the result of evaluating the string equation
    '''
    from operator import add, sub, floordiv, mul

    OPS = {'+':add, '-':sub, '*':mul, '//':floordiv}
    a,op,b = equation.split()
    
    try:
        return OPS[op](int(a),int(b)) 
    except ZeroDivisionError:
        return -1

# def arithmetic_operation(n):
#     a, op, b = n.split()
#     if op == '+':
#         return int(a) + int(b)
#     if op == '-':
#         return int(a) - int(b)
#     if op == '*':
#         return int(a) * int(b)
#     if b == '0':
#         return -1
#     return int(a) // int(b)

x = arithmetic_operation("12 + 12")
print(x)

# eval(n) ---> builtin function if inside condition is true it will give output