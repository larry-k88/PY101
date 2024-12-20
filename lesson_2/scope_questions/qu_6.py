# What will the following code print and why?
# Don't run it until you have tried to answer.

def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

# Will print 'Inner 1: 25, then Inner 2: 15
# inner_func1() creates a new local variable x and assigns it to 25
# It then prints it
# inner_func2() tried to print x, but has no local variable, so it looks
# to an outer variable, the outer function - it cannot access a "sister"
# function, inner_func2(), but can access the "parent" function