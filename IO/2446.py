import sys
n=int(sys.stdin.readline())
for i in range(1,n+1):
    print(' '*(i-1),'*'*(2*(n-i+1)-1),sep='')
for i in range(2,n+1):
    print(' ' * (n-i), '*' * (2 *i- 1), sep='')
