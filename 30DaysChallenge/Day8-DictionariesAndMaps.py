n = int(input())
mydict = {}
for i in range(0, n):
    data = input().split(" ")
    key = data[0]
    value = data[1]
    mydict[key] = value

for i in range(0, n):
    key = input()
    if key in mydict:
        print(key+"="+mydict[key])
    else:
        print("Not found")
