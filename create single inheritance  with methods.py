class Demo:
    Branch = "AIML"

    def addition(self, a, b):
        print(a + b)

    def subtraction(self, a, b):
        print(a - b)

    def multiply(self, a, b):
        print(a * b)

# Creating an object of the Demo class
d1 = Demo()

# Calling the methods
d1.addition(10, 20)      # Output: 30
d1.subtraction(30, 10)   # Output: 20
d1.multiply(2, 10)       # Output: 20