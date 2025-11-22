number=int(input("Enter an n-digit number: "))
original_number=number
reversed_number=0
while number>0:
    digit=number%10
    reversed_number=reversed_number*10+digit
    number=number//10
if original_number==reversed_number:
    print("palindrome.")
else:
    print("not a palindrome.")