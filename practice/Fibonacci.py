def febonocci(val):
    feb=[1,1]
    val1=1
    val2=1
    val3=0
    for i in range(1,val):
        val1=feb[i]
        val2=feb[i+1]
        val3=val1+val2
        feb.append(val3)
        
    return feb

val=int(input("Enter range : "))
print(febonocci(val))
