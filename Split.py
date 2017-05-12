def operation(op):
    opList = ['+', '-', '/', '*']
    compList = ['>', '<', '=']
    tempList = ['.', '$', '#', '%', '&', '|', ' ','(',')']

    for i in opList:
        if op == i:
            return True
    for i in compList:
        if op == i:
            return True
    for i in tempList:
        if op == i:
            return True
def CheckState(state,value):
    if value == 'str':
        if state != '':
            return True
    if value == 'list':
        if len(state) > 0:
            return True
def Split(sent):
    lis = []
    lists = []
    str = ''
    for i in sent:
        if i == ';' or i == '\n':
            if CheckState(str,'str'):
                lis.append(str)
            if CheckState(lis,'list'):
                lists.append(lis)
            lis = []
            str = ''
            continue
        if operation(i):
            if CheckState(str,'str'):
                lis.append(str)
            if i != ' ':
                lis.append(i)
            str = ''
            continue
        str = str + i
    if CheckState(str,'str'):
        lis.append(str)
    if CheckState(lis,'list'):
        lists.append(lis)

    return lists
