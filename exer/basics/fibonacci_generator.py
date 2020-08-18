from performance import performance

@performance
def fib(number):
    MyGen = FibonacciGenerator(number)
    for i in MyGen:
        print(i)
        if i[0] == 5:
            print("it's 5!!")


class FibonacciGenerator():
    current_number = 0
    fib_number_current = 0
    fib_number_previous = 0

    def __init__(self, number):
        self.number = number
    
    def __iter__(self):
        return self
    
    def __next__(self):         
        try:
            if FibonacciGenerator.current_number == 0:
                # print(FibonacciGenerator.current_number, self.number)
                FibonacciGenerator.fib_number_current = 1
                return FibonacciGenerator.current_number,0
            elif FibonacciGenerator.current_number == 1:
                # print(FibonacciGenerator.current_number, self.number)
                return FibonacciGenerator.current_number,FibonacciGenerator.fib_number_current
            elif FibonacciGenerator.current_number <= self.number:
                # print(FibonacciGenerator.current_number, self.number)
                temp_number = FibonacciGenerator.fib_number_current
                FibonacciGenerator.fib_number_current = FibonacciGenerator.fib_number_current + FibonacciGenerator.fib_number_previous
                FibonacciGenerator.fib_number_previous = temp_number
                return FibonacciGenerator.current_number,FibonacciGenerator.fib_number_current
        finally:
            FibonacciGenerator.current_number += 1
        raise StopIteration


fib(20)