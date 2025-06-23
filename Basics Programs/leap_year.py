# Leap year checking
year=int(input("Enter the year :"))

if year<1000:
    print(f"Enter a year above 1000")
else:    
    if year%400==0 or year%100!=0 and year%4==0:
        print(f"{year} is a leap year...")
    else:
        print(f"{year} is not a leap year")