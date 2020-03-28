# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
numbers = input().split()
weight = input().split()
numbers = [int(i) for i in numbers]
weight = [int (i) for i in weight]
soma = 0
mean = 0

for index, i in enumerate(numbers):
    mean += (i * weight[index])
    soma += weight[index]

mean = round((mean / soma), 1)
print(mean)
