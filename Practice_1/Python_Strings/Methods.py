# capitalize()
print("hello world".capitalize())  # Hello world

# casefold()
print("HELLO".casefold())  # hello

# center()
print("hello".center(10))  # '  hello   '

# count()
print("hello".count('l'))  # 2

# encode()
print("hello".encode())  # b'hello'

# endswith()
print("hello.txt".endswith('.txt'))  # True

# expandtabs()
print("a\tb".expandtabs(4))  # 'a   b'

# find()
print("hello".find('e'))  # 1

# format()
print("Hello, {}".format("Alice"))  # Hello, Alice

# format_map()
print("{name}".format_map({'name': 'Bob'}))  # Bob

# index()
print("hello".index('e'))  # 1

# isalnum()
print("abc123".isalnum())  # True

# isalpha()
print("abc".isalpha())  # True

# isascii()
print("hello".isascii())  # True

# isdecimal()
print("123".isdecimal())  # True

# isdigit()
print("123".isdigit())  # True

# isidentifier()
print("var_name".isidentifier())  # True

# islower()
print("hello".islower())  # True

# isnumeric()
print("123".isnumeric())  # True

# isprintable()
print("hello".isprintable())  # True

# isspace()
print("   ".isspace())  # True

# istitle()
print("Hello World".istitle())  # True

# isupper()
print("HELLO".isupper())  # True

# join()
print(",".join(["a", "b", "c"]))  # a,b,c

# ljust()
print("hello".ljust(10, '-'))  # hello-----

# lower()
print("HELLO".lower())  # hello

# lstrip()
print("   hello".lstrip())  # 'hello'

# maketrans() + translate() (қатар қолданылады)
trans = str.maketrans("ae", "AE")
print("apple".translate(trans))  # ApplE

# partition()
print("hello=world".partition('='))  # ('hello', '=', 'world')

# replace()
print("hello world".replace("world", "Python"))  # hello Python

# rfind()
print("hello".rfind('l'))  # 3

# rindex()
print("hello".rindex('l'))  # 3

# rjust()
print("hello".rjust(10, '-'))  # -----hello

# rpartition()
print("file.txt.bak".rpartition('.'))  # ('file.txt', '.', 'bak')

# rsplit()
print("a,b,c".rsplit(',', 1))  # ['a,b', 'c']

# rstrip()
print("hello   ".rstrip())  # 'hello'

# split()
print("a,b,c".split(','))  # ['a', 'b', 'c']

# splitlines()
print("line1\nline2".splitlines())  # ['line1', 'line2']

# startswith()
print("hello.py".startswith("hello"))  # True

# strip()
print("  hello  ".strip())  # 'hello'

# swapcase()
print("Hello".swapcase())  # hELLO

# title()
print("hello world".title())  # Hello World

# translate() — жоғарыда maketrans() мысалында көрсетілген

# upper()
print("hello".upper())  # HELLO

# zfill()
print("42".zfill(5))  # 00042