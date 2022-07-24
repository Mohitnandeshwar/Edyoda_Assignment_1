# Python Program to Reverse a word

st1 = input("Please enter your word : ")

st2 = ''

for i in st1:
    st2 = i + st2
    
print("Original = ", st1)
print("Reversed = ", st2)