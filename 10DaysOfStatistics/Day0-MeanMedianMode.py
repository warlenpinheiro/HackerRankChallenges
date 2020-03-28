# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
from collections import Counter

n = int(input())
vet = input().split()
numbers = [int(i) for i in vet]

mean = statistics.mean(numbers)
mode = Counter(sorted(numbers))
mode = mode.most_common(1)[0]
median = statistics.median(numbers)

print(mean)
print(median)
print(mode[0])
