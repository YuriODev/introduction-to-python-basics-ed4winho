def is_symmetrical(number):
    num_str = str(number)
    if num_str == num_str[::-1]:
        return True
    else:
        return False     
number=int(input("enter a number"))
