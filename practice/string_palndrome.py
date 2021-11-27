# solution 1
st = input("enter a string : ") #saikiran
ts =""
val = range(len(st)-1,-1,-1)
for item in val:
    ts=ts + st[item]

if(st == ts):
    print("Palendrome")
else:
    print("not a palin")


# solution 2
wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")



# solution 3
def reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]
	return x

word = input('give me a word:\n')
x = reverse(word)
if x == word:
	print('This is a Palindrome')
else:
	print('This is NOT a Palindrome')