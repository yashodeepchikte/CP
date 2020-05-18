#    1 -> A
#   2 -> B
#   3 -> C
#   ...
#   26 -> Z
#   27 -> AA
#   28 -> AB 

number = int(input("enter the integer"))

value = dict(zip([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0] ,
                 list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')))
#print(value)
column = ""
while number:
    remainder = number%26
    if remainder == 0:
        number -= 1
    column += value[remainder]
    number = number//26
print(column)
    