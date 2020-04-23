# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
words = []

for i in range(0, n):
    words.append(input())

for word in words:
    evens = []
    odds = []
    for index in range(len(word)):
        if index == 0:
            evens.append(word[index])
        elif index % 2 == 0:
            evens.append(word[index])
        else:
            odds.append(word[index])
    print(''.join(evens), ''.join(odds))
