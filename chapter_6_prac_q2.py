sub1 = int(input("enter the marks sub1 :"))
sub2 = int(input("enter the marks sub2 :"))
sub3 = int(input("enter the marks sub3 :"))
percentage = ((sub1+sub2+sub3)*100)/300
if((sub1+sub2+sub3)/3 > 40 and (sub1>33 and sub2>33 and sub3>33)):
    print("you are pass")
    print(percentage)
else:
    print("you are fail")