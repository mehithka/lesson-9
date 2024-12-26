num = int(input("enter an armstrong number:" ))

sum  = 0

temp = num

while temp>0:
    digit = temp % 10 
    sum += digit ** 3
    temp //= 10

if num == sum :
  print("this is an armstrong number")
else:
   print("this is not an armstorng number")

   