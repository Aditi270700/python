# immutable datatype
# immutable cannot change state or contents

# int
# float
# Complex
# String
# Tuple
# set

# int
a=5
print(a, "is type of",type(a))

#  float
b=2.0
print(b, "is type of", type(b))


# complex
c=1+2j
print(c,"is type of", type(c))

# string
# A string is a collection of one or more characters put in a single quote, double
# quote or triple quote
# multiline string can be denoted using triple quote

s="this is a string"
print(s, type(s))
s='''
fghjhkjklklllk
ghhjbnm
vghbhj
'''
print(s,type(s))

s='10'
print(s,type(s))


# Tuple
# tuple is an ordered sequence of items same as a list
# it is defined within parentheses() where items are seperated by commas
# tuple is fast,because we cannot update,delete in tuple


t=(5,'aditi',1+3j)
print(t,type(t))


# set
# A set is an unordered collection of itens
# Every set element is unique(no duplicate) and must be
# immutable (cannot be changed)
#  {}

my_set = {1,2,3}
print(my_set)

s={10,20,10,30}
print(s,type(s))