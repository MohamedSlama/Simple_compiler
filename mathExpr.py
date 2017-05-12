import Parser as prs


def Term(list):
    start = []
    end = []
    operations = ['+', '-']
    for operation in operations:
        for i in range(len(list)):
            if list[i] == operation:
                start = list[:i]
                end = list[i + 1:]
                return start, end, operation
    return 0


def Factor(list):
    start = []
    end = []
    operations = ['*', '/']
    for operation in operations:
        for i in range(len(list)):
            if list[i] == operation:
                start = list[:i]
                end = list[i + 1:]
                return start, end, operation
    return 0


def Fact(list):
    if prs.nummber(list[0]) or prs.id(list[0]):
        return True
    else:
        return False


def math_expr(list):
    term = Term(list)
    if term == 0:
        factor = Factor(list)
        if factor == 0:
            if Fact(list):
                return True
            else:
                prs.Error('not fact');
                return False
        else:
            start, end, operation = factor
            if Fact(start):
                return math_expr(end)
            else:
                prs.Error('not fact');
                return False
    else:
        start, end, operation = term
        if math_expr(start):
            return math_expr(end)
        else:
            return false
