print("Welcome to the Unit Converter!")
print("Please select the conversion option: ")
print("1. Convert from millimeters to meters")
print("2. Convert from meters to millimeters")
print("3. Convert from Newtons to Kilonewtons")
print("4. Convert from Kilonewtons to Newtons")
print("5. Convert from Celsius to Kelvin")
print("6. Convert from Kelvin to Celsius")
option = int(input("Enter your option (1 or 2 or 3 or 4 or 5 or 6): "))
if option == 1:
    value = float(input("Please enter the value you want to convert into meters: "))
    result = value / 1000
    print(f"The value in meters is: {result} m")
elif option == 2:
    User_input = float(input("Please enter the value you want to convert: "))
    result = User_input * 1000
    print(f"The value in millimeters is: {result} mm")
elif option == 3:
    value= float(input("Please enter the value you want to convert into Kilonewtons: "))
    result = value / 1000
    print(f"The value in Kilonewtons is: {result} kN")
elif option == 4:
    value = float(input("Please enter the value you want to convert into Newtons: "))
    result = value * 1000
    print(f"The value in Newtons is: {result} N")
elif option == 5:
    value = float(input("Please enter the value you want to convert into Kelvin: "))
    result = value + 273.15
    print(f"The value in Kelvin is: {result} K")
elif option == 6:
    value = float(input("Please enter the value you want to convert into Celsius: "))
    result = value - 273.15
    print(f"The value in Celsius is: {result} °C")
else:
    print("Invalid option selected. Please choose either 1, 2, 3, 4, 5, or 6.")