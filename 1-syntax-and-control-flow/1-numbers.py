# Read through the following expressions and predict the output once printed.
# What data type will they evaluate to?
# Justify your predictions in a comment below each expression

# 1.
12*4
# int. Operation only with ints and the result is also an int.

# 2.
3*0.1
# float. Operation is executed with a float, so the result will always be float.

# 3.
0.1+6
# float. Same as 2.

# 4.
11.3-10
# float. Same as 2.

# 5.
13%2
# int. Same as 1.

# 6.
13%2.0
# float. Operation is executed with a float, so the result will always be float, 
# even if the result doesn't need decimals.

# 7.
2**8
# int. Same as 1.

# 8.
11+9
# int. Same as 1.

# 9.
6/10
# float. Although operation is only with ints, the result is a float.

# 10.
19//10
# int. Same as 1.

print(type(19//10))
