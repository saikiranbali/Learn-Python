numbers = (1,2,3,4,4,6)
print(numbers)

#tuples are immutable. we dont have insert, append functions in tuples
#numbers[0]=7 will give error as we cant insert valeues

#tuples are kind of linked lists used to store sequence of values
print(numbers.count(4))
#gives the no of occurances of 4 in  tuple
print(numbers.index(4))
#gives the first occurence of the index 4 in tuple