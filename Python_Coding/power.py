def calculate_power(base, exponent):
    
    result = pow(base, exponent)
    return result

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = calculate_power(base, exponent)
print("{base} raised to the power {exponent} is:",{result})
