import Split as sp
import Parser as prs
import mathExpr as ME

text = '''
X + y =100*65489-fsdahfj+76
x = c+4u
while (c>c( qb = fds+fgds
if (c>c) qb = fds+fgds
Q = x+y+n+5*9*y*u/u+i
'''

lists = sp.Split(text)

Res = prs.Parse(lists)

for i in range(len(lists)):
    print(lists[i],Res[i])

# text = 'x+y+n+5*9*y*u/u+i'
# lis = sp.Split(text)
# print (lis)
# print(ME.math_expr(lis[0]))
