number1=int(input("Write a number : "))
for i in range(2,number1):
	if number1%i==0:
		print("It is not a prime no")
		break
else:
	print("It is a prime congratulations")

