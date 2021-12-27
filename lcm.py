# write a python program to calculate lcm of two numbers .

def lcm_of_two_numbers(a, b):

    """This function returns lcm of 2 numbers."""

    if a > b:
        greater = a
    elif b > a:
        greater = b

    while True:
        if ((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater+=1

    return f"The LCM of {a} and {b} is {lcm} "

print(lcm_of_two_numbers(40,15))

help(lcm_of_two_numbers)