def convert_temperature(temp, unit):
    if unit == 'F':
        return (temp - 32) * 5/9  # Fahrenheit to Celsius
    elif unit == 'C':
        return (temp * 9/5) + 32  # Celsius to Fahrenheit
    else:
        return "Invalid unit. Please use 'F' for Fahrenheit or 'C' for Celsius."

# Example usage:
# Convert 98.6 degrees Fahrenheit to Celsius
ftp = float(input("Enter the degree in Fahrenheit "))

ctp = convert_temperature(ftp, 'F')
print(f"{ftp} degrees Fahrenheit is {round(ctp, 2)} degrees Celsius")

# Convert 37 degrees Celsius to Fahrenheit
ctp = float(input("Enter the degree in Celsius "))
ftp = convert_temperature(ctp, 'C')
print(f"{ctp} degrees Celsius is {round(ftp, 2)} degrees Fahrenheit")
