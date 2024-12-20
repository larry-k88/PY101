# What will the following code print and why?
# Don't run it until you have tried to answer.

num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

# Will print '10' - global keyword enables the function to not only 
# access the original variable, but reassign it too
# When the function runs, instead of creating a new `num` variable, 
# it reassigns the value of the original from 5 to 10, so when print()
# is invoked using `num` as the argument, the new reassigned value is 
# printed