# Read through the following expressions and predict the output printed output.
# Justify your predictions in a comment below each expression

# 1.
30 > 12
# True

# 2.
4 < 4
# False

# 3.
12 == '12'
# False. Not loose equality

# 4.
7 < 7.0
# False. Instead of erroring

# 5.
if 'Python' > 'JavaScript':
    current_thoughts = '🐍🐍🐍'
else:
    current_thoughts = 'Take me back to Node!'

# Python emojis. Alphabetical?

# 6.
1 == True
# True. The True bool is represented as 1

# 7.
0.9 < True
# True. Same as 6.

# 8.
fav_animal = '🐈' if 36**2 > 1300 else '🐕'
# Dog. Condition is false, so it proceeds to else block. Dog is assigned to fav_animal

# 9.
14 > 5 and len('tree') == 8/2
# True. and keyword is splitting the conditions. Both must be True to evaluate to True overall

# 10.
5 or 0.7
# 5. 5 is truthy.
# If 0 or 0.7, then it will be 0.7.

# 11.
5 > 10 or 4
# 4. First condition is false, so proceed to right side of or keyword

print(5 > 10 or 4)
