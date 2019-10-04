#Jason Reinhardt
#Period 1
# Dice Rolling Sim
import random

one=0
two=0
three=0
four=0
five=0
six=0
sides=[1,2,3,4,5,6]
roll= int(input("Enter the amount of rolls "))
rollNum=0
while rollNum < int(roll):
	rolls=random.choice(sides)
	print("\nRoll Number: "+ str(rollNum+1))
	if rolls== 1:
		print("The dice landed on 1")
		one=one+1
	elif rolls==2:
		print("The dice landed on 2")
		two=two+1
	elif rolls==3:
		print("The dice landed on 3")
		three=three+1
	elif rolls== 4:
		print("The dice landed on 4")
		four=four+1
	elif rolls== 5:
		print("The dice landed on 5")
		five=five+1
	elif rolls==6:
		print("The dice landed on 6")
		six=six+1
	rollNum=rollNum+1
print("\nTotal Rolls: "+ str(roll))
print("\n1s= "+ str(one))
print("2s= "+ str(two))
print("3s= "+ str(three))	
print("4s= "+ str(four))
print("5s= "+ str(five))
print("6s= "+ str(six))
print("\nResult %: ")
one= int(one)/int(roll)*100
two= int(two)/int(roll)*100
three= int(three)/int(roll)*100
four= int(four)/int(roll)*100
five= int(five)/int(roll)*100
six= int(six)/int(roll)*100
print("1s= "+str(one)+"%")
print("2s= "+str(two)+"%")
print("3s= "+str(three)+"%")
print("4s= "+str(four)+"%")
print("5s= "+str(five)+"%")
print("6s= "+str(six)+"%")