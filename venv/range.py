#This is used to generate a sequence of numbers. the below one will save upto 5, exculding value 6
numbers = range(6)
print(numbers)
for i in numbers:
    print(i)

#the below will save sequence from 6 - 11, it will exclude 12
numbers = range(6,12)
print(numbers)
for i in numbers:
    print(i)
    
# first param is from
# second param is to, excluding the value
# third param is step, the diff between the values
numbers = range(6,20,2)
print(numbers)
for i in numbers:
    print(i)
    

#we dont need to sepearately store in number
for i in range(6,12):
    print(i)
    