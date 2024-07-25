# find is to give the index posistion of the sub string in the main string
str="welcome to python classroom"
sub="room"
print(str.find(sub,10,27))
print(str.find(sub,25,27)) #if the string is not present int the given range then it displays -1
print(len(str))