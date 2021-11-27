#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
num = int(input("enter a number : "))
check = int(input("Enter a check : "))
if(num%check==0):
    print("Even and divisble by "+str(check))
else:
    print("Not divisible by "+str(check))