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

```
print(2 + 3 * 4, 4 * (3 + 2))
```
> It will print '14, 20'
> It covers the concept of operator precedence. The 2 expressions,separated by a comma, are evaluated first, then their results are passed to the `print()` function where they are automatically converted into their string representation
> In the first expression, the `*` operator has precedence over the `+` operator - that is, the operands `3` and `4` bind more closely to their operator that the operands `2` and `3`. Therefore, we evaluate `3 * 4` to `12`, before adding `2`.
> In the second expression, the parentheses around `3 + 2` have a higher precedence so this is evaluated first. We therefore have `4 * 5` as our final expression to evaluate.
> In order to remove the space in the output, we can add a separator parameter after the expressions. The default separator is a space, so by refactoring to this, we change that separator to nothing:
> print(2 + 3 * 4, 4 * (3 + 2), sep='')  

### 5. What can be used in place of commas to make this more readable?

```
print(123112940)
```
> Underscores are used to make large (or small) numbers more readable. Commas cannot be used as they are used to separate arguments in the print function. The placement underscores can be used flexibly - that is, they can separate any numbers
> print(123_112_940) or print(12_31129_40)

## Strings

### Basic questions:
- Are strings mutable or immutable? 
> Immutable, anything that appear to re-assign a string is actually creating a new object
- Are strings primitive or non-primitive?
> Primitive
- Are strings literals?
> Yes, strings are recognised by the parser which an object can be created from
- What is a text sequence?
> It is a string of characters  
- What kind of characters are used in a string? 
> Unicode characters, of which ASCII characters are a subset
- Are text sequences the same as ordinary sequences?
> No, they only contain string characters and are immutable. Sequences can contain multiple objects of various types and some are mutable. The characters in a text sequence are strings of length 1. 

### 1. What is the output of this code, and why? What is the concept covered here?

```
str1 = "Hello, world!"
sub1 = str1[8:12]
print(sub1)
sub2 = str1[::-1]
print(sub2)
sub3 = str1[::2]
print(sub3)
```
> The text sequence "Hello, world!" is assigned to the variable `str1`
> We then create a new variable called `sub1` which is assigned to the slice of `str1` from index 8 to 11 (index notation includes the start value but excludes the stop value) - given that indexing starts from position 0, when `sub1` is passed to the `print()` function, the string representation "orld" is output
> Another variable `sub2` is then created and assigned to the a new object which is the reverse of `str1` - the `::-1` syntax in relation to strings creates a new reversed object (strings are immutable). This is then printed.
> A final variable `sub3` is created and is assigned to the value of a slice of `str1` - the start and stop has been omitted which defaults to the whole string, but the step value of 2 means the new object will contain every other character from the string.
> The output will be:
> 'orld'
> '!dlrow ,olleH'
> 'Hlo ol!'

### 2. What does this print and why? What concept is this?

```
print("Hello\nWorld")
```
> It will print:
> Hello
> World
> The `\n` is an escape character and Python inserts a line break at the position where it's printed

### 3. What does this print and why? What concept is this?

```
name = 'Alexander Graham Bell'
print(name[0])
```
> A
> This is example of the indexing syntax that text sequences support. Strings are ordered sequences of characters. Index numbers start at 0 in Python so when we index the 0th character in the string referenced by `name`, the character 'A' is passed as an argument to the `print()` function.

## f-strings

### Basic Questions:
- What are f-strings? 
> They are strings prefixed with an 'f' which enables formatting of the string and string interpolation using {}

### 1. What does this print and why, what is the concept?

```
name = 'Abraham Lincoln'
print(f"{name} was a President of the US")
```
> Abraham Lincoln was a President of the US
> The f prefix indicates that this is an f-string, or formatted string literal.
> The expression in curly braces (in this case, the variable `name`) is evaluated first its value (the string "Abraham Lincoln") is passed to the print function along with the rest of the string.
> Another option is the the `str.format()` method:
> print("{} was a President of the US".format(name))

## string methods

### Basic Questions:
- How do you identify a method versus a function?
> A function is invoked by typing its name, followed by its argument in parentheses 
> Methods are called on the object, followed by a `.` and the the function invocation

### 1. What does this print and why?

```
mashup = "thIs is How we type careLEssly"
cleaned = mashup.capitalize()
print(cleaned)
```
> This is how we type carelessly
> `mashup` is a variable which points to a string object. When the `capitalize()` method is called on the object, it returns a new string (strings are immutable) whose value is assigned to a new variable, called `cleaned`. The function itself returns the string but with the first character in uppercase and the rest in lowercase.
> We then pass this new object to the `print()` function

### 2. What do these print and why?

```
stuff = 'tHIS iS bACKWARDS'
str1 = stuff.swapcase()
str2 = stuff.upper()
str3 = stuff.lower()
print(stuff)
print(str1)
print(str2)
print(str3)
```
> tHIS iS bACKWARDS
> This Is Backwards
> THIS IS BACKWARDS
> this is backwards
> `stuff` points to a string object which is immutable. When we call the three methods on `stuff`, they return a new object whose value is captured by assigning it to a new variable. This happens because the string objects are immutable. These variables are then passed to the `print()` function and their respective values are displayed in their string representations.
> swapcase() swaps the case of each character in the string
> upper() makes every character uppercase
> lower() makes every character lowercase

### 3. What do these print and why?

```
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
> True
> False
> False
> False
> False
> True
> True
> True
> `is.alpha()` returns True is all characters in the string are alphabetic and there is at least one character
> The `all()` function returns True if all items in an iterable evaluate to Truthy. In this case, the argument passed to the `all()` function is a generator expression - the expression iterates over each word in words and evaluates `word.isalpha()`, which returns True or False based on whether the word contains only alphabetic characters. Here, as each of list items is alphabetic, each call to `isalpha()` returns True, meaning that the `all()` is passed an iterable where each element is True, therefore also returning True.

### 4. What does this print and why?

```
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
> Is 'HelloWorld' alphabetic? True
> Is '12345' alphabetic? False
> Is 'Hello World' alphabetic? False
> This produces the same and is more flexible:
> print("Is '{}' alphabetic? {}".format(string1, result1))

### 5. What do these print and why?

```
s1 = "123abc"
print(s1.isdigit())
s2 = "123$%^"
print(s2.isdigit())
s3 = ""
print(s3.isdigit())
s4 = "12345"
print(s4.isdigit())
```
> False
> False
> False
> True

### 6. What do these print and why?

```
print("Hello World".isalnum())
print("Hello@World".isalnum())
print("".isalnum())
print("Hello123".isalnum())
```
> False
> False
> False
> True

### 7. What do these print and why?

```
name = 'HELLO'

if name.isupper():
    print("WORLD")
else:
    print("world")
```
> WORLD

###  8. What do these print and why?
```
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
> This is all caps
> This is all lowercase
> Neither

### 9. What do these print and why?

```
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
> True
> False
> False
> Number of words in the sentence: 5
> `.split()` function splits, by default, at whitespace. It also treats consecutive spaces as a single delimiter and removes all leading/trailing whitespace.

### 10. What do these print and why?

```
s = "   Hello, World!   "
print(s.strip())
print(s.strip(" !"))
```
> Hello, World!
> Hello, World
> It only strips leading/trailing characters (it leaves the space between the words)

### 11. What do these print and why?

```
s = "www.example.com"
print(s.lstrip('wcmo.'))
```
> example.com


### 12. What do these print and why?

```
s = 'impatient'
print(s.rstrip('tp'))
print(s.rstrip('p'))
```
> impatien
> impatient

### 13. What do these print and why?

```
s = "Hello, World!"
print(s.replace("Hello", "Hi"))
print(s.replace("o", "0"))
```
> Hi, World!
> Hell0, W0rld!

### 14. What do these print and why?

```
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
> ['This', 'is', 'a', 'sample', 'sentence.']
> ['John', 'Doe', '30', 'New York']
> ['This', 'is', 'a sample sentence']
> Last one splits only 2 times, resulting in 3 elements

### 15. What does this print and why?

```
str1 = "hello world"
str2 = str1.capitalize()
print("Original string:", str1)
print("Capitalized string:", str2)
```
> Original string: hello world
> Capitalized string: Hello World

## boolean vs. truthiness

### Basic Question:
- In Python, what values are considered Falsy and what are considered Truthy?
> Falsy values are those which evaluate to False when passed to the `bool()` built-in function. Examples are: None, any numeric value representing 0, empty sequence/collections, False

### 1. What do these print and why?

```
truthy_values = [1, 2, 3, "hello", [1, 2, 3], {"a": 1}, True, 0, "", [], {}, None, False]

print(“Values:”)
for value in truthy_values:
    if value:
        print(f"{value} is truthy")
    else:
        print(f"{value} is falsy")
```
> Values:
> 1 is truthy
> 2 is truthy
> 3 is truthy
> hello is truthy
> [1, 2, 3] is truthy
> {'a' : 1} is truthy
> True is truthy
> 0 is falsy
>  is falsy
> [] is falsy
> {} is falsy
> None is falsy
> False is falsy
> NB quotes around strings are left out when using the print function, even for an empty string

### 2. What do these print and why?

```
x = 5
y = 10
z = 15

print(x > 0 and y < 20)
print(not x == y)
print(x < y and y < z)
print(x > y or y > z)
print(not (x > y))
```
> True
> True
> True
> False
> True
> No short-circuiting in any of these

### 3. What do these print and why?

```
a = 10
b = 20

print(a < b < 30)
print(a > b or b == 20)
print(b == 20 or a > b)
```
> True
> True
> True (this one short-circuits)

### 4. What do these print and why?

```
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)
print(6 not in my_list)
```
> True
> True

### 5. What do these print and why?

```
temperature = 25
time_of_day = "morning"

if temperature < 30 and (time_of_day == "morning" or time_of_day == "afternoon"):
    print("It's a pleasant day!")
else:
    print("It's either too hot or not the right time of day.")
```
> It's a pleasant day

### 6. What does this print and why?

```
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
> Hello 2
> No number will return "Hello"

## ranges

### Basic questions:
- Is a range primitive or non-primitive?
> Non-primitive
- Is a range mutable or immutable?
> Immutable - once created, they cannot be modified
- Does range have a literal form or a type constructor?
> Type constructor `range()`
- Is a range a sequence or a collection?
> Sequence
- What is the most common use of the range datatype?
> Providing a finite limit of iterations for loops
- Are ranges homogenous or heterogeneous?
> Homogeneous - they contain only integer types
- Why are ranges considered lazy?
> The only integers stored by Python, until the constructor function is called, are the start, stop and step parameters. The values in the range are not stored in memory (more efficient for large ranges)

### 1. What do these print and why? What concept does this demonstrate?

```		
print(range(0,10))
print(len(range(5, 15)))
print(my_range[1])
print(str(range(3, 7)))
print(list(range(12, 8, -1)))
print(list(range(5, 5, 1)))
print(5 in range(5))
print(5 not in range(5, 10))
```
> range(0, 10) - lazy sequence
> 10
> Error - my_range not defined. Ranges are indexable if defined - they are sequences
> range(3, 7)
> [12, 11, 10, 9]
> []
> False
> False

### 2. What does this code print and why? What concept does this demonstrate?

```
example = range(0)
if example:
    print(list(example))
else:
    print(example)
```
>`range(0)` is a falsy value. Python is able to check the length of the range generator expression before it generates (or tried to generate) its values.
> The `else` block executes, printing the range object `range(0)`

### 3. What does this code print and why? What concept does this demonstrate?

```
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
> 0 is between 0 and 50
> 25 in between 0 and 50
> `n` is a local variable that is used in pattern matching.
> Alternative is to use `case _ if number < 0`

## list and dictionary syntax

### Basic Questions
- What categories are lists and dictionaries?
> Lists are sequences, dictionaries are mappings
- Are they mutable or immutable?
> Mutable
- Are they primitive or non-primitive?
> Both non-primitive
- Are they literals, or do they require type constructors?
> Lists can be literals `[1, 2, 3]` or type constructors: `list((1, 2, 3))`
- Are they sequences?
> Lists are sequences - they are ordered and therefore support indexing syntax. Dictionaries preserve insertion order and are indexing by the key (not position)
- Does the order of the elements in both matter?
> The order is a list is essential for many list operations, such as indexing. Since Python 3.7, dictionaries maintain insertion order.

## list methods: len(list), list.append(), list.pop(), list.reverse()

### 1. What does this print and why?

```
my_list = [1, 2, 3, 4, 5]
length_of_list = len(my_list)
print("Length of the list:", length_of_list)
```
> Length of the list: 5
> A variable named `my_list` is created and assigned to a list object `[1, 2, 3, 4, 5]`
> The `len()` function takes one argument and returns the number of items in that object. In this case, it returns the number of items (the length) of the list object. That value is assigned to a new variable `length_of_list`.
> The value of the `length_of_list` variable is passed to the `print()` function, along with a string. The `print()` function automatically converts any non-string expressions (here, the integer 5) to a string to be displayed to the user
* This has the same output and is more concise and reduces the number of single-use variables. However, the original is better for debugging, and also if the variable is re-used elsewhere in the program
```
my_list = [1, 2, 3, 4, 5]
print("Length of the list:", len(my_list))
```

### 2. What does this print and why?

```
lst_one = [0, 1, 2, 3]
lst_two = lst_one.append(4)
if lst_two:
    print(lst_two)
else:
    print(lst_one)
```
> The `append()` function is mutating (modifies in-place, or 'destructive'). The variable `lst_one` is assigned to a list object `[0, 1, 2, 3]`. The return value of the `append()` function is `None` and that value is therefore assigned to a new variable `lst_two`.
> The `if` block will run if `lst_two` is a truthy value, which is it not. The `else` block is therefore executed, printing the string representation of the object referenced by `lst_one` - in this case, the mutated list `[0, 1, 2, 3, 4]`
* Python passes the reference to the object when we call `append()`, not the object itself. The mutability of that object dictates whether the original object is modified.

### 3. What does this print and why?

```
my_list = [1, 2, 3, 4, 5]
ele = my_list.pop()
print("Popped element:", ele)
print("List after popping:", my_list)
ele1 = my_list.pop(1)
print("Popped element at index 1:", ele1)
print("Modified list after popping at index 1:", my_list)
```
> A variable `my_list` is assigned to the list object `[1, 2, 3, 4, 5]`
> Another variable is created and assigned to the return value of the `pop()` method being called on the list object, which is `5`. As lists are mutable, the object is modified in-place (mutated).
> The `print()` function is then called on a string and the variable `ele` - the variable is evaluated first and its string representation is displayed: 'Popped element: 5'
> The `print()` function is then called again on a string and the variable `my_list` - the variable is evaluated first and its string representation is displayed: 'List after popping: [1, 2, 3, 4]' 
> A further variable `ele1` is created and assigned the return value of calling the `pop(1)` method on the, now modified, list object. The function retrieves and returns the element at index 1, which is the integer 2 (indexing starts at zero)
> Two more string representations are printed:
> Popped element at index 1: 2
> Modified list after popping at index 1: [1, 3, 4]
* If using string concatenation (as opposed to commas) in the `print()` statements, explicit coercion to strings is required: `print("Popped element:" + str(ele))`

### 4. What does this print and why?

```
elements = [0, 1 , 2, "Dima"]
print(elements.reverse())
print(elements)
```
> A variable `elements` is created and assigned to a list object which contains integer and string elements. The list object itself is mutable but the integers and strings within are immutable.
> The `reverse()` method is called on the list object which mutates the object, in this case reversing the order of the elements (lists are sequences so order is important). The return value of calling the method would be `None`, and this is the value that is passed to the `print()` function
> When the `print()` function is called on the object, it will display the mutated object: `["Dima", 2, 1, 0]`
* To reverse a list without mutating/modifying the original, use `reversed()` function or slicing (`[::-1]`):
* `print(elements[::-1])` or `print(list(reversed(elements)))`

### 5. What does this print and why?

```
ages = {
    "dimo": 31,
    "olena": 32,
    "tetiana": 28
}

def get_val_of_dimo(info):
    try:
        # info['dimo']
        return info['dimo']
    except KeyError:
        return "Typo"

print(get_val_of_dimo(ages))
```
> A dictionary object is created which contains 3 key/value pairs - the dictionary is mutable but the actual keys and value are strings/integers and therefore immutable
> A function is defined which handles exceptions: the line of code that may raise an error is `return info['dimo']` - this will raise a KeyError if the key (in square brackets) is not in the dictionary (`info`)
> If no error is raised (i.e. the key is in the dictionary), the value associated with the key is returned
> If the error is raised, it is caught and handled by the `except` block which returns the string "Typo"
> When we pass the dictionary into the function, the key 'dimo' exists and therefore we see the string representation of the integer 31 as the output
> I do not know what the purpose of `info['dimo']` line - please can you elaborate?
* commented out line not needed
* Better overall to use the `.get()` method:
```
def get_val_of_dimo(info):
    return info.get('dimo', "Typo")
```

### 6. What does this print and why?

```
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys = my_dict.keys()
print(keys)
for key in keys:
    print(key)
```
> 

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
