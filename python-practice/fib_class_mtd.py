class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0 
        self.__num1 = self.__num2 = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in (1, 2):
            return 1
        res = self.__num1 + self.__num2
        self.__num1, self.__num2 = self.__num2, res
        return res
k = int(input("Enter the number of fibonacci you want to print: "))
obj = Fib(k)
for i in obj:
    print(i, end=' ')
