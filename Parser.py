import string
import mathExpr as ME


def Error(str):
    print(str)


def CheckChar(char, CharList):
    for i in CharList:
        if i == char:
            return True
    return False


def id(input):
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    digits = [str(i) for i in range(0, 10)]
    CHARS = lower + upper + digits

    flag = False
    for i in lower:
        if input[0] == i: flag = True;break
    for i in upper:
        if input[0] == i: flag = True;break
    if flag:
        for i in input[1:]:
            if CheckChar(i, CHARS) == False:
                return False
        return True

    return False


def nummber(input):
    digits = [str(i) for i in range(0, 10)]
    flag = False
    for i in input:
        for j in digits:
            if i == j:
                flag = True
                break
        if flag == False:
            return False
        else:
            flag = False
    return True


def check_logic(list):
    for i in list:
        if i == '>' or i == '<' or i == '=' or i == '!':
            return True
    return False


def Parse(lists):
    return [Stmt(list) for list in lists]


def CheckExprNum(list):
    for i in list:
        if i == '=':
            return 1
        if i == 'if':
            return 2
        if i == 'while':
            return 3


def Stmt(list):
    ExprNum = CheckExprNum(list)
    if ExprNum == 1:
        return Expr1(list)
    if ExprNum == 2:
        return Expr2(list)
    if ExprNum == 3:
        return Expr3(list)


def FindLogic(list):
    start = 0
    flag1 = True
    end = 0
    flag2 = True
    for i in range(len(list)):
        if list[i] == '(' and flag1:
            flag1 = False
            start = i
        elif list[i] == ')' and flag2:
            flag2 = False
            end = i
    if end < start:
        return -1, -1
    elif end == start:
        return 0, 0
    else:
        return start, end


def Expr1(list):
    if id(list[0]) and list[1] == '=':
        return ME.math_expr(list[2:])
    else:
        Error('id error')
        return False


def Expr2(list):
    if list[0] == 'if':
        start, end = FindLogic(list[1:])
        if start + end == 0:
            Error('their no logical expr')
        elif start + end < 0:
            Error('logical expr () not correct')
        else:
            if check_logic(list[start + 1:end]):
                return Stmt(list[end + 2:])
            else:
                Error('logical expr not correct')
                return False


def Expr3(list):
    if list[0] == 'while':
        start, end = FindLogic(list[1:])
        if start + end == 0:
            Error('their no logical expr')
        elif start + end < 0:
            Error('logical expr () not correct')
        else:
            if check_logic(list[start + 1:end]):
                return Stmt(list[end + 2:])
            else:
                Error('logical expr not correct')
                return False
