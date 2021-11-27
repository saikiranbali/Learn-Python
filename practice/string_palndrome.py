st = input("enter a string : ") #saikiran
ts =""
val = range(len(st)-1,-1,-1)
for item in val:
    ts=ts + st[item]

if(st == ts):
    print("Palendrome")
else:
    print("not a palin")