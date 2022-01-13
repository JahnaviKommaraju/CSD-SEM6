#3,6,9->fish
#5,0->bus
n=input("enter number: ")
s=""
for i in n:
    if(i=='3'or i=='6'or i=='9'):
        s=s+"Fish"
    elif(i=='5' or i=='0'):
        s=s+"Bus"
    else:
        s=s+i
print(s)