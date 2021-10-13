m1 = int(input("Marks of student in subject 1: "))

m2 = int(input("Marks of student in subject 2: "))

m3 = int(input("Marks of student in subject 3: "))
#total assuming out of 50

if((m1/50)*100 < 33):
    print("fail")

elif((m2/50)*100 < 33):
    print("fail")
elif((m3/50)*100 < 33):
    print("fail")
elif((m1+m2+m3)/150*100 < 40):
    print("fail")
else:
   print("pass")