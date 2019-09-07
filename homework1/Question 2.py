# x=1 is a global variable. This is a global variable because it is not declared inside def test.
x=1
# def test is a function.
def test():
# global x is a global variable. It is declared in the function test. 
    global x
# x=2 is a global variable, x has a value of 2. It is within test function.
    x=2
# test() function is being called below.
test()
# print(x) will print the value 2  because the test function is called and x becomes 2. 
print(x)