# Ask the user for a number and determine whether the number is prime or not using functions. (For those who have forgotten, 
# a prime number is a number that has no divisors.).

def prime(val):
    count=0
    for i in range(2,val):
        if(val%i==0):
            count+=1
    if(count==0):
        return str(val)+" is prime"
    else:
        return str(val)+" is not prime"

a = int(input("Enter a nunber : "))
print(prime(a))

#solution 2 using list comprehessions

num = int(input('Insert a number: '))
a = [x for x in range(2, num) if num % x == 0]

def is_prime(n):
	if num > 1:
		if len(a) == 0:
			print("Prime")
		else:
			print ("NOT prime")
	else:
		print ("NOT prime")
	
is_prime(num)