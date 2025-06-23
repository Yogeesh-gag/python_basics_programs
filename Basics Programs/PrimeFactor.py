number=int(input("Enter the number :"))

if number<0:
    print("The entered number should be greater than 0")
else:
    print(f"The prime factors of {number} is :",end=" ")
    i=2
    while i*i<=number:
        while number%i==0:
            print(i,end=" ")
            number //=i
        i+=1
    if number>1:
        print(number)
    else:
        print()


