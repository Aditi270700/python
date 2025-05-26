# Bitwise operator
# bitwise operator works bits
# true=1     false=0

#     A     B       A&B      A|B       A^B

#     0     0        0        0          0
#     0     1        0        1          1
#     1     0        0        1          1
#     1     1        1        1          0

x=10
y=8
print(bin(x))
print(bin(y))
print(bin(x&y),x&y)
print(bin(x|y),x|y)