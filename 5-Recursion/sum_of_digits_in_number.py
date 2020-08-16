# returns the sum of all the digtis in a number using recusrion

def sum_of_digits(num):
    if num < 0:
        return num

    if num == 0:
        return 0
    else:
        return num%10 + sum_of_digits(num//10)



# starter code:
sum_of_digits(123456789 )  # the return value should be ---------> 45