import random

number=int(input("Enter the number of flips: "))
head=0
tail=0

if number<0:
    print(f"Please enter the postivie integer")
else:
    for i in range(number+1):
        if random.random()<0.5:
            tail +=1
        else:
            head +=1
head_percent=(head/number)*100
tail_percent=(tail/number)*100

print(f"Total number of flips:{number}")
print(f"Head :{head} {head_percent}%")
print(f"Tail :{tail} {tail_percent}%")