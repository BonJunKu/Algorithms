import sys
n=int(sys.stdin.readline())
for i in range(1,n+1):
    print('*'*i,' '*2*(n-i),'*'*i,sep='')
for i in range(1,n):
    print('*'*(n-i),' '*i*2,'*'*(n-i),sep='')
