# What will the following code print and why?
# Don't run it until you have tried to answer.

def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

# Will print `Hello World'. Calling inner() sets `inner_var` to 'World'
# but also looks for `outer_var` for the print() function, which can be
# accessed as it is in an outer scope.