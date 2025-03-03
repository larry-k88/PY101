## Type coercions: explicit (e.g., using int(), str() and implicit)

### 1: Which variable is coerced? Is it implicit or explicit coercion?

```
x = 3.5
y = 5
z = x + y
```
> Variable `x` is created and assigned the float value of 3.5. Another variable `y` is created and assigned the integer value of 5.
> A third variable `z` is created and assigned the value of the expression `x + y`. 
> Python's arithmetic operators will coerce the data types of their operands if required. In this case, the addition operator must have both operands of the same data type. We currently have a float and an integer but Python implicitly coerces `y` into a float (`5` to `5.0`) so its data types matches that of `x`. The expression is then evaluated, resulting in `z` being assigned the value of `8.5` - a float.
> This can be confirmed by checking the data type of `z` using type(z).
> It is implicit coercion as we haven't specifically asked Python to change a data type.
* It is an example of Python automatic type conversion

### 2: What coercion is happening here? Is it implicit or explicit?

```
a = 1
b = 2
print(a + b)
```
> Variable `a` is created and assigned the integer value of 1. Another variable `b` is created and assigned the integer value of 2.
> The expression `a + b` is then evaluated first before its result is passed to the `print()` built-in function as an argument.
> As `a` and `b` are both of the same data type (integers), there is no coercion required - the expression evaluates to the integer value of `3`, which is passed to `print()`
> The `print()` function returns `None`, but displays an output to the use via the terminal. The output is implicitly coerced to a string data type to make it more reader-friendly.
> The program will output the string '3'.
* Output will be displayed without the quotes but is a string
* `print()` automatically converts its arguments to string representation for display

### 3: What coercion is happening here? Is it implicit or explicit?

```
month = "December"
day = int(input("What day is it? "))
print(f"Today is the {day} of {month}")
```
> A variable `month` is created and assigned the string value of 'December'. A variable called `day` is created which is assigned the value of the expression on the right hand side. This expression uses the built-in `input()` function to get some data from the user - in this case, the prompt "What day is it? " is displayed to the user and they can type their input. The `int()` built-in function explicitly coerces the user input into an integer (from a string). This integer is the value assigned to the variable `day`
> The built-in `print()` function then automatically converts its arguments to strings for display purposes, an example of implicit coercion. In this case, the argument is an 'f-string', or 'formatting string literal'. This is a way to interpolate expressions and include them in the string that is output. 
* The f-string firstly evaluates the expressions inside the {}.
* Then it automatically converts the `day` integer to its string representation for interpolation (a special type of implicit coercion) - these take the place of the placeholders in the f-string.
* The whole string is then passed to `print()`
* `print()` isn't considered coercion - it doesn't return the resulting strings, it just displays them

## Numbers, including handling exceptions (ValueError, ZeroDivisionError)

### Basic questions:
- Are integers and floats mutable or immutable? 
> Both integers and floats are immutable data types in Python - this means they cannot be changed once created. Anything that appears to change them are actually creating a new object. Integers are whole numbers without any fractional competent. Floats are numbers with a decimal point.
- Are integers and floats primitive or non-primitive?
> They are primitive data types, otherwise known as basic or fundamental. Other types are Booleans and Strings
- Are integers and floats literals?
> Yes. 
- What is a literal?
> A literal is something that the parser can recognise and create an object from. It is notation for representing a fixed value

### 1: What does this return and why? What concept does this cover?

```
def convert_to_int(string):
    try:
        converted_integer = int(string)
        return converted_integer
    except ValueError:
        return "That string cannot be converted to an integer"

print(convert_to_int("hello"))

print(convert_to_int("5"))
```
> The function is defined on Line 1: it takes a string as an argument and tries to explicitly coerce it into an integer.
> If no errors are raised, the function returns that coerced integer.
> If a ValueError is raised (i.e. the argument is not numeric), the return value will be the string on Line 6.
> When the print statement on Line 8 is executed, the string 'hello' is passed to the function. As it is not a numeric string, the built-in function `int()` will raise a Value Error - this will result in the code in the `except` block executed.
> When the print statement on Line 10 is run, the numeric string '5' will be coerced to the integer value 5.
> Both these return value are passed to the `print()` function which automatically convert any non-string arguments into string representations for display purposes.
> Concepts include: exception handling, implicit/explicit coercion, ValueErrors, built-in functions

### 2: What does this return and why? What concept does this cover?

```
def division(number1, number2):
    numerator = number1
    denominator = number2

    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "The denominator cannot be zero"

print(division(5, 0))
```
> The function is defined and takes 2 arguments - they are then assigned to two variables which are within the functions scope.
> A try block is executed which divides one of the arguments by the other. If no error is raised, the value of expression (a float, due to the division operator) will be returned from the function.
> If a ZeroDivisionError is raised, the string on Line 9 is returned instead.
> These return values are then passed as arguments into the `print()` function which automatically converts non-string arguments into string representation for display purposes.
> In this case, the output will be "The denominator cannot be zero"
> This snippet covers the `/` operator (floating-point division - not implicit coercion), exception handling, built-in functions and ZeroDivisionErrors.

### 3: What does this print and why, what concept does this demonstrate?

```
def addition(number1, number2):
    number1 += number2

x = 1
y = 2

addition(x, y)
print(f"x is {x}, y is {y}")
```
> The function is defined in Line 1 and takes 2 arguments. The augmented assignment operator is used to assign the value of the expression `number1 + number2` to the variable called `number1`. There is no return value to this function (by default, it will return `None`)
> Outside the function, two variables are created and assigned integer values. These values are passed into the function when it is called on Line 7. 
> The `print()` function on Line 8 contains an f-string. Python will evaluate the expressions in the curly braces and the result of the expression will be interpolated into the string. This string is then passed to the `print()` function with automatically converts any non-string argument into a string representation for display purposes.
> The output here will be "x is 1, y is 2". The function definition and invocation have no impact on the output in this case.
> This demonstrates the immutability of integers - when an immutable object is passed to a function, any changes to the parameter inside the function don't affect the variable outside the function. In this case, `number1` is reassigned using the `+=` operator (it is originally initialised as `x` on Line 7, but is reassigned to `3` on Line 2.) This does not change the value of `x` in the global scope.

### 4. What does this print and why? What concept does this cover? How would you refactor this to remove the space?

```python
print(2 + 3 * 4, 4 * (3 + 2))
```


### 5. What can be used in place of commas to make this more readable?

```python
print(123112940)
```

## Strings

### Basic questions:
- Are strings mutable or immutable? (Immutable)
- Are strings primitive or non-primitive? (Primitive)
- Are strings literals? (Literals)
- What is a text sequence? (strings of characters)
- What kind of characters are used in a string? (Unicode characters)
- Are text sequences the same as ordinary sequences? (No, text sequence contain only string characters. ordinary sequences refer to any other sequence types that store multiple elements (e.g. lists, tuples, ranges))

### 1. What is the output of this code, and why? What is the concept covered here?

```python
str1 = "Hello, world!"
sub1 = str1[8:12]
print(sub1)
sub2 = str1[::-1]
print(sub2)
sub3 = str1[::2]
print(sub3)
```


### 2. What does this print and why? What concept is this?

```python
print("Hello\nWorld")
```


### 3. What does this print and why? What concept is this?

```python
name = 'Alexander Graham Bell'
print(name[0])
```


## f-strings

### Basic Questions:
- What are f-strings? (string prefix for defining formatted string literals that enables string interpolation)

### 1. What does this print and why, what is the concept?

```python
name = 'Abraham Lincoln'
print(f"{name} was a President of the US")
```


## string methods

### Basic Questions:
- How do you identify a method versus a function?

### 1. What does this print and why?

```python
mashup = "thIs is How we type careLEssly"
cleaned = mashup.capitalize()
print(cleaned)
```

### 2. What do these print and why?

```python
stuff = 'tHIS iS bACKWARDS'
str1 = stuff.swapcase()
str2 = stuff.upper()
str3 = stuff.lower()
print(stuff)
print(str1)
print(str2)
print(str3)
```

### 3. What do these print and why?

```python
s1 = "Hello"
print(s1.isalpha())
s2 = "Hello World"
print(s2.isalpha())
s3 = "Hello!"
print(s3.isalpha())
s4 = "Hello123"
print(s4.isalpha())
s5 = ""
print(s5.isalpha())
s6 = "こんにちは"
print(s6.isalpha())
s7 = "HelloWorld"
print(s7.isalpha())
words = ["apple", "banana", "cherry"]
print(all(word.isalpha() for word in words))
```

### 4. What does this print and why?

```python
string1 = "HelloWorld"
string2 = "12345"
string3 = "Hello World"

result1 = string1.isalpha()
result2 = string2.isalpha()
result3 = string3.isalpha()

print("Is '{}' alphabetic?".format(string1), result1)
print("Is '{}' alphabetic?".format(string2), result2)
print("Is '{}' alphabetic?".format(string3), result3)
```

### 5. What do these print and why?

```python
s1 = "123abc"
print(s1.isdigit())
s2 = "123$%^"
print(s2.isdigit())
s3 = ""
print(s3.isdigit())
s4 = "12345"
print(s4.isdigit())
```

### 6. What do these print and why?

```python
print("Hello World".isalnum())
print("Hello@World".isalnum())
print("".isalnum())
print("Hello123".isalnum())
```

### 7. What do these print and why?

```python
name = 'HELLO'

if name.isupper():
    print("WORLD")
else:
    print("world")
    ```

###  8. What do these print and why?
```python
def punctuation_type(str):
    if str == str.upper():
        print('This is all caps')
    elif str == str.lower():
        print('This is all lowercase')
    else:
        print('Neither')

str1 = 'HELLO'
str2 = 'yolo'
str3 = 'My Name Is: '

punctuation_type(str1)
punctuation_type(str2)
punctuation_type(str3)
```

### 9. What do these print and why?

```python
str1 = "    "
str2 = "  Hello   "
str3 = "Hello World"

print(str1.isspace())
print(str2.isspace())
print(str3.isspace())

sentence = "Hello     World!   How are you?   "
word_count = sum(1 for word in sentence.split() if not word.isspace())
print("Number of words in the sentence:", word_count)
```

### 10. What do these print and why?

```python
s = "   Hello, World!   "
print(s.strip())
print(s.strip(" !"))
```

### 11. What do these print and why?

```python
s = "www.example.com"
print(s.lstrip('wcmo.'))
```

### 12. What do these print and why?

```python
s = 'impatient'
print(s.rstrip('tp'))
print(s.rstrip('p'))
```

### 13. What do these print and why?

```python
s = "Hello, World!"
print(s.replace("Hello", "Hi"))
print(s.replace("o", "0"))
```

### 14. What do these print and why?

```python
sentence = "This is a sample sentence."
words = sentence.split()
print(words)

csv_data = "John,Doe,30,New York"
fields = csv_data.split(",")
print(fields)

sentence = "This is a sample sentence."
words = sentence.split(maxsplit=2)
print(words)
```

### 15. What does this print and why?

```python
str1 = "hello world"
str2 = str1.capitalize()
print("Original string:", str1)
print("Capitalized string:", str2)
```

## boolean vs. truthiness

### Basic Question:
- In Python, what values are considered Falsy and what are considered Truthy?

### 1. What do these print and why?

```python
truthy_values = [1, 2, 3, "hello", [1, 2, 3], {"a": 1}, True, 0, "", [], {}, None, False]

print(“Values:”)
for value in truthy_values:
    if value:
        print(f"{value} is truthy")
    else:
        print(f"{value} is falsy")
```

### 2. What do these print and why?

```python
x = 5
y = 10
z = 15

print(x > 0 and y < 20)
print(not x == y)
print(x < y and y < z)
print(x > y or y > z)
print(not (x > y))
```

### 3. What do these print and why?

```python
a = 10
b = 20

print(a < b < 30)
print(a > b or b == 20)
```

### 4. What do these print and why?

```python
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)
print(6 not in my_list)
```

### 5. What do these print and why?

```python
temperature = 25
time_of_day = "morning"

if temperature < 30 and (time_of_day == "morning" or time_of_day == "afternoon"):
    print("It's a pleasant day!")
else:
    print("It's either too hot or not the right time of day.")
```

### 6. What does this print and why?

```python
num = 12

if num / 3 < 3 and num > 10:
    print("Hello")
elif num >= 8 and num < 6 or num > 4 and num < 16:
    print("Hello 2")
elif num % 4 == 0 or num < 7 and num < 10:
    print("Hello 3")
else:
    print("Buy")
```

## ranges

### asic questions:
- Is a range primitive or non-primitive?
- Is a range mutable or immutable?
- Does range have a literal form or a type constructor?
- Is a range a sequence or a collection?
- What is the most common use of the range datatype?
- Are ranges homogenous or heterogeneous?
- Why are ranges considered lazy?

### 1. What do these print and why? What concept does this demonstrate?

```python		
print(range(0,10))
print(len(range(5, 15)))
print(my_range[1])
print(str(range(3, 7)))
print(list(range(12, 8, -1)))
print(list(range(5, 5, 1)))
print(5 in range(5))
print(5 not in range(5, 10))
```

### 2. What does this code print and why? What concept does this demonstrate?

```python
example = range(0)
if example:
    print(list(example))
else:
    print(example)
```

### 3. What does this code print and why? What concept does this demonstrate?

```python
def number_range(number):
    match number:
        case n if n < 0:
            print(f'{number} is less than 0')
        case n if n <= 50:
            print(f'{number} is between 0 and 50')
        case n if 50 < n <= 100:
            print(f'{number} is between 51 and 100')
        case _:
            print(f'{number} is greater than 100')
number_range(0)
number_range(25)
```

## list and dictionary syntax

### Basic Questions
- What categories are lists and dictionaries?
- Are they mutable or immutable?
- Are they primitive or non-primitve?
- Are they literals, or do they require type constructors?
- Are they sequences?
- Does the order of the elements in both matter?

## list methods: len(list), list.append(), list.pop(), list.reverse()

### 1. What does this print and why?

```python
my_list = [1, 2, 3, 4, 5]
length_of_list = len(my_list)
print("Length of the list:", length_of_list)
```

### 2. What does this print and why?

```python
lst_one = [0, 1, 2, 3]
lst_two = lst_one.append(4)
if lst_two:
    print(lst_two)
else:
    print(lst_one)
```

### 3. What does this print and why?

```python
my_list = [1, 2, 3, 4, 5]
ele = my_list.pop()
print("Popped element:", ele)
print("List after popping:", my_list)
ele1 = my_list.pop(1)
print("Popped element at index 1:", ele1)
print("Modified list after popping at index 1:", my_list)
```

### 4. What does this print and why?

```python
elements = [0, 1 , 2, "Dima"]
print(elements.reverse())
print(elements)
```

### 5. What does this print and why?

```python
ages = {
    "dimo": 31,
    "olena": 32,
    "tetiana": 28
}

def get_val_of_dimo(info):
    try:
        info['dimo']
        return info['dimo']
    except KeyError:
        return "Typo"

print(get_val_of_dimo(ages))
```

### 6. What does this print and why?

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
print(keys)
for key in keys:
    print(key)
```

### 7. What does this print and why?

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()
print(values)
for value in values:
    print(value)
```

### 8. What does this print and why?

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print(items)
for key, value in items:
    print(key, value)
```

## variable scope, global keyword, variables as pointers, variable shadowing

### 1. What does this print and why?

```python
name = 'John'

def greet():
    print(f"Hello, {name}!")

greet()
```

### 2. What does this print and why?

```python
def assign():
    var = 20
    print(var)

assign()
```

### 3. What does this print and why?
```python
try:
    print(var)
except NameError as e:
    print("Error occurred")
```

### 4. What does this print and why?

```python
var = 10

def function1():
    var = 20
    print(var)

function1()

try:
    print(var)
except NameError:
    print("Error occurred")

def function2():
    var += 5
    print(var)

try:
    function2()
except UnboundLocalError:
    print("Error occurred")

def function3():
    global var
    var += 5
    print(var)

function3()
print(var)
```

### 5. What does this print and why?

```python
var = 10

def function1():
    print(var)

function1()

def function2():
    var = 20
    print(var)

function2()
print(var)
```

### 6. What does this print and why?

```python
def function1():
    x = 10

    def function2():
        y = 20
        print(x)

    function2()
    print(x)

function1()
print(x)
print(y)
```

### 7. What does this print and why?

```python
var = 10

def access():
    print(var)
```
