class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        maximumNumber = max(self.__elements)
        results = list()
        for i in self.__elements:
            results.append(abs(i - maximumNumber))
    
        self.maximumDifference = max(results)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
