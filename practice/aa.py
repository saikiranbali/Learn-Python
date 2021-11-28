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