sub1=int(input("enter subject 1="))
sub2=int(input("enter subject 2="))
sub3=int(input("enter subject 3="))

avg=int((sub1+sub2+sub3)/3)
print(avg)
if 90<avg:
    print("grade A")

elif 80<avg:
    print("grade B")
    
elif 70<avg:
    print("grade C")
    
elif 60<avg:
    print("grade D")
    
else:
    print("grade F")
    