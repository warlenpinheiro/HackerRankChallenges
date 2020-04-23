import sys

n = int(input())
mydict = dict()
for _ in range(0, n):
    key, value = input().split(" ")
    mydict[key] = value

key = sys.stdin.readline().strip()
while key:
    if key in mydict:
        print(key+"="+mydict[key])
    else:
        print("Not found")
    key = sys.stdin.readline().strip()
