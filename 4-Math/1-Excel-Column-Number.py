#A -> 1
#B -> 2
#C -> 3
#...
#Z -> 26
#AA -> 27
#AB -> 28

column = input("enter capital alphabets without spaces").upper()
value = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 
                 ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26])))
number = 0
i=0
while column:
    number = number + (26**i)*value[column[-1]] 
    column = column[:-1]
    i+=1
    
print(number)