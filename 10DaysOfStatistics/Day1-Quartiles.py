# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics

n = int(input())
X = [int(i) for i in input().split()]
X = sorted(X)
if(n % 2 == 0):
    X1 = [X[i] for i in range(0, int(n/2))]
    X3 = [X[i] for i in range(int(n/2), n)]
else:
    X1 = [X[i] for i in range(0, (int((n+1)/2)) - 1)]
    X3 = [X[i] for i in range(int(((n+1)/2)), n)]

Q1 = int(statistics.median(X1))
Q2 = int(statistics.median(X))
Q3 = int(statistics.median(X3))
print(Q1)
print(Q2)
print(Q3)
