# 1 loop through the following list and print all of my favourite things.
my_favourite_things = ['raindrops on roses', 'whiskers on kittens',
                       'bright copper kettles, warm woolen mittens']

for one_favourite_thing in my_favourite_things:
    print(one_favourite_thing)

# 2 Create a loop which prints the numbers 5 to 1 on separate lines followed by 'THUNDERBIRDS ARE GO 🚀'

for i in range(5, 0, -1):
    print(i)

print('THUNDERBIRDS ARE GO 🚀')

# 3 Create a loop which loops and prints the three times table up to 30.
# eg. 1 x 3 = 3
#     2 x 3 = 6
#     3 x 3 = 9

for i in range(1, 31):
    print(f'{i} x 3 = {i * 3}')
