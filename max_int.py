max_int=0
num_int = int(input("Input a number: "))    # Do not change this line
if num_int > 0:
    while num_int > 0:
        max_int=max(max_int,num_int)
        num_int = int(input("Input a number: "))

    else:
        print("The maximum is", max_int)    # Do not change this line