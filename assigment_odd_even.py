#python program to find total number of odd and even elemets in a list .
list=[99,97,65,42,32,12,55,89]
even=0
odd=0
for i in list:
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print("Even number in list",even)
print("Odd number in list",odd)