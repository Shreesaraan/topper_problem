register_number=int(input())
even=0
odd=0
while(register_number>0):
    digit=register_number%10
    if digit%2==0:
        even+=digit
    else:
        odd+=digit
    register_number//=10

if even==odd:
    print(True)
else:
    print(False)