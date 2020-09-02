# creating the empty dictionary cache
d = {}

# defining our expensive function
def expensive_seq(x, y, z):
    # if our tuple is not in our dictionary
    if (x, y, z) not in d:
        # this is the base case which we should start with
        if x <= 0:
           d[(x, y, z)] = y + z
        # this is the case where we recurse closer to x = 0
        elif x > 0:
            d[(x, y, z)] = expensive_seq(x-1,y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
    # after putting the value into the dictionary, return it
    return d[(x, y, z)]

# this is computationally efficient because it stores each
# calculation into our dictionary one time, and uses those results
# to calculate the next larger result instead of re-doing all exponential calculations
# we are saving all exponential calculations into the table making it easier


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
