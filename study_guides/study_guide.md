# Study Guide for PY109

- [Study Guide for PY109](#study-guide-for-py109)
  - [naming conventions: legal vs. idiomatic, illegal vs. non-idiomatic](#naming-conventions-legal-vs-idiomatic-illegal-vs-non-idiomatic)
  - [type coercions: explicit (e.g. using int(), str()) and implicit](#type-coercions-explicit-eg-using-int-str-and-implicit)
  - [numbers](#numbers)
  - [strings](#strings)
  - [f-strings](#f-strings)
  - [string methods](#string-methods)
    - [capitalize, swapcase, upper, lower](#capitalize-swapcase-upper-lower)
    - [isalpha, isdigit, isalnum, islower, isupper, isspace](#isalpha-isdigit-isalnum-islower-isupper-isspace)
    - [strip, rstrip, lstrip, replace](#strip-rstrip-lstrip-replace)
    - [split, find, rfind](#split-find-rfind)
  - [boolean vs. truthiness](#boolean-vs-truthiness)
  - [None](#none)
  - [ranges](#ranges)
  - [list and dictionary syntax](#list-and-dictionary-syntax)
  - [list methods: len(list), list.append(), list.pop(), list.reverse()](#list-methods-lenlist-listappend-listpop-listreverse)
  - [dictionary methods: dict.keys(), dict.values(), dict.items(), dict.get()](#dictionary-methods-dictkeys-dictvalues-dictitems-dictget)
  - [slicing (strings, lists, tuples)](#slicing-strings-lists-tuples)
  - [operators](#operators)
    - [Arithmetic: +, -, \*, /, //, %, \*\*](#arithmetic--------)
    - [String operators: +](#string-operators-)
    - [List operators: +](#list-operators-)
    - [Comparison: ==, !=, \<, \>, \<=, \>=](#comparison------)
    - [Logical: and, or, not](#logical-and-or-not)
    - [Identity: is, is not](#identity-is-is-not)
    - [operator precedence](#operator-precedence)
  - [mutability and immutability](#mutability-and-immutability)
  - [pass by object reference](#pass-by-object-reference)
  - [variables](#variables)
    - [naming conventions](#naming-conventions)
    - [initialization, assignment, and reassignment](#initialization-assignment-and-reassignment)
    - [scope](#scope)
    - [global keyword](#global-keyword)
    - [variables as pointers](#variables-as-pointers)
    - [variable shadowing](#variable-shadowing)
  - [conditionals and loops](#conditionals-and-loops)
    - [for](#for)
    - [while](#while)
  - [print() and input()](#print-and-input)
  - [exceptions (when they will occur and how to handle them)](#exceptions-when-they-will-occur-and-how-to-handle-them)
  - [Functions:](#functions)
    - [definitions and calls](#definitions-and-calls)
    - [return values](#return-values)
    - [parameters vs. arguments](#parameters-vs-arguments)
    - [nested functions](#nested-functions)
    - [output vs. return values, side effects](#output-vs-return-values-side-effects)
  - [expressions and statements](#expressions-and-statements)


## naming conventions: legal vs. idiomatic, illegal vs. non-idiomatic

+ Idiomatic - follow convention (PEP8)
+ Non-Idiomatic - don't follow convention (but still valid)
+ Illegal (invalid) - throw an error or do something unexpected

+ General Conventions for all **identifiers** (except Constants and Classes):
  + 'snake_case': lowercase letters, digits and underscores
  + start with a letter, separate words with underscores
  + __ (double underscore) has a special meaning
  + letters and digits must be from standard ASCII (7-bit)
    + NB 8-bit ASCII is 'extended ASCII' and Unicode is variable 8-bit. 16-bit or 32-bit 
  
+ Constants: 
  + SCREAMING_SNAKE_CASE: uppercase letters, digits and underscores
  + same other rules as above
  + Python doesn't differentiate constants and variables - this is an advisory naming convention
  
+ Classes:
  + PascalCase (similar to camelCase which just doesn't have first word capitalised): uppercase and lowercase and digits
  + Capitalise each word (no underscores)

+ To be a valid (legal) name:
  + Letters, digits, underscores from Extended ASCII (8-bit) and Unicode
  + No punctuation, special characters (most) or whitespace
  + Cannot start with a digit
  + Cannot use Python's reserved words e.g. `if`, `def`, `while`, `pass`
  
+ NB non-idiomatic names can still be legal - best to avoid
  + e.g. fourPieceSuit (camelCase) - legal but not convention
+ Not all illegal names will throw an error:
  
        first,last = ['Bill', 'Ben'] # illegal as it contains punctuation
    + creates 2 variables rather that one called 'first,last'

## type coercions: explicit (e.g. using int(), str()) and implicit

+ Built-in Data Types:  
a) Table Format
    
| Data Type	   | Class	   | Category	    | Kind	        | Mutable |
| :------------| :-------- |:---------------| :-------------|:--------|
| integers	   | int	   | numerics	    | Primitive	    | No      |
| floats	    | float      | numerics	      | Primitive	  | No      |
| boolean	   | bool	   | booleans	    | Primitive	    | No      |
| strings	   | str	   | text sequences	| Primitive	    | No      |
| ranges	   | range	   | sequences	    | Non-primitive	| No      |
| tuples	   | tuple	   | sequences	    | Non-primitive	| No      |
| lists	       | list	   | sequences	    | Non-primitive	| Yes     |
| dictionaries | dict	   | mappings	    | Non-primitive	| Yes     |
| sets	       | set	   | sets	        | Non-primitive	| Yes     |
| frozen sets  | frozenset | sets	        | Non-primitive	| No      |
| functions	   | function  | functions	    | Non-primitive	| Yes     |
| NoneType	   | NoneType  | nulls	        | --?--	        | No      |

b) Tree format:
+ Primitive Types **(all immutable)**
  + Numeric Types
    - int (integer)
    - float (floating-point)
  + Boolean Type
    - bool (Boolean)
  - Text Sequence Type
    - str (string)
+ Non-Primitive Types (**all immutable except as shown**)
  + Collections
    + Sequences
      - list (**mutable**)
      - tuple
      - range
     + Mappings
        - dict (**mutable**)
     + Sets
        - set (**mutable**)
        - frozenset
  + Other Non-Primitive Types
    + NoneType (None)
    + functions (**mutable**)

+ Coercion is the act of changing one data type into another (if is has to be specified, it's 'explicit' coercion)
+ String to number:
  + `int` and `float` (to integer and float respectively)
+ Number to string:
  + `str` (used to change most types to a string)

+ Implicit coercion performs it without specifying it:
  + `print()` implicitly coerces to a string before printing it
  + mixing number types in an [expression](#expressions-and-statements):
    + Adding an integer and a float outputs a float
  + Booleans are coerced to integer values of 1 or 0 in arithmetic expressions:
 
        print(True + True + True) # outputs 3
  + Truthiness of any value (regardless of type) in conditional expressions:

        has_value = 3
        if has_value:
            print('This is not zero')
    + `if has value` evaluates to `True` so the print statements executes

+ Literals are direct representations of objects in source code:
  + `3.88` is a literal,whereas `range(0, 10)` is a type constructor

## numbers

+ Represented by numeric values - mathematical operations can be performed on them
  + integers, floats, complex, decimal, fractions (also binary, octal, hexadecimal)
+ Integers are whole numbers with no decimal part but cannot be grouped using commas (underscores can be used instead)
+ Floats are similar but have a decimal part 
+ Large numbers are handled differently depending on the number type:
  + Floats - printed using scientific notation
  
        3.14 * (10 ** 7) # 3.14e+7

  + Integers - to display a large integer using scientific notation

        int(3e+7) # 30000000

## strings

+ also known as text sequences, they are just strings of Unicode characters
+ they can be treated as 'normal' sequences (i.e. characters can be indexed or iterated over)
+ however, they don't contain any objects (unlike sequences) - they only contain characters which are part of the value
+ string literals can be written in single, double or triple quotes
  + use single or double depending on what the string contains (triples can be useful if the string contains both single and double, or you want to go over multiple lines)
  + or, you can use `\` just before the quote which tells python to treat the next character as a literal character rather that what it may "mean" to Python
+ indexing must be one less that the length and negative numbers access from the end:

        my_str = 'abc'
        my_str[1] # b
        my_str[-1] # c (i.e. the last)
+ 'raw' strings prefix the literal with `r` and doesn't recognise backslashes:

        print('This backslash \\ is dope') # This backslash \ is dope
        print(r'This backslash \ is dope') # This backslash \ is dope
    + NB special case: cannot end with a single, unescaped `\`, even though they are not interpreted as escape sequences

## f-strings

+ formatted string literals - include string interpolation
+ prefix with an `f` and put the expression in curly braces (these can be included in the f-string by doubling up: `{{foo}}`)
+ can be used to format big numbers with `_` or `,`:

        print(f'{123456789.987654321:,}') # 123,456,789.98765433

## string methods

+ all methods are functions (not all functions are methods)
+ methods belong to classes and requires an object of that class to call it
+ they work with specific objects (i.e. strings)
+ they return a modified version of the object is it called on but do **not** mutate the original string:

        'abcde'.upper() # returns a modified version of the string object 'abcde'
    + the `upper` method from the `str` class is being called on the string object `'abcde'`

### capitalize, swapcase, upper, lower

+ **str.capitalize()** - first letter capitalised (titlecase, not uppercase - digraphs have first letter capitalised, not the full character which would be 2 characters), everything else lowercase
+ **str.swapcase()** - upper becomes lower, lower becomes upper
  + str.swapcase().swapcase() == str not always true (e.g. always True for standard ASCII, but not for extended ASCII or special Unicode characters)
+ **str.upper()** - changes to uppercase
  + same rules apply as above re. str.upper().upper()
+ **str.lower()** - changes to lowercase
  + same rules apply as above re. str.lower().lower()

### isalpha, isdigit, isalnum, islower, isupper, isspace

+ **isalpha()** - True if string has at least 1 character, and all are alphabetic
+ **isdigit()** - True if string has at least 1 character, and all are digits
+ **isalnum()** - True if string has at least 1 character, and all are alphanumeric (i.e. at least one of the following is True isalpha, isdecimal, isdigit or isnumeric)
+ **islower()** - True if string has at least 1 character, and all characters are lowercase
+ **isupper()** - True if string has at least 1 character, and all characters are uppercase
+ **isspace()** - True if string has at least 1 character, and all characters are whitespace
+ NB empty strings will return False

### strip, rstrip, lstrip, replace

+ These all take arguments:
+ **strip(characters)** - removes *leading* or *trailing* characters
  + Default is whitespace
  + characters is just a list of characters, not a specific combination:

            test_string = 'www.rightmove.com'
            test_string.strip('w.ocm') # 'example'

+ **rstrip(characters)** - as above but for *trailing* characters only.   (removesuffix() will remove a single suffix, not a set of characters)
+ **lstrip(characters)** - as above but for *leading* characters only.   (removeprefix() will remove a single prefix, not a set of characters)
+ **replace(old, new, count=-1)** - old occurrences replaced by new, specified by the count (from left to right). Default is all

### split, find, rfind



## boolean vs. truthiness



## None



## ranges



## list and dictionary syntax



## list methods: len(list), list.append(), list.pop(), list.reverse()



## dictionary methods: dict.keys(), dict.values(), dict.items(), dict.get()



## slicing (strings, lists, tuples)



## operators



### Arithmetic: +, -, *, /, //, %, **



### String operators: +



### List operators: +



### Comparison: ==, !=, <, >, <=, >=



### Logical: and, or, not



### Identity: is, is not



### operator precedence



## mutability and immutability



## pass by object reference



## variables



### naming conventions



### initialization, assignment, and reassignment



### scope



### global keyword



### variables as pointers



### variable shadowing



## conditionals and loops



### for



### while



## print() and input()



## exceptions (when they will occur and how to handle them)



## Functions:



### definitions and calls



### return values



### parameters vs. arguments



### nested functions



### output vs. return values, side effects



## expressions and statements



