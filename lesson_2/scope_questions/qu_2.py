# What will the following code print and why?
# Don't run it until you have tried to answer.

num = 5

def my_func():
    num = 10

my_func()
print(num)

# Will print `5` as the `num` variable within my_func() is created in 
# the function scope only - it is assigned the value of 10 when the 
# function is called, but that value is not captured.
# When print() is called, it uses the initial assigned value of `num` 
# as the argument