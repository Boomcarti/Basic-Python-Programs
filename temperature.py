
input_str = input("Enter a temperature in Fahrenheit: ")
fahrenheit_value = eval(input_str)

#Calculate equivalent Celsius value
celsius_value = (fahrenheit_value - 32)*(5/9)

# Calculate equivalent Kelvin value
kelvin_value = celsius_value + 273.15

print("The temperature in Celsius is:", celsius_value)
print("The temperature in Kelvin is:", kelvin_value)
