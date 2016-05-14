# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'


# first way
def is_friend(s):
    if s[0] == 'D':
        return True
    return False

# second way
def is_friend(s):
	return s[0] == 'D'

print is_friend('Diane')
#>>> True

print is_friend('fred')
#>>> False

# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'


def is_friend(name):
    return name[0] == 'D'or name[0] == 'N'


# print is_friend('Diane')
# #>>> True

# print is_friend('Ned')
# #>>> True

# print is_friend('Moe')
#>>> False