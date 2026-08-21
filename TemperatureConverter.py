print("----- TEMPERATURE CONVERTER -----")

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return (c + 273.15)

while True:
    try:
        temp = int(input("Enter Temperature: "))
        print("You input: ", temp)
        print("Celsius to Fahreheit: ", celsius_to_fahrenheit(temp))
        print("Fahreheit to Celsius: ", fahrenheit_to_celsius(temp))
        print("Celsius to Kelvin: ", celsius_to_kelvin(temp))
    except ValueError:
        print("Please input number only")