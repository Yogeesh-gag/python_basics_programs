import math

t=float(input("Enter temperature in Fahrenheit :"))
v=float(input("Enter the wind speed in mph :"))

if abs(t)>50 or v<3 or v>120:
    print("Invalid input : |t| must be <=50 and 3<=v<=120")
else:
    wind_chill = 35.74 + (0.6215 * t) + ((0.4275 * t - 35.75) * math.pow(v, 0.16))

print(f"Tempertaure:{t:.2f}F")
print(f"Wind Speed: {v:.2f} mph")
print(f"Wind Chill:{wind_chill:.2f} F")