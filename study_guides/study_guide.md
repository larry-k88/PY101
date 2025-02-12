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
    - [booleans](#booleans)
    - [truthiness](#truthiness)
    - [short-circuiting](#short-circuiting)
  - [None](#none)
  - [ranges](#ranges)
  - [list and dictionary syntax](#list-and-dictionary-syntax)
    - [list](#list)
    - [dictionaries](#dictionaries)
  - [list methods: len(list), list.append(), list.pop(), list.reverse()](#list-methods-lenlist-listappend-listpop-listreverse)
  - [dictionary methods: dict.keys(), dict.values(), dict.items(), dict.get()](#dictionary-methods-dictkeys-dictvalues-dictitems-dictget)
  - [slicing (strings, lists, tuples)](#slicing-strings-lists-tuples)
  - [operators](#operators)
    - [Arithmetic: +, -, \*, /, //, %, \*\*](#arithmetic--------)
    - [String operators: +](#string-operators-)
    - [List operators: +](#list-operators-)
    - [Comparison: ==, !=, \<, \>, \<=, \>=](#comparison------)
    - [Logical: and, or, not](#logical-and-or-not)
      - [and](#and)
      - [or](#or)
      - [not](#not)
    - [Identity: is, is not](#identity-is-is-not)
    - [operator precedence](#operator-precedence)
  - [mutability and immutability](#mutability-and-immutability)
  - [pass by object reference](#pass-by-object-reference)
  - [variables](#variables)
    - [naming conventions](#naming-conventions)
    - [initialization, assignment, and reassignment](#initialization-assignment-and-reassignment)
    - [Scope](#scope)
      - [Global](#global)
      - [Local](#local)
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
    - [expressions](#expressions)
    - [statement](#statement)
    - [important points](#important-points)


## naming conventions: legal vs. idiomatic, illegal vs. non-idiomatic

+ Idiomatic - follow convention (PEP8)
+ Non-Idiomatic - don't follow convention (but still valid)
+ Illegal (invalid) - throw an error or do something unexpected

+ General Conventions for all **identifiers** (except Constants and Classes):
  + 'snake_case': lowercase letters, digits and underscores
  + start with a letter, separate words with underscores
  + `__` (double underscore) has a special meaning
  + letters and digits must be from standard ASCII (7-bit)
    + NB 8-bit ASCII is 'extended ASCII' and Unicode is variable (8-bit, 16-bit or 32-bit)
  
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
    + Adding an integer to a float outputs a float
  + Booleans are coerced to integer values of 1 or 0 in arithmetic expressions:
 
        print(True + True + True)
        --> output is 3

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
  
        3.14 * (10 ** 7)
        --> 3.14e+7

  + Integers - to display a large integer using scientific notation

        int(3e+7)
        --> 30000000

## strings

+ also known as text sequences, they are just strings of Unicode characters
+ they can be treated as 'normal' sequences (i.e. characters can be indexed or iterated over)
+ however, they don't contain any objects (unlike sequences) - they only contain characters which are part of the value
+ string literals can be written in single, double or triple quotes
  + use single or double depending on what the string contains (triples can be useful if the string contains both single and double, or you want to go over multiple lines)
  + or, you can use `\` just before the quote which tells python to treat the next character as a literal character rather that what it may "mean" to Python
+ indexing must be one less that the length and negative numbers access from the end:

        my_str = 'abc'
        my_str[1]
        --> b
        my_str[-1]
        --> c (i.e. the last character)
+ 'raw' strings prefix the literal with `r` and doesn't recognise backslashes:

        print('This backslash \\ is dope')
        --> This backslash \ is dope
        print(r'This backslash \ is dope')
        --> This backslash \ is dope

    + NB special case: cannot end with a single, unescaped `\`, even though they are not interpreted as escape sequences

## f-strings

+ formatted string literals - include string interpolation
+ prefix with an `f` and put the expression in curly braces (these can be included in the f-string by doubling up: `{{foo}}`)
+ can be used to format big numbers with `_`, `,` or `e`:

        print(f'{123456789.987654321:,}') # 123,456,789.98765433
        print(f'{123456789.987654321:e}') # 1.234568e+08

## string methods

+ all methods are functions (not all functions are methods)
+ methods belong to classes and requires an object of that class to call it
+ they work with specific objects (i.e. strings)
+ they return a modified version of the object is it called on but do **not** mutate the original string:

        'abcde'.upper() # returns a modified version of the string object 'abcde'
    + the `upper` method from the `str` class is being called on the string object `'abcde'`

### capitalize, swapcase, upper, lower

+ **str.capitalize()** - first letter capitalised (titlecase, not uppercase - digraphs have first letter capitalised, not the full character which would be 2 characters), everything else lowercase
  + **str.title()** - first letter of each word is capitalised but it treats whitespace and punctuation as word boundaries so beware. `str.capwords(string)` (from `import string') can solve this
+ **str.swapcase()** - upper becomes lower, lower becomes upper
  + str.swapcase().swapcase() == str not always true (e.g. always True for standard ASCII, but not for extended ASCII or special Unicode characters)
+ **str.upper()** - changes to uppercase
  + same rules apply as above re. str.upper().upper()
+ **str.lower()** - changes to lowercase (best for standard ASCII, but different to `casefold()` which is more useful when dealing with special characters or non-English language )
  + same rules apply as above re. str.lower().lower()

### isalpha, isdigit, isalnum, islower, isupper, isspace

+ **isalpha()** - True if string has at least 1 character, and all are alphabetic, False otherwise. (add `isascii()` if you need to exclude non-ASCII characters)
+ **isdigit()** - True if string has at least 1 character, and all are digits, False otherwise
+ **isalnum()** - True if string has at least 1 character, and all are alphanumeric (i.e. at least one of the following is True isalpha, isdecimal, isdigit or isnumeric), False otherwise
+ **islower()** - True if string has at least 1 character, and all characters are lowercase, False otherwise
+ **isupper()** - True if string has at least 1 character, and all characters are uppercase, False otherwise
+ **isspace()** - True if string has at least 1 character, and all characters are whitespace (includes tabs, newlines, carriage returns, vertical tabs and form feeds), False otherwise
+ NB empty strings will return False

### strip, rstrip, lstrip, replace

+ These can all take arguments:
+ **strip(characters)** - removes *leading* or *trailing* characters
  + default is whitespace

        string = '   3 spaces either side   '
        string.strip()
        --> '3 spaces either side'

  + characters must be either leading/trailing to be removed

        string = '?-*-mixture-*-?'
        string.strip('*')
        --> '?-*-mixture-*-?'

  + `?` is removed
    
        string = '?-*-mixture-*-?'
        string.strip('?')
        --> '-*-mixture-*-' 

  + the argument is just a list of characters, not a specific combination:

        string = 'www.rightmove.com'
        string.strip('w.ocm')
        --> 'rightmove'

+ **`rstrip(characters)`** - as above but for *trailing* characters only.   (`removesuffix()` will remove a single suffix, not a set of characters)
+ **`lstrip(characters)`** - as above but for *leading* characters only.   (`removeprefix()` will remove a single prefix, not a set of characters)
+ **`replace(old, new, count=-1)`** - `old` occurrences replaced by `new`, specified by the count (from left to right). Default is all (notation: `-1`)

### split, find, rfind

+ **split(sep=None, maxsplit=-1)**
  + returns a *list* of words, separated by the delimiter `sep`:

        string = 'him, her, they'
        string.split(',')
        # ['him', ' her', ' they']

  + runs left to right up to `maxsplit` times:

        string = 'him, her, they'
        string.split(',', 1)
        # ['him', ' her, they']
    
  + consecutive delimiters are not grouped and are returned as empty strings (this applies when the delimiter is set to `' '`):

        string = 'him,, her,, they'
        string.split(',')
        # ['him', '', ' her', '', ' they']

        string = 'him  her  they' # NB double spaces between words
        string.split(' ')
        # ['him', '', 'her', '', 'they']

  + delimiters can be multi-character

  + if sep=None (or not provided), a different algorithm runs which treats any consecutive whitespace as a single separator (resulting in no empty strings if there is leading/trailing whitespace)

        string = ''
        string.split()
        --> []

  + if a string has no delimiters, it returns the string:

        string = 'abcde'
        
        string.split()
        --> 'abcde'

        string.split('.')
        --> 'abcde'

        list(string) # to separate them
        --> ['a', 'b', 'c', 'd', 'e']

+ **find(sub, start, end)**
  + returns the index of the 1st character in the substring
  + `start` and `end` denote a slice (optional) - NB `,` not `:` syntax
    + leaving `end` blank defaults to end of string
  + if sub not found, returns -1

+ **rfind(sub, start, end)**
  + as above but returns the highest index (i.e. furthest to the right), rather than the 1st
  + if sub not found, returns -1 

+ Note the difference between taking a slice (a new string) and finding a substring within that (shorter) slice (1st example); and finding a substring within a sliced argument relative to the original string (2nd example):

        text = 'abc abc def abc'

        print(text[3:10].find('c'))     --> 3
        print(text.find('c', 3, 10))    --> 6

## boolean vs. truthiness

### booleans

+ Boolean values are either `True` or `False` - they are definitive versions of 'truthy' and 'falsy'
+ Logical operators return boolean values
+ They can behave as numerical values (True = 1 and False = 0)

### truthiness

+ 'truthy' and 'falsy' describe how objects behave in a Boolean context
+ expressions are evaluated based on truthiness, rather than an actual value of True/False:

        if 'a':
            print('hi')
        --> prints 'hi' as 'a' is truthy (but not True)

        if '':
            print('hi')
        --> prints nothing as '' is falsy (but not False)

+ *Falsy* values are as follows:
    + `False`
    + `None`
    + Any representation of zero: `0`, `0.0`, `0j`
    + Any empty collection/sequence: `''`, `()`, `[]`, `{}`, `set()`, `frozenset()`, `range(0)`
    + Any custom data types can define additional *falsy* values
+ Everything else is *truthy*:
  + e.g. [0] is truthy as the list itself is not empty
  
### short-circuiting

+ see [logical operators](#logical-and-or-not)
+ truthiness can be combined with short-circuiting as follows:
  + logical operators don't always return True or False - they care about the truthiness and return the final expression they evaluate:

        3 and 'foo'    --> 'foo'
        0 and 3        --> 0
        'foo' and 0    --> 0

        3 or 'foo'     --> 3
        0 or 3         --> 3
        'foo' or 0     --> 'foo'

## None

+ This is the absence of a value (not `0` or something empty/falsey/False)
+ The only member of the `NoneType` class

## ranges

+ range is a type; `range()` calls the constructor to create a range object - this object is an immutable sequence that contains integers (homogeneous) between 2 points
+ `range(start, end, step)`
+ if `start` is omitted, default is 0
+ `start` is inclusive, `end` is non-inclusive
  + range(5, 10) goes from 5 to 9 inclusive
+ `step` defaults to 1; -1 goes backwards
+ is it a lazy sequence - the object doesn't store all the numbers in the range (only the 3 values) until it is expanded/materialised
+ creating ranges requires them to be iterated over and put into a data structure:

        range(5, 10)            --> range(5, 10)
        list(range(5, 10))      --> [5, 6, 7, 8, 9]
        tuple(range(10, 5, -1)) --> (10, 9, 8, 7, 6)

+ ranges can be indexed (before expanding/materialising the range):

        range(5, 10)[1]         --> 6


## list and dictionary syntax

+ both are heterogeneous collections, specifically sequences
+ both are mutable
+ if multi-line, use trailing comma (do not use if not multi-line)
+ both support nesting

### list

+ `list()` creates an empty list
+ `list(iterable)` creates a list of the objects - can be used to create a shallow copy of the list (1st nested layer copies, inner layers copy the pointers only):

        list_1 = [1, 2, 3]
        list_2 = list(list_1)
        list_1 == list_2 --> True, same value
        list_1 is list_2 --> False, different objects

+ ordered
+ objects accessed/reassigned via indexing (0 up to 1 less than the list length)
+ element (or indexed) reassignment:

        numbers = [1, 2, 3]
        numbers[1] = 42
        --> numbers is now: [1, 42, 3]

+ IndexError if the index is out of range (applies to accessing and reassigning)

### dictionaries

+ not ordered by definition (but dicts do preserve insertion order)
+ these map a key (usually string) onto a value - the key is unique (trying to add a duplicate just replaces the value)
+ `len()` counts the pairs
+ instead of indexes, we use the keys to access/reassign values:

        number_pairs = {'one' : 1,
                       'two' : 2,
                       }
        number_pairs['one'] = 100
        # number_pairs is now: {'one' : 100,
                                'two' : 2,
                                }

+ `KeyError` if key doesn't exist (when accessing). NB it creates new key/value pair if trying to assign to a key that doesn't exist
+ keys must be 'hashable' (usually similar to immutable) - e.g. strings, tuples
+ `del` keyword removes the pair (`del variable` deletes the variable totally):

        del number_pairs['one']
        --> number_pairs is now: {'two': 2}

## list methods: len(list), list.append(), list.pop(), list.reverse()

+ `len(list)` - returns the number of elements in the list (elements could be single objects, nested lists/tuples/dicts etc.)
  
+ **all these methods are mutating (you can tell it's mutating as they usually return `None` when printed)**:
  + `list.append()` - adds item to end of a list (e.g. within a loop). To merge a list, or add more than one elements from an iterable (list, set, tuple etc., use `list.extend()`)
    + `list.insert(i, 'element')` - adds element before position i (i = -1 does not insert at the end, it inserts at position -2):

          list1 = [5, 7, 8]
          list1.insert(1, 6)
          --> list 1 is now: [5, 6, 7, 8] i.e. inserts before position 1

  + `list.pop(i)` - removes and returns element at position i, or the last element if left blank (IndexError if out of range)
    + `list.remove()` - searches for the object and removes the first occurrence (ValueError if no such object)
    + `list.clear()` - empties the sequence (works with dicts)
  + `list.reverse()` - reverses the sequence (use when you don't need to preserve the original list order):

        list1 = [1, 2, 3]
        list1.reverse()
        --> list1 is now: [3, 2, 1]

## dictionary methods: dict.keys(), dict.values(), dict.items(), dict.get()

+ `dict.keys()` - returns a dict_keys object (dictionary view object)
+ `dict.values()` - returns a dict_values object (dictionary view object)
+ `dict.items()` - returns a dict_items object (dictionary view object)
+ all 3 of the above get automatically updated if the dictionary is mutated
+ these objects are iterables so their contents can be iterated over (e.g. in loops)

+ `dict.get(key)` used instead of key access if unsure if the key exists as this returns `None` by default if not present (can be set as a parameter):

        number_pairs.get('three','Does Not Exist')
        --> 'Does Not Exist'

## slicing (strings, lists, tuples)

+ extracts a portion of the sequence (NB strings are treated like sequences here)
+ `[x:y]` where `x` is start (included) and `y` is stop (not included)
+ a third value `z` can be added for stepping (similar to ranges)
+ if `x` and `y` are the same, result is an empty slice
+ negative values can be used to count from the last element - NB it returns the elements from left to right, it's only the counting that's done in reverse:

        seq = 'abcdefghi'
        seq[3:7]    --> defg
        seq[-6:-2]  --> defg
        seq[-2:-6]  --> expect hgfe, but it doesn't read the string backwards, so returns ''

+ `seq[:]` returns a duplicate (shallow copy) - same as `seq[0:len(seq)]`
+ `seq[::-1]` returns a reversed copy i.e. a new object (therefore works with immutable objects)
  + similar to `seq.reverse()` but this mutates the original (cannot work on immutable strings/tuples)
+ slicing can be used as an assignment target (for mutable objects, not tuples or strings):

        seq = [1, 3, 5, 6, 8]
        seq[3:5] = [7, 9]
        --> seq is now: [1, 3, 5, 7, 9]

## operators

### Arithmetic: +, -, *, /, //, %, **

+ all work with built-in integer and float types (but also complex, decimal and fractions)
+ when mixing types, implicit [coercion](#type-coercions-explicit-eg-using-int-str-and-implicit) applies
+ when using `/`, the result is always a float, regardless of operand type
+ `//` returns the result rounded **down** to a whole number (NB if either operand is a float, the result will be a float, still rounded down):

        16 // 3   --> 5 (rounded down from 5.33)
        -16 // 3  --> -6 (rounded down from -5.33)
        16 // -3  --> -6 (rounded down from -5.33)
        -16 // -3 --> 5 (rounded down from 5.33)
  + does not work with complex numbers
+ `%` is the modulo operator and returns the remainder (if operands are positive)
  + if operands are negative, result has the same sign as the second operand but also satisfies an identity linking it to the `//` operator (not relevant now) 
+ operating on floats can lead to imprecision due to how real numbers are stored:

        0.1 + 0.2 == 0.3 --> False 
    + using `math.isclose`, or `decimal.Decimal` (note the use of strings) alleviates this:

            import math
            math.isclose(0.1 + 0.2, 0.3) --> True
            
            from decimal import Decimal
            Decimal('0.1') + Decimal('0.2) == Decimal('0.3') --> True

### String operators: +

+ will be reassignment
+ looks like addition and/or multiplication:

        '1' + '2' --> '12'
        'abc' * 3 --> 'abcabcabc'

### List operators: +

+ will be reassignment
+ this will combine the lists

        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        list1 + list2       # not mutating, this result would need assigning to a variable to use it
        --> [1, 2, 3, 4, 5, 6]

+ similar to the `extend()` method, except this *is* mutating:

        list1.extend(list2) # this mutates list1 (i.e. modifies in place)
        --> [1, 2, 3, 4, 5, 6]

    + this is equivalent to `list1 += list2` which is also mutating, not reassignment despite being called 'augmented assignment'. If left-hand operand was immutable, this would just be reassignment:

            list1 = [1, 2, 3]
            list2 = [4, 5, 6]
            id(list1) = # 12345678

            list1.extend(list2) # mutating, id numbers match
            id(list1) = # 12345678 

            list1 += list2 # mutating, id numbers match
            id(list1) # 12345678

            tuple1 = (1, 2, 3)
            tuple2 = (4, 5, 6)
            id(tuple1) = 87654321

            tuple1 += tuple2 # reassignment as tuples are immutable
            id(tuple1) = 99999999

### Comparison: ==, !=, <, >, <=, >=

+ compares value equality of its operands and return Boolean values
+ if the types of the operands are different, it returns `False`, except numbers:

        5 = '5'
        --> False (different types)

        1 == 1.0
        --> True (`int` and `float` with same value)
        NB large floats (> 18 sig figs) lack precision so may get unexpected False

+ for more/less than, strings are compared "lexicographically" which is character by character from left to right

        '24' < '3'
        --> True (the character '2' comes before '3')

+ Note that uppercase are 'smaller' than lowercase (order in ASCII table) - use `upper()` or `lower()` (or `casefold()`) methods to achieve case-insensitive comparison
+ as soon as the decision can be made, it returns:

        'abcdef' > 'abc'
        --> True (unable to continue taking character from shorter string, therefore longer string must be bigger)

+ For sets:
  + determines if it is a subset or superset:

        {3, 1, 2} < {2, 4, 3, 1}
        --> True, LHS is a subset of the RH

        {2, 4, 3, 1} > {3, 1, 2}
        --> True, LHS is a superset of the RHS

+ For lists/tuples:
  + goes element by element and compares them:

        [1, 2, 3] < [1, 2, 3, 4]
        --> True, LHS is shorter than the RHS so it stops comparing and assumes LHS is smaller

        (1, 4, 3) < (1, 3, 3)
        --> False, second element of LHS is 4, versus 3 on the RHS

### Logical: and, or, not

#### and

+ returns `True` if both operands are truthy
+ [short-circuiting applies](#short-circuiting)

#### or

+ returns `True` if either operand is truthy
+ [short-circuiting applies](#short-circuiting)

#### not

+ returns `True` when the operand is falsy and vice versa:

        not(4 == 4) # evaluates (4 == 4) first (True), then negates it
        --> False
+ parentheses are not necessary but they make it clearer
+ `not` takes a single operand - known as a **unary operator**

### Identity: is, is not

+ these compare the objects that the variables point at:
  + if they point to the same object (and therefore have the same value), `is` will return `True` (they will also have identical id numbers)
  + if they have the same value (i.e. satisfies the `==` operator), they are not necessarily the same object
+ NB 'interning' is a process which assigns a unique object to every value from -5 to 256 (and also some strings) - this means that their id will be the same even if the variables point to different objects:

        x = 5
        y = 5 (2 distinct objects, expect id to be different even though values are the same)
        id(x) == id(y)
        --> True

+ `is not` is simply the inverse

### operator precedence

+ terminology: operators with higher precedence "bind" more tightly to their operands
+ highest to lowest:
    + `()`
    + `**`, `*`, `/`, `//`, `%`, `+`, `-`
    + `==`, `!=`, `<=`, `<`, `>`, `>=`
    + `not`
    + `and`
    + `or`
+ if the operands are working with "non-values" (i.e. expressions), these need to be evaluated first:

        def value(n):
            print(n)
            return n

        print(value(3) + value(5) * value(7))

    + `value(3)` evaluates first, printing `3` and returning `3`
    + `value(5)` evaluates second, printing `5` and returning `5`
    + `value(6)` evaluates third, printing `7` and returning `7`
    + so we print 3, 5, 7 (on separate lines), then print the value of: (3 + 5 * 7), which is 3 + 35 = 38

+ short-circuiting makes it more complex:

        1 or 2 and 3
        --> 1 
        # `and` expression evaluated first to yield `3'
        # `1 or 3` short-circuits to 1

        0 or 2 and 3
        --> 3
        # `and` expression evaluated first to yield `3'
        # 0 or 3 evaluates to 3 (no short-circuiting)

        5 and 1 / 0
        --> ZeroDivisionError

        5 or 1 / 0
        --> 5 (1 / 0 never evaluated even though `/` has higher precedence than `or`)

+ some expressions will evaluate right-to-left (multiple assignments or multiple `**` operators) - they are **not** good practice:

        a = b = c = 3
        5 ** 3 ** 2 evaluates as 5 ** (3 ** 2), or 5 ** 9

+ make use of parentheses for clarity!

## mutability and immutability

+ see the [data types](#type-coercions-explicit-eg-using-int-str-and-implicit) table
+ mutation is the act of changing the value of the object in memory
+ you cannot do this to immutable objects, you will have to create a new object and change where the variable is pointing/referencing
  
## pass by object reference

+ pass by value:
  + the function has a copy of the original object 
  + anything the function does to the copy does not affect the original 
+ pass by reference:
  + the function has a reference to the original (a pointer)
  + anything the function does to the object affects the original
+ Python appears to do both:

        def change_name(name):
            name = 'bob'

        name = 'jim'
        change_name(name)
        print(name)
        --> 'jim' (the variable `name` is only changed within the function)

        def add_element(my_list):
            my_list.extend([4])

        my_list = [1, 2, 3]
        add_element(my_list)
        print(my_list)
        --> [1, 2, 3, 4] (object has been mutated)

+ Python uses 'pass by object reference':
  + we pass the reference to the object but whether the function modifies the original depends on the mutability of the object
  + **if the operation within the function mutates the argument, it will affect the original object** 

## variables

+ They label data to aid understanding of the program - they identify objects that the program uses

### naming conventions

+ make it easy for other programmers (and your future self)
+ accurate, descriptive and understandable
+ 'identifiers' includes names of variables, constants, functions, methods, classes, parameters and modules
+ see [here](#naming-conventions-legal-vs-idiomatic-illegal-vs-non-idiomatic) for more general rules for naming identifiers, but variables should be in snake_case

### initialization, assignment, and reassignment

+ creating and initialisation are the same thing, it's the process of giving the variable a value
+ it happens during an assignment statement:

        name = 'Boris' 
        # the variable `name` is assigned the string 'Boris'

+ reassignment is the process of giving the variable a new value
  
+ when assigning a variable, the expression on the RHS is evaluated first

+ augmented assignment (statement, not expression):
  + ****generally, using `a = a + b` will be reassignment. `a += b` will be reassignment too, unless a is mutable**
  + simply shorthand for reassigning a value based on a previous one

            number = 100
 
            number = number + 10 # this is reassignment
            number += 10 # does the same thing - augmented assignment
        
    + works with any data type that supports the operators (will be mutating with a mutable data type, reassignment if immutable)

### Scope

+ Scope is the part of the program that can access a particular identifier, "global" or "local":

#### Global

+ if the variable is initialised in the global (outermost) scope (i.e. not inside a function), it will be accessible anywhere (even inside functions)
  
#### Local
  
+ if the variable is initialised inside a function, it is only accessible from inside that function - it has local (function) scope and nothing outside the function can access it

+ Rule 1:
  + Variables defined in a function are local to it (cannot be accessed in outer scope)
+ Rule 2:
  + Variables defined in a function are local unless marked `global` or `nonlocal`
+ Rule 3:
  + Variables used (accessed) but not reassigned may be kept in the outer scope (reassigning will create a new variable)
+ Rule 4:
  + Peer scopes do not conflict - two functions with the same variable can exist, each with different values 
+ Rule 5: 
  + Nested function have their own scope - inner scopes can access outer scopes, but not the other way round
  
+ NB variables defined in blocks, like `if` or `while` loops do not have their own scope in the same way that functions do
+ functions can access variables *outside* of its location, but not *inside*
  + python searches the **lexical** scope (i.e. outer scopes) to find the nearest variable

        greeting = 'Salutations'

        def well_howdy(who):
            print(f'{greeting}, {who}') # variable is not in the function, so it looks outside to find it

        well_howdy('Angie')
        print(greeting)

        --> Salutations, Angie  # from the function
        --> Salutations         # from the print statement

+ sometimes, variables are in scope, but unassigned:

        def scope_test():
        if True:
            foo = 'Hello'
        else:
            bar = 'Goodbye'

        print(foo)
        print(bar)

        scope_test()
        --> Hello               # if branch runs
        --> UnboundLocalError   # else branch never runs, but bar is "in scope"

### global keyword

+ `global` - tells Python to look in the global scope (instead of creating a new one)
+ If it doesn't exist already, it simply creates the variable
  
          greeting = 'Salutations'

          def well_howdy(who):
              global greeting # rather than creating a new variable that shadows the outermost one, this re-assigns the global variable
              greeting = 'Howdy'
              print(f'{greeting}, {who}')
          
          well_howdy('Angie')
          print(greeting)

          --> Howdy, Angie
          --> Howdy

### variables as pointers

+ initialisation creates the variable name in Python
  + this points to memory address (usually in the stack)
  + at that memory address, there is another pointer to an address (usually in the heap) where the object is stored
+ reassignment simply creates a new object in the heap and the memory address in the stack changes from pointing at the old object, to the new one


### variable shadowing

+ occurs when identifiers (variables) share the same name in different scopes
+ it is the temporary hiding of the variable of the same name in the outer scope.
  
        greeting = 'Salutations' # this will be shadowed/hidden

        def well_howdy(who):
            greeting = 'Howdy' # this variable "shadows" the one above
            print(f'{greeting}, {who}')

        well_howdy('Angie')
        print(greeting) # this refers to the outer (first) variable

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

### expressions

 + these must be evaluated to produce a new object and determine their value
 + examples include:
   + Literals (e.g. `5`, `Jim`, `None`)
   + references to variables that have been defined
   + code containing [operators](#operators)
   + function calls (e.g. `print()`)
   + combinations of the above that evaluate to a single object
 + they produce a value that:
   + can be assigned to a variable
   + can be passed to a function/method
   + returned by a function or method
  
### statement

+ an instruction to perform an action - they do not return values, they just do something
+ examples include:
  + assignment (e.g. `x = 4`)
  + control flow (e.g. `if`, `for` etc.)
  + function/class definitions
  + return statements
  + import statements

### important points

+ expressions can be part of statements:

        y = x + 5
        # x + 5 is the expression in the assignment statement

+ 'stand-alone' expressions have return values that are ignored and therefore appear to be statements - considered to be both:

        3 + 4            # Simple expression
        pint('Hello')    # Function call; returns None
        my_list.sort()   # Method call; returns None    