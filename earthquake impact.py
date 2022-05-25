num1 = float(input("Enter earthquake magintude from (1 to 10) : "))
if num1 <= 0 and num1 > 10:
    print("Invalid input")
elif num1 > 0 and num1 <= 2.5:
    print(f" Magnitude of {num1} Millions earthquake each year")
    print("Usually not felt")
elif num1 > 2.5 and num1 <= 5.4:
    print(f"Magnitude of {num1} 500,000 earthquake each year")
    print("Often felt, but only causes minor damage")
elif num1 > 5.4 and num1 <= 6.0:
    print(f"Magnitude of {num1} 350 earthquake each year")
    print("Slight damage to buildings and other structures")
elif num1 > 6.0 and num1 <= 6.9:
    print(f"Magnitude of {num1} 100 earthquake each year")
    print("May cause a lot of damage in very populated areas")
elif num1 > 6.9 and num1 <= 7.9:
    print(f"Magnitude of {num1} 10-15 earthquake each year")
    print("Major earthquake , Serious damage")
else:
    print(f"Magnitude of {num1} One or two earthquake each year")
    print("Great earthquake , Can totally destroy communities near the epicenter")
