# Your code here
import math
import random

# even though this function is too slow to use the whole time
# it can still be utilized within the slowfun function 
# to make new calculations and save the results
# so leave this function alone
def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

# make an empty hash 
d = {}

# iterate through our dictionary using the tuple.
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # if the tuple doesn't exist in the dictionary
    # do the calculation for it and add it to the dictonary
    if (x, y) not in d:
        d[(x, y)] = slowfun_too_slow(x,y)
    # after it's been added, return what's at the dictionary location
    return d[(x,y)] 

# Do not modify below this line!
# I modified below this line to import a timer.
# My lookup_table runs in about 5 seconds :3
import datetime
start_time = datetime.datetime.now()

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

end_time2 = datetime.datetime.now()
print(end_time2 - start_time)