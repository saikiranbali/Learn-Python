wt = float(input("Weight: "))
measure = input("(K)g or (L)bs :")
if(measure.lower()=='l'):
    print("Weight in KG : "+str(wt*0.45392))
else:
    print("Weight in LBs : "+str(wt*2.205))
